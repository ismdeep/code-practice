package main

import (
	"fmt"
)

func main() {
	var testChan chan int
	testChan = make(chan int, 10)

	/* 往 Channel 中写入数据 */
	testChan <- 1

	var a int

	/* 从 Channel 中读取数据 */
	a = <- testChan

	fmt.Println(a)
}
