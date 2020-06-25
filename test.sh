#!/bin/bash

# run the tests
docker-compose run -e ENVIRONMENT=TESTING api

exit_code_a=$?

# clean up afterwards
docker-compose down

exit_code_b=$?

exit $((exit_code_a + exit_code_b))
