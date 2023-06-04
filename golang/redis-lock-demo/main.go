package main

import (
	"fmt"
	"math"
	"math/rand"
	"time"

	"github.com/go-redsync/redsync/v4"
	"github.com/go-redsync/redsync/v4/redis/goredis/v9"
	"github.com/redis/go-redis/v9"
)

func GetLockAndSayHello(id int) {
	// Create a pool with go-redis (or redigo) which is the pool redisync will
	// use while communicating with Redis. This can also be any pool that
	// implements the `redis.Pool` interface.
	client := redis.NewClient(&redis.Options{
		Addr: "127.0.0.1:6379",
	})
	pool := goredis.NewPool(client) // or, pool := redigo.NewPool(...)

	// Create an instance of redisync to be used to obtain a mutual exclusion
	// lock.
	rs := redsync.New(pool)

	// Obtain a new mutex by using the same name for all instances wanting the
	// same lock.
	mutexName := "global-mutex-demo-000"
	mutex := rs.NewMutex(mutexName, redsync.WithExpiry(10*time.Second))

	// Obtain a lock for our given mutex. After this is successful, no one else
	// can obtain the same lock (the same mutex name) until we unlock it.
	if err := mutex.Lock(); err != nil {
		// fmt.Println("Warn:", err.Error(), "id:", id)
		return
	}

	// Do your work that requires the lock.
	fmt.Println("Date:", time.Now().Format(time.RFC3339), "ID:", id, "say:", "Hi.")
	time.Sleep(time.Duration(rand.Intn(300)) * time.Millisecond)

	// Release the lock so other processes or threads can obtain a lock.
	if ok, err := mutex.Unlock(); !ok || err != nil {
		fmt.Println("Warn: mutex unlock failed", "Err:", err)
	}
}

func main() {
	for i := 0; i < 16; i++ {
		go func(id int) {
			for {
				GetLockAndSayHello(id)
			}
		}(i)
	}

	time.Sleep(math.MaxInt64)
}
