package main

import "gorm.io/gorm"

var MySQL *gorm.DB

var SQLite *gorm.DB

func init() {
	MySQL = initMySQL()
	SQLite = initSQLite()
}
