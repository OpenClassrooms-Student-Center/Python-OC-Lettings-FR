FROM python:3.8-slim

EXPOSE 8080

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# CMD python manage.py runserver 0.0.0.0:8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "oc_lettings_site.wsgi"]
