#!/usr/bin/bash

echo "Today is " `date`

echo $1

rand=${RANDOM}
docker run --rm --network host --name sio-client-${USER}-${rand} -d -it ekarpovs/sio-client-aarch64:1.0.0

if [ "$1" = log ] ; then
    docker logs -f -t sio-client-${USER}-${rand}
fi
