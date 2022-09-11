package main

import (
	"testing"
)

func TestMain(m *testing.M) {
	_ = MySQL.AutoMigrate(&Student{})
	_ = SQLite.AutoMigrate(&Student{})

	m.Run()
}

func BenchmarkMySQLInsert(b *testing.B) {
	for i := 0; i < b.N; i++ {
		addStudent(MySQL)
	}
}

func BenchmarkSQLiteInsert(b *testing.B) {
	for i := 0; i < b.N; i++ {
		addStudent(SQLite)
	}
}

func BenchmarkMySQLScan(b *testing.B) {
	for i := 0; i < b.N; i++ {
		queryStudent(MySQL)
	}
}

func BenchmarkSQLiteScan(b *testing.B) {
	for i := 0; i < b.N; i++ {
		queryStudent(SQLite)
	}
}

func TestSQLiteAddLargeData(t *testing.T) {
	for i := 0; i < 1000000; i++ {
		addStudent(SQLite)
	}
}
