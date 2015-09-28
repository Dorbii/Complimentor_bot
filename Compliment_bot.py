import praw 
import time
import os
from datetime import datetime
from Config_bot import *

print ("Initializing...") #Starting up the bot
cache = []
subreddit_array = ["all"]
botCallToAction = ["complimentor_bot", "the", "tell me i'm pretty"]

print("Loggin in as %s..." %REDDIT_USERNAME)
# Create the instance 
user_agent = ("Make me feel pretty for /u/"+REDDIT_USERNAME) #Similar to UID
r = praw.Reddit(user_agent=user_agent)
# and login
r.login(REDDIT_USERNAME, REDDIT_PASS,disable_warning=True)

def run_bot():
	if not os.path.isfile("Config_bot.py"):
		print ("ERROR: Please check bot Config_bot file")
		exit(1)
	running = True
	n = 1
	while running:
		try:
			for nth_subreddit in subreddit_array:
				print("Searching subreddit %s..." %nth_subreddit)
				comments = r.get_comments(nth_subreddit) #Pulling the comments from subreddit  
				
				for comment in comments: #for all comments pulled
					Player_Comment = comment.body.lower() #typecasts comment to lower case
					Bot_Call = any(string in Player_Comment for string in botCallToAction) #Do they need a compliment?
					if comment.id not in cache and Bot_Call:
						comment.upvote()
						comment.reply ("You used to be beautiful")
						print("I made it better")
						cache.append(comment.id) #store comment id in cache 
			print ("I can only spread so much love")
			time.sleep(0) #Pause for 60 sec
		except KeyboardInterrupt:
			running = false
		except Exception as e: #Catch random errors
			print ('error: ', e)
			time.sleep(600)


run_bot()
