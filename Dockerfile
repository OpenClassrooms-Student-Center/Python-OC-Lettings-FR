# pull the official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /app

# create a user
RUN addgroup --system django \
    && adduser --system --ingroup django django

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 \
PYTHONUNBUFFERED 1
ENV PORT=8000
ENV SENTRY_DSN "$SENTRY_DSN"


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app
RUN pip install -r requirements.txt

# copy project
COPY . /app

RUN python manage.py collectstatic --noinput --clear

RUN chown -R django:django /app
USER django

CMD gunicorn oc_lettings_site.wsgi:application
