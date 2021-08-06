#!/bin/sh


echo "Initializing postgres db..."

while ! nc -z cv-db $DB_PORT; do
  sleep 0.1
done

echo "postgres database has initialized successfully"
