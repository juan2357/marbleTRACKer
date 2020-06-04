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

allDB = "SELECT * FROM tweets"

mostPopularTeam = "SELECT hashtags AS Team, user_name as User, comment as comments, count(*) AS popTeam from tweets GROUP BY Team ORDER BY popTeam desc LIMIT 3"

teamLocation = "SELECT hashtags as Team, location_state as FanState, count(*) as TeamLocation from tweets GROUP BY Team ORDER BY TeamLocation desc limit 3"

mycursor.execute(allDB)

myresult = mycursor.fetchall()

for x in myresult:

    with open('json/allDB.json', 'w') as out_file:

        out_file.write('var allDB = %s;' % json.dumps(myresult, indent = 3))

mycursor.execute(teamLocation)

myresult = mycursor.fetchall()

for x in myresult:

    with open('json/teamLocation.json', 'w') as out_file:

        out_file.write('var teamLocation = %s;' % json.dumps(myresult, indent = 3))

mycursor.execute(mostPopularTeam)

myresult = mycursor.fetchall()

for x in myresult:

    with open('json/mostPopularTeam.json', 'w') as out_file:

        out_file.write('var mostPopularTeam = %s;' % json.dumps(myresult, indent = 3))



mydb.close()
