#!/bin/sh
#format: month day hour:minute:second AM/PM (e.g  April 03 12:32:12 PM)
CURRENTDATEONLY=`date +"%B %d %I:%M:%S %p"`

echo [${CURRENTDATEONLY}]