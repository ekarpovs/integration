#!/usr/bin/bash

echo "Today is " `date`

echo $1

docker run --rm --network host --name sio-client-${USER} -d -it ekarpovs/sio-client-aarch64:1.0.0

if [ "$1" = log ] ; then
    docker logs -f -t sio-client-${USER}
fi
