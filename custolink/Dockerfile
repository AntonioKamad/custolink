# Image de base à utiliser
FROM python:3.8-slim

# Changement du working directory de l'image à créer
WORKDIR /app

# Copie le dossier dans le container dans /app
COPY . /app

#Pour faire une purge et que certains éléments soient supprimés
RUN pip cache purge

# Installlation de tous les packages spécifiés dans le fichier requirements
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# INstallation de MySQL Connector pour Python, car avec l'installation de mariadb cela ne marche pas
RUN pip install mysql-connector-python

# Expose le port 5000 qui sera utilisé pour visiter le site
EXPOSE 5000

# Définition des variables d'environnement comme l'application à lancer et le hôte
ENV NAME custolink
ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0

#Faire la copie du dossier dans le container
COPY . .

#Lancement de l'application au démarrage de l'image
CMD ["flask", "run"]
