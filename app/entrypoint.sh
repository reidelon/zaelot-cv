#!/bin/sh


echo "Initializing postgres db..."

while ! nc -z cv-db 5432; do
  sleep 0.1
done

echo "postgres database has initialized successfully"
