#!/bin/bash

fails=""
aaa

inspect() {
    if [ $1 -ne 0 ]; then
        fails="${fails} $2"
    fi
}

# run users tests
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

# run client tests
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

# run end to end tests
e2e() {
  echo "\nRunning end-to-end tests!\n"
  type=$1
  if [[ "${type}" == "ci" ]]; then 
    ./node_modules/.bin/cypress run --config baseUrl=http://localhost:3007
  else
    ./node_modules/.bin/cypress run
  fi
  inspect $? e2e
}

docker-compose up -d --build
option=$1

# decide which tests are to be ran
if [[ "${option}" == "users" ]]; then users
elif [[ "${option}" == "client" ]]; then client
elif [[ "${option}" == "fix-users" ]]; then fix_users
elif [[ "${option}" == "e2e" ]]; then e2e
elif [[ "${option}" == "ci" ]]; then
  echo "\nRunning tests in continuous integration!\n"
  users
  client
  e2e ci
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