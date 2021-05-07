#!/bin/sh

#24 hour format
# CURRENTDATEONLY=`date +"%a %B %d %H:%M:%S"`
#12 hour format
CURRENTDATEONLY=`date +"%a %B %d %I:%M:%S %p"`

echo ^c#61AFEF^[${CURRENTDATEONLY}]

case $BUTTON in
     1) notify-send -t 2000 "$(uptime -p)" ;;
esac
