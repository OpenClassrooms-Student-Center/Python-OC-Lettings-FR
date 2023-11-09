# Utilisez une image de base Python
FROM python:3.9-slim

# Définissez le répertoire de travail dans l'image
WORKDIR /app

# Copiez les fichiers dans le répertoire de travail
COPY . /app

# Installez les dépendances de l'application
RUN pip install -r requirements.txt

# Exécutez les migrations et créez la base de données
RUN python manage.py migrate

# Exposez le port sur lequel l'application Django s'exécute
EXPOSE 8000

# Commande pour lancer l'application Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]