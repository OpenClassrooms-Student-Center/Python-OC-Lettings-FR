# Base image
FROM python:3.10-slim

# Prevent Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Copy requirements first (cache optimization)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect statics
RUN SECRET_KEY=dummy-secret-key \
    USE_SQLITE=true \
    python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Run server with start.sh script
RUN chmod +x start.sh

CMD ["./start.sh"]
