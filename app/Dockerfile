# pull official base image
FROM python:3.9.5-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update && apt-get install -y pipenv netcat gcc postgresql \
  && apt-get clean

COPY Pipfile* ./
RUN pipenv install --system --deploy

# add app
COPY . .