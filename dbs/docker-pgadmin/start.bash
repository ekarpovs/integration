#!/usr/bin/bash

echo "Today is " `date`

echo $1

docker compose -p only-${USER} up -d
