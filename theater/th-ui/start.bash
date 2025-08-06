#!/usr/bin/bash

echo "Today is " `date`

echo $1
echo $2

docker compose -f docker-compose.yml -p ${USER}-1 up -d

if [ "$2" = log ] ; then
    docker logs -f -t st-provider-${USER}-1
fi
