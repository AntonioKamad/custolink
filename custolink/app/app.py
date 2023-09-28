# Imports pour le correct fonctionnement de l'appli
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Configuration de la connection MariaDB connection
db_config = {
    "host": "mariadb",
    "user": "flask",
    "password": "flask",
    "database": "MOCK_DATA",
}

# On spécifie la route sur laquelle l'application se lancera
@app.route('/')
def client_list():
    #On va essayer de établir la connection à la base de données
    try:
        # Connection à MariaDB
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Requête pour obtenir la data client de la base de données
        cursor.execute("SELECT * FROM MOCK_DATA")
        clients = cursor.fetchall()
        # Impression des données pour le debug
        print(clients)

        # Fermeture de la connection à la base de données 
        conn.close()

        # On retourne toutes les information de tous les clients de la base de données et on les passe la liste au fichier html comme "clients"
        return render_template('client_list.html', clients=clients)

    # Exeption et retour d'exeption
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

