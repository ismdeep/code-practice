package main

import (
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

func initSQLite() *gorm.DB {
	conn, err := gorm.Open(sqlite.Open("/tmp/db-data.db"))
	if err != nil {
		panic(err)
	}
	return conn
}
