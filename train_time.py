import requests
import vlc
from time import sleep
from gtts import gTTS
from secrets import *
from datetime import datetime, date


current_time = str(datetime.now().time())
current_time = current_time[0:5]

current_date = str(datetime.now().date())
print(current_date, current_time)


station = "WCY" #Waddon
# WCY - West Croydon
# ECR - East Croydon
# VIC - London Victoria
# LBG - London Bridge
# BFR - London Blackfriars

url = "https://transportapi.com/v3/uk/train/station/" + station + "/" + \
      current_date + "/" + current_time + "/timetable.json?app_id=" + app_id + \
      "&app_key=" + api_key + "&train_status=passenger"

r = requests.get(url)

if r:
      media = vlc.MediaPlayer("BingBong.mp3")
      media.play()
      sleep(4.2)

for i in range(len(r.json()['departures']['all'])):
      destination = (r.json()['departures']['all'][i]['destination_name'])
      departure = (r.json()['departures']['all'][i]['aimed_departure_time'])
      platform = (r.json()['departures']['all'][i]['platform'])
      operator_name = (r.json()['departures']['all'][i]['operator_name'])
      tts = gTTS("At " + str(departure) + " the train to " + str(destination) + " will depart from platform " + str(platform) + \
      " This service is provided by " + str(operator_name), lang="en-us")
      tts.save("announce.mp3")
      media = vlc.MediaPlayer("announce.mp3")
      media.play()
      sleep(10)
else:
      print("there was a bit of a pickle")

media = vlc.MediaPlayer("BingBong.mp3")
media.play()
sleep(4.2)

