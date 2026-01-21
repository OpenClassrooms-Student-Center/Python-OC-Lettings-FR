FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ARG SECRET_KEY="temporary-insecure-key-for-local-build-only-do-not-use-in-production"
ENV SECRET_KEY=${SECRET_KEY}

COPY . .

RUN python manage.py makemigrations --noinput && \
    python manage.py migrate --noinput

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]
