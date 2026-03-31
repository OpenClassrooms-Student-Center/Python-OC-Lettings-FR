FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DJANGO_SETTINGS_MODULE=oc_lettings_site.settings \
    SECRET_KEY=build-secret-key-not-for-production

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

COPY test_db.sqlite3 /app/test_db.sqlite3

EXPOSE 8000

CMD ["sh", "-c", "echo '=== contenu /app/static ===' && ls /app/static/ && python manage.py collectstatic --noinput && gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000"]
