#!/bin/sh

DIR=/var/log/pop-captive

# Setup cron job daily at 4AM, DO NOT RUN AS ROOT!
# Append to /etc/crontab
# 0 4 * * * pop-captive /opt/pop-captive/scripts/remove-old-logs.sh

# Remove log files from older than 370 days (a bit more than a year)
# https://www.retsinformation.dk/eli/lta/2006/988
# Se paragraf 5 stk 2 og paragraf 9 hvor der står 1 år
find $DIR -type f -mtime +370 -exec rm {} \;
