# Base image
FROM python:3.8.1-slim

# Environment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Dependancies
RUN apt-get update && \
    apt-get -y install netcat && \
    apt-get clean

# Working directory
RUN mkdir -p /src/src/app
WORKDIR /usr/src/app

# Requirements
RUN pip install --upgrade pip && \
    pip install pipenv
COPY ./Pipfile /usr/src/app/Pipfile
COPY ./Pipfile.lock /usr/src/app/Pipfile.lock
RUN pipenv install --ignore-pipfile --deploy --system

# Entrypoint
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# Add app
COPY . /usr/src/app