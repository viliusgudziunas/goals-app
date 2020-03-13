#!/bin/bash

fails=""

inspect() {
    if [ $1 -ne 0 ]; then
        fails="${fails} $2"
    fi
}

# run tests for users service
users() {
  echo "\nRunning users tests!\n"
  docker-compose exec users pytest "project/tests" -s -p no:warnings --cov="project"
  inspect $? users
  docker-compose exec users flake8 .
  inspect $? users-style
  docker-compose exec users black . --check --exclude=migrations
  inspect $? users-lint
  docker-compose exec users /bin/sh -c "isort ./*/*/*.py --check-only --filter-files"
  inspect $? users-imports
}

# run tests for client service
client() {
  echo "\nRunning client tests!\n"
  docker-compose exec client react-scripts test --coverage --watchAll=false
  inspect $? client
}

# format users code
fix_users() {
  echo "\nFormatting users code!\n"
  docker-compose exec users black . --exclude=migrations
  docker-compose exec users /bin/sh -c "isort ./*/*/*.py --filter-files"
}

docker-compose up -d --build
option=$1
# run the proper tests
if [[ "${option}" == "users" ]]; then users
elif [[ "${option}" == "client" ]]; then client
elif [[ "${option}" == "fix-users" ]]; then fix_users
elif [[ "${option}" == "ci" ]]; then
  echo "\nRunning tests in continuous integration!\n"
  users
  client
  docker-compose down
else
  echo "\nThis option is not supported: ${option}"
  exit 1
fi

# return the proper code
if [ -n "${fails}" ]; then
  echo "Tests failed: ${fails}"
  exit 1
else
  echo "Tests passed!"
  exit 0
fi