#!/usr/bin/env python

#sajatID=773118564236685312
#Trump=25073877

from twython import Twython 
import time
import sys
import string
import simplejson


APP_KEY = 'DZ1oGQ5oovYcBrMakOLdDH0zh'
APP_SECRET = 'mC7kgkSzkPfeMQ04E1SOnDnftZofetQcWs5mIFsHlM4nBOw7Bq'
OAUTH_TOKEN = '773118564236685312-0nWaPky0ZQ6Cn4FgeZ8jSTTBJ85Vpul'
OAUTH_TOKEN_SECRET = 'U7ikfn6jfupKCvIUFWey5ke8WB2g1OS5j2RSqL2nH81cT'




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
	follower_id=twitter.get_followers_ids(user_id='1248382346',cursor=next_cursor)
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
	follower_id=twitter.get_followers_ids(user_id='478595317',cursor=next_cursor)
	#print follower_id
	time.sleep(60)
	#print "Next step"
	next_cursor=follower_id['next_cursor']
	#print next_cursor
	print "Finish"
	f.write(str(follower_id))
f.close()
