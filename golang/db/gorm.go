package main

import (
	"fmt"
	"github.com/ismdeep/rand"
	"gorm.io/gorm"
)

type Student struct {
	ID   int    `gorm:"primaryKey"`
	Name string `gorm:"type:varchar(255)"`
}

func addStudent(db *gorm.DB) {
	if err := db.Create(&Student{
		Name: rand.HexStr(32),
	}).Error; err != nil {
		fmt.Println(err)
	}
}

func queryStudent(db *gorm.DB) {
	var stu Student
	if err := db.Model(&Student{}).Scan(&stu).Error; err != nil {
		fmt.Println(err)
	}
}
