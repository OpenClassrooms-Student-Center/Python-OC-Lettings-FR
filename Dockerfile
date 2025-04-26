FROM python:3.12.3-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings
ENV PYTHONUNBUFFERED=1

ARG SECRET_KEY
ARG SENTRY_DSN

ENV SECRET_KEY=${SECRET_KEY}
ENV SENTRY_DSN=${SENTRY_DSN}

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]
