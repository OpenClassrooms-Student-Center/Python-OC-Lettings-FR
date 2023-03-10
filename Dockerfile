FROM python:3.10.5-alpine

WORKDIR /code

# Add project files to the code/ folder
ADD ./ .

# Install dependencies
RUN pip install -r requirements.txt

# Define the default port
EXPOSE 8000

# Setup executable command in the container
CMD python manage.py runserver 0.0.0.0:8000