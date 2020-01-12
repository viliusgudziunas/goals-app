# Base image
FROM python:3.8.1-alpine

# Dependancies
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd

# Working directory
RUN mkdir -p /src/src/app
WORKDIR /usr/src/app

# Requirements
RUN pip install --upgrade pip && \
    pip install pipenv
COPY ./Pipfile /usr/src/app/Pipfile
RUN pipenv install --skip-lock --deploy --system

# Entrypoint
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# App
COPY . /usr/src/app

# Run server
CMD ["/usr/src/app/entrypoint.sh"]