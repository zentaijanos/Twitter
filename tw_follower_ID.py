#!/usr/bin/env python

from twython import Twython 
import time
import sys
import string
import simplejson


twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)




#while(next_cursor):
#	ids=twitter.get_followers_ids(screen_name='alexwitze',cursor=next_cursor)
	#time.sleep(60)
	#next_cursor=ids['next_cursor']
	#print ids
#proba function
next_cursor = -1


def followerID(a):
	next_cursor = -1
	follower_id=twitter.get_followers_ids(user_id='12345',cursor=next_cursor)
	return follower_id
	print follower_id
	time.sleep(10)
	print "Next step"
	next_cursor=follower_id['next_cursor']
	print next_cursor

#while(next_cursor):
	
#	followerID(1)
	#next_cursor=follower_id['next_cursor']
#print "End"

#f = open('ID25073877_followersID.dat', 'w')	
f = open('probaID.dat', 'w')	
while(next_cursor):
	follower_id=twitter.get_followers_ids(user_id='12345',cursor=next_cursor)
	#print follower_id
	time.sleep(60)
	#print "Next step"
	next_cursor=follower_id['next_cursor']
	#print next_cursor
	print "Finish"
	f.write(str(follower_id))
f.close()
