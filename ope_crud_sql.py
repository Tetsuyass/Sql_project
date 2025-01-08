import mysql.connector

# Connexion à la base de données
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="etudiant",     #utilisateur non-root avec accès.
        password="votre_mot_de_passe",
        database="AgenceLocation"
    )

# 1. Proposer une application (ex. Python) permettant de se connecter à la base de données et d’exécuter des
#opérations CRUD (2 opérations par type).

###### CREATE ######

# Création d'une nouvelle voiture
def create_car(conn, voiture_data):
    query = ("INSERT INTO VOITURE (immat, modele, marque, categorie, couleur, places, achatA, compteur, prixJ, codeP) "
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    with conn.cursor() as cursor:
        cursor.execute(query, voiture_data)
        conn.commit()

# Ajouter un propriétaire
def create_owner(conn, owner_data):
    query = ("INSERT INTO PROPRIETAIRE (codeP, pseudo, email, ville, anneel) "
             "VALUES (%s, %s, %s, %s, %s)")
    with conn.cursor() as cursor:
        cursor.execute(query, owner_data)
        conn.commit()

###### LECTURE ######

# Lecture des voitures
def read_cars(conn):
    query = "SELECT * FROM VOITURE"
    with conn.cursor() as cursor:
        cursor.execute(query)
        for car in cursor.fetchall():
            print(car)

# Lire les locations d'un client

def read_client_rentals(conn, codeC):
    query = "SELECT * FROM LOCATION WHERE CodeC = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (codeC,))
        for rental in cursor.fetchall():
            print(rental)


###### UPDATE #####

# Mise à jour du kilométrage
def update_car_km(conn, immat, new_km):
    query = "UPDATE VOITURE SET compteur = %s WHERE immat = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (new_km, immat))
        conn.commit()

# Modifier l'adresse d'un client

def update_client_address(conn, codeC, new_address):
    query = "UPDATE CLIENT SET adresse = %s WHERE codeC = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (new_address, codeC))
        conn.commit()


###### DELETE ######

# Suppression d'une voiture
def delete_car(conn, immat):
    query = "DELETE FROM VOITURE WHERE immat = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (immat,))
        conn.commit()

# Supprimer un client

def delete_client(conn, codeC):
    query = "DELETE FROM CLIENT WHERE codeC = %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (codeC,))
        conn.commit()


# Exemple d'utilisation
conn = connect_to_db()
create_car(conn, ('AB123CD', 'ModelX', 'Tesla', 'SUV', 'Red', 5, 2021, 0, 100, 'P01'))
read_cars(conn)
update_car_km(conn, 'AB123CD', 1500)
delete_car(conn, 'AB123CD')
conn.close()
