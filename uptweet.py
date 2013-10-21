#!/usr/bin/python
import psutil
import tweepy
import datetime
import uptime
#----------------------------------------
#Written by Paul Klein
#This is a simple script that I use to
#recieve texts for how my VPS is running.
#It uses psutil for memory usage, tweepy
#to sent the tweet out, datetime to print
#the date and time, and uptime to easily
#get uptime. This is my first ever python
#project! Some code sampled from online
#exampes (specifically the mem size definitions)
#--------------------------------------
# Gives a human-readable uptime string
def readableUptime():
        total_seconds = uptime.uptime()
def readableUptime():
        total_seconds = uptime.uptime()
        # Vars
        MINUTE  = 60
        HOUR    = MINUTE * 60
        DAY      = HOUR * 24
        # Get the days, hours, etc:
        days    = int( total_seconds / DAY )
        hours   = int( ( total_seconds % DAY ) / HOUR )
        minutes = int( ( total_seconds % HOUR ) / MINUTE )
        seconds = int( total_seconds % MINUTE )
        # Create String "N days, N hours, N minutes, N seconds"
        string = ""
        if days> 0:
         string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
        if len(string)> 0 or hours> 0:
         string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
        if len(string)> 0 or minutes> 0:
         string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
         string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
        return string;
#Converting Bytes for RAM output. Makes it readable
def convert_bytes(bytes):
    bytes = float(bytes)
    if bytes >= 1099511627776:
        terabytes = bytes / 1099511627776
        size = '%.2fT' % terabytes
    elif bytes >= 1073741824:
        gigabytes = bytes / 1073741824
        size = '%.2fG' % gigabytes
    elif bytes >= 1048576:
        megabytes = bytes / 1048576
        size = '%.2fM' % megabytes
    elif bytes >= 1024:
        kilobytes = bytes / 1024
        size = '%.2fK' % kilobytes
    else:
        size = '%.2fb' % bytes
    return size
#Building the status for the tweet
time = readableUptime()
mem = convert_bytes(psutil.avail_phymem())
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
status =  "Uptime: " +  time  + " Mem: " + mem +  " Date: " + date
##Twitter Auth Stuff##
##YOU MUST CHANGE THESE TO YOUR OWN OR IT WILL NOT WORK##
consumer_token = "consumer_token"
consumer_secret = "consumer_secret"
key = "access_token_key"
secret = "access_token_secret"
#Auth's the program, then tweets the status
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)
#Status sent!
api.update_status(status)
