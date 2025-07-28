FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files
COPY requirements.txt .

# Install Python dependencies globally
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user for security
RUN groupadd -r django && useradd -r -g django django

# Copy the source code
COPY . .

# Make the startup script executable
RUN chmod +x start.sh

# Create the directory for static files
RUN mkdir -p /app/staticfiles

# Collect static files (as root before changing permissions)
RUN python manage.py collectstatic --noinput --settings=oc_lettings_site.settings_production

# Change permissions for the django user
RUN chown -R django:django /app
# Switch to the django user
USER django
# Expose port 8000
EXPOSE 8000

# Default environment variables
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings_production

# Default command to start the application
CMD ["./start.sh"] 