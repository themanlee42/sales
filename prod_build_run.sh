#!/bin/bash

# build the Docker images
docker-compose -f docker-compose.prod.yml build

# run Docker Compose
docker-compose -f docker-compose.prod.yml up
