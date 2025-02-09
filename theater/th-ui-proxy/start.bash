#!/usr/bin/bash

echo "Today is " `date`

echo $1

docker network create theater

docker compose -f docker-compose.yml -p ${USER} up -d

if [ "$1" = log ] ; then
    docker logs -f -t th-ui-proxy-${USER}
fi
