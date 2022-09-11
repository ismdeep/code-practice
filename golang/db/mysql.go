package main

import (
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

func initMySQL() *gorm.DB {
	conn, err := gorm.Open(mysql.Open("root:db-123456@tcp(127.0.0.1:20001)/db?parseTime=true&loc=Local&charset=utf8mb4,utf8"))
	if err != nil {
		panic(err)
	}
	return conn
}
