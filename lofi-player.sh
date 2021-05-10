#!/bin/bash
#
# CLI lofi music stream player
#
# Requirements:
# 1: youtube-dl:
# wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
# sudo chmod a+rx /usr/local/bin/youtube-dl
#
# 2: vlc:
# sudo apt install vlc

if [ "$#" == "0" -o "$1" == "study" ]
  then cvlc --quiet --no-video $(youtube-dl --get-url "https://www.youtube.com/watch?v=5qap5aO4i9A")
  elif [ "$1" == "sleep" ]
    then cvlc --quiet --no-video $(youtube-dl --get-url "https://www.youtube.com/watch?v=DWcJFNfaw9c")
  else echo "Unknown lofi stream"
fi
