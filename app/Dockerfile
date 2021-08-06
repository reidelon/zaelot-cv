FROM python:3.9.6-slim-buster


ENV MICRO_SERVICE=/usr/src/app
RUN mkdir -p $MICRO_SERVICE
RUN mkdir -p $MICRO_SERVICE/static
# set working directory
# where the code lives
WORKDIR $MICRO_SERVICE
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update && apt-get install -y pipenv netcat gcc postgresql \
  && apt-get clean
# copy project
COPY . $MICRO_SERVICE
RUN pipenv install --system --deploy

# COPY ./entrypoint.sh $MICRO_SERVICE
CMD ["/bin/bash", "/usr/src/app/entrypoint.sh"]