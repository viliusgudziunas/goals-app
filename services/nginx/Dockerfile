# Base image
FROM nginx:1.17.7-alpine

# Update config
RUN rm /etc/nginx/conf.d/default.conf
COPY /dev.conf /etc/nginx/conf.d