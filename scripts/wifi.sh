#!/bin/bash

echo -e "GET http://google.com HTTP/1.0\n\n" | nc google.com 80 > /dev/null 2>&1

if [ $? -eq 0 ]; then
    #not connected
    echo ^c#E06C75^"[]"
else
    #connected
    echo ^c#98c379^"[]"
fi

case $BUTTON in
     1) st nmtui & ;;
     3) notify-send -t 2000 "$(iwgetid -r)" ;;
esac