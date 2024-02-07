#!/bin/bash

# Check if the first argument is "-hard"
if [ "$1" == "-hard" ]; then
    # If "-hard" is passed as an argument, build with --no-cache
    docker-compose -f docker-compose.dev.yml build --no-cache
else
    # If no "-hard" argument, build without --no-cache
    docker-compose -f docker-compose.dev.yml build
fi

# Run Docker Compose
docker-compose -f docker-compose.dev.yml up
