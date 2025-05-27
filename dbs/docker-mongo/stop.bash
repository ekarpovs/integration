#!/usr/bin/bash

echo "Today is " `date`

echo $1

if [ "$1" = down ] 
then
    docker compose -p alone-${USER} down -v
else
    docker compose -p alone-${USER} stop
fi