import mysql.connector

mydb = mysql.connector.connect(
  host = "database-1.c3gkloztdhyp.us-east-1.rds.amazonaws.com",
  user="admin",
  passwd="12345678",
  database="marble"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM tweets")

myresult = mycursor.fetchall()

for x in myresult:

  print(x)

mydb.close()
