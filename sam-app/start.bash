#!/usr/bin/bash

echo "Today is " `date`

echo $1
#echo $2

docker compose -f docker-compose.yml -p intgr-${USER} up -d

if [ "$1" = log ] ; then
    docker logs -f -t sam-app-intgr-${USER}
fi
