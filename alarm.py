#!/usr/bin/env python3
from playsound import playsound
import sys, time, datetime, os

base_path = os.path.dirname(os.path.realpath(__file__))

if len(sys.argv) < 2:
    timing = input("Enter your alarm time! (format: hours:minutes:seconds)")
else:
    timing = sys.argv[1]

if timing.count(":") == 2:
    hours, minutes, seconds = timing.split(":")
    all_seconds = int(seconds)+int(minutes)*60+int(hours)*60*60
elif timing.count(":") == 1:
    minutes, seconds = timing.split(":")
    all_seconds = int(seconds)+int(minutes)*60
elif timing.count(":") == 0:
    all_seconds = int(timing)

start = time.time()
while 1:
    seconds_left = all_seconds-(time.time()-start)
    if seconds_left<=0:
        break
    sys.stdout.write("\r{}:{}:{}".format(int(seconds_left//3600),int((seconds_left%3600)//60),round(seconds_left%60,2)))
    sys.stdout.flush()
    time.sleep(0.05)

sys.stdout.write("\rREADY")

playsound(base_path+'/../alarm_sounds/alarm.mp3')