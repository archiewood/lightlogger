#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin


cd /home/pi/lightlogger/

git add .

git commit -m "hourly backup `date +'%Y-%m-%d %H'`"

git push -u origin master


