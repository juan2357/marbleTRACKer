import json
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

  print(json.dumps(myresult, indent = 2))

mydb.close()

# mydb = mysql.connector.connect(
#   host = "database-1.c3gkloztdhyp.us-east-1.rds.amazonaws.com",
#   user="admin",
#   passwd="12345678",
#   database="marble"
# )
#
# print(mydb)
#
# mycursor = mydb.cursor()
#
# mycursor.execute("SELECT * FROM tweets")
#
# row_headers=[x[0] for x in mycursor.description]
#
# rv = cur.fetchall()
#    json_data=[]
#    for result in rv:
#         json_data.append(dict(zip(row_headers,result)))
#    return json.dumps(json_data)
# #
# # myresult = mycursor.fetchall()
# #
# # x[0] for x in myresult:
# #
# #   print(x)
#
# mydb.close()
