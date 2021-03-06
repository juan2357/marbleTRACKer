import tweepy
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

# pushing to mysql db
access_token = "1267470711209238531-4nsBlByecoMODDbuFPne7QUhtnc2rW"
access_token_secret = "rVZPSJXVam7MY1ZkAUFi4q0InSnbG7o3CYTEnveQqZ9hE"
consumer_key = "YDuuIEWVHtfGQQYJqqOH8CO1y"
consumer_secret = "DOXC7jWaMaMoTEt6pOfHN3qlsCHyTCnNptgVV9oA4R2uVlKlDq"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

search_word = ("#ML2020")

tweets = tweepy.Cursor(api.search,
                        q=search_word,
                        lang="en").items(3)

sourcedTweets = list()

for tweet in tweets:
    tj = tweet._json
    # print(json.dumps(tj, indent = 3))


    sourcedTweets.append((tweet.created_at, tj['user']['name'], tweet.text))
    # 
    # print('=' *100)
    # print('=' *100)
    #
    # # print(json.dumps(sourcedTweets, indent = 3))

sql = "INSERT INTO tweets (post_date, user_name, comment) VALUES (%s, %s, %s)"

mycursor.executemany(sql, sourcedTweets)

mydb.commit()



mydb.close()
