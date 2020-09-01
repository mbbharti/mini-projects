import mysql.connector



mydb=mysql.connector.connect(host='localhost',user='root',password='1234',database='db1')

cur=mydb.cursor()


# To create Database
# cur.execute("CREATE DATABASE db1")


s="CREATE TABLE form(name varchar(30) NOT NULL,email varchar(15) UNIQUE,gender varchar(7) NOT NULL,college varchar(50) NOT NULL,place varchar(20) NOT NULL,pin int(6) NOT NULL)"

cur.execute(s)
