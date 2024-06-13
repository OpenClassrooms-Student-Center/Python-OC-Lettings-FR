# Utiliser une image de base officielle Python
FROM python:3.8-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application dans le répertoire de travail
COPY . .

# Exposer le port sur lequel l'application va tourner
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]
