#!/bin/sh

# Log 
echo "Waiting for the database..."
# Wait for netcat loop to confirm db is up
while ! nc -z $DATABASE_HOST 5432; do
    sleep 1
done
# Log
echo "Database is ready"
# Perform migrations
python manage.py migrate
# Run webserver
python manage.py runserver 0.0.0.0:8000