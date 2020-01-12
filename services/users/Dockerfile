# Base image
FROM python:3.8.1-alpine

# Working directory
RUN mkdir -p /src/src/app
WORKDIR /usr/src/app

# Requirements
RUN pip install --upgrade pip && \
    pip install pipenv
COPY ./Pipfile /usr/src/app/Pipfile
RUN pipenv install --skip-lock --deploy --system

# App
COPY . /usr/src/app

# Run server
CMD python manage.py run -h 0.0.0.0