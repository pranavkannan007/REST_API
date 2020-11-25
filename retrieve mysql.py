import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pranavkmk007",
  database="bookinfo"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM booksdata")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
