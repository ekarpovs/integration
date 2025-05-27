#!/usr/bin/bash

echo "Today is " `date`

echo $1

if [ "$1" = down ] 
then
    docker compose -f docker-compose.yml -p intgr-${USER} down -v
else
    docker compose -f docker-compose.yml -p intgr-${USER} stop
fi
