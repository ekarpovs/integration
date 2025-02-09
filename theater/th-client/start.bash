#!/usr/bin/bash

echo "Today is " `date`

echo $2

docker compose -f docker-compose.yml -p ${USER} up -d

if [ "$2" = log ] ; then
    docker logs -f -t th-client-${USER}
fi
