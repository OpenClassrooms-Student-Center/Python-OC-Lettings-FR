#!/bin/bash

# Startup script for the Django application in production

echo "Starting Django application..."

# Wait for the database to be ready (if needed)
# sleep 5

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start Gunicorn
echo "Starting Gunicorn server..."
exec gunicorn --bind 0.0.0.0:8000 --workers 3 --timeout 120 oc_lettings_site.wsgi:application 