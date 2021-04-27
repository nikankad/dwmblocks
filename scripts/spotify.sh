#!/bin/sh


#playing=""
#paused=""

status="$(/usr/bin/playerctl status)"
if [[ "$status" == "Playing" ]]; then
    playerctl metadata --format "[ $playing{{ artist }}-{{ title }}]"
elif [[ "$status" == "Paused" ]]; then
    # playerctl metadata --format "$paused  {{ artist }} - {{ title }}"
    playerctl metadata --format ""

else
    echo
fi
