# Base Image
FROM node:12.14.1-alpine

# Working directory
RUN mkdir -p /src/src/app
WORKDIR /usr/src/app

# Dependancies
COPY package.json /usr/src/app/package.json
COPY package-lock.json /usr/src/app/package-lock.json
RUN npm ci
RUN npm install react-scripts@3.3.0 -g --silent

# Environment
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# Start app
CMD ["npm", "start"]