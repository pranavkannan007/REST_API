import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pranavkmk007",
  database="bookinfo"
)

mycursor = mydb.cursor()

sql = "INSERT INTO booksdata (BookName, Author, Genre, PublishedYear) VALUES (%s, %s, %s, %s)"
val = ("The Hobbit", "J.R.R Tolkien", "Fantasy", "1937")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
