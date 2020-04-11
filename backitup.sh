#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin


cd /home/pi/lightlogger/

git add .

git commit -m 'backup hourly `date`'

git push -u origin master


