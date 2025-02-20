#!/usr/bin/bash

echo "Today is " `date`

echo $1
echo $2

EXTERNAL_URL=$1 docker compose -f docker-compose.yml -p ${USER} up -d

if [ "$2" = log ] ; then
    docker logs -f -t th-ui-proxy-${USER}
fi
