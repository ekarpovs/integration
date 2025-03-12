#!/usr/bin/bash

echo "Today is " `date`

echo $1

docker compose -p ${USER} up -d
if [ "$1" = log ] ; then
    docker logs -f -t six-keys-server-${USER}
fi
