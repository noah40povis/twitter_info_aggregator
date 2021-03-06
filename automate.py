import twint
import schedule
import time

# you can change the name of each "job" after "def" if you'd like.
def jobone():
	c = twint.Config()
	#tweets that contain these texts 
	c.Search = '$OPEN'
	c.Search = '$MP'
	c.Search = '$SNAP'
	c.Search = '$INAQ'
	c.Search = '$UUUU'
	c.Search ='$MP'
	#timeframe 
	c.Since = '2020-12-10'
	#language of tweets 
	c.Lang = "en"
	#c.Custom = ["date", "time", "username", "tweet", "link", "likes", "retweets", "replies", "mentions", "hashtags", "location"]
	c.Limit = 2000
	#store in elastic search instance
	c.Elasticsearch = "http://localhost:9200"
	twint.run.Search(c)

# def jobtwo():
# 	print ("Fetching Tweets")
# 	c = twint.Config()
# 	# choose username (optional)
# 	c.Username = "insert username here"
# 	# choose search term (optional)
# 	c.Search = "insert search term here"
# 	# choose beginning time (narrow results)
# 	c.Since = "2018-01-01"
# 	# set limit on total tweets
# 	c.Limit = 1000
# 	# no idea, but makes the csv format properly
# 	c.Store_csv = True
# 	# format of the csv
# 	c.Custom = ["date", "time", "username", "tweet", "link", "likes", "retweets", "replies", "mentions", "hashtags"]
# 	# change the name of the csv file
# 	c.Output = "filename2.csv"
# 	twint.run.Search(c)

# run once when you start the program

jobone()
#jobtwo()

# run every minute(s), hour, day at, day of the week, day of the week and time. Use "#" to block out which ones you don't want to use.  Remove it to active. Also, replace "jobone" and "jobtwo" with your new function names (if applicable)

#schedule.every(1).minutes.do(jobone)
schedule.every().hour.do(jobone)
# schedule.every().day.at("10:30").do(jobone)
# schedule.every().monday.do(jobone)
# schedule.every().wednesday.at("13:15").do(jobone)

# schedule.every(1).minutes.do(jobtwo)
#schedule.every().hour.do(jobtwo)
# schedule.every().day.at("10:30").do(jobtwo)
# schedule.every().monday.do(jobtwo)
# schedule.every().wednesday.at("13:15").do(jobtwo)

while True:
  schedule.run_pending()
  time.sleep(1)
