#!/bin/bash

# run the tests
docker-compose run -e ENVIRONMENT=TESTING api

# clean up afterwards
docker-compose down