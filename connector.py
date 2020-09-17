import mysql.connector

MyDB = mysql.connector.connect(
host = "localhost",
user = "root",
password = "",
)

mycursor =  MyDB.cursor()

mycursor.execute('CREATE DATABASE gradingSysDB')

mycursor.execute('CREATE TABLE student( S_id INT AUTO_INCREMENT PRIMARY KEY, fname VARCHAR(120), lname VARCHAR(120), grade VARCHAR(30), class VARCHAR(30)')
mycursor.execute('CREATE TABLE teacher( T_id INT AUTO_INCREMENT PRIMARY KEY, fname VARCHAR(120), lname VARCHAR(120), teacher_id VARCHAR(30), class VARCHAR(30), passwd VARCHAR(120)')
