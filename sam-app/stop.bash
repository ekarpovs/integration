#!/usr/bin/bash

echo "Today is " `date`

echo $1

if [ "$1" = down ] 
then
    docker compose -f docker-compose.yml -p ${USER} down -v
else
    docker compose -f docker-compose.yml -p ${USER} stop
fi
