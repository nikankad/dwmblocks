#!/bin/sh

#format for time is day(eg. Wed) month day hour:minute:second
CURRENTDATEONLY=`date +"%a %B %d %H:%M:%S"`

echo ^c#61afef^[${CURRENTDATEONLY}]

