import mysql.connector

MyDB = mysql.connector.connect(
host = "localhost",
user = "root",
password = "",
)

mycursor =  MyDB.cursor()

mycursor.execute('CREATE DATABASE gradingSysDB')
