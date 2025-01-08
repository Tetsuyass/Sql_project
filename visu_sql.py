from sqlalchemy import create_engine
import plotly.express as px
import pandas as pd

def connect_to_db():
    # Connexion avec SQLAlchemy
    db_url = "mysql+mysqlconnector://etudiant:Tokorico360@localhost/AgenceLocation"
    engine = create_engine(db_url, echo=False)
    return engine

engine = connect_to_db()

# Exemple 1 : Histogramme des voitures par catégorie
df1 = pd.read_sql("SELECT categorie, COUNT(*) as count FROM voiture GROUP BY categorie", con=engine)
fig1 = px.bar(df1, x='categorie', y='count', title='Nombre de voitures par catégorie')
fig1.show()

# Exemple 2 : Répartition des couleurs des voitures
df2 = pd.read_sql("SELECT couleur, COUNT(*) as count FROM voiture GROUP BY couleur", con=engine)
fig2 = px.pie(df2, names='couleur', values='count', title='Répartition des couleurs des voitures')
fig2.show()

# Exemple 3 : Kilométrage moyen par marque
df3 = pd.read_sql("SELECT marque, AVG(compteur) as avg_km FROM voiture GROUP BY marque", con=engine)
fig3 = px.scatter(df3, x='marque', y='avg_km', size='avg_km', color='marque', title='Kilométrage moyen par marque')
fig3.show()

# Exemple 4 : Locations par année
df4 = pd.read_sql("SELECT annee, COUNT(*) AS nb_locations FROM location GROUP BY annee ORDER BY annee", con=engine)
fig4 = px.line(df4, x='annee', y='nb_locations', markers=True, title='Locations par année')
fig4.show()

# Exemple 5 : Durée moyenne des locations par client
df5 = pd.read_sql("""
    SELECT client.codeC, client.nom, client.prenom, AVG(location.duree) AS duree_moyenne 
    FROM client 
    JOIN location ON client.codeC = location.codeC 
    GROUP BY client.codeC, client.nom, client.prenom 
    ORDER BY duree_moyenne DESC
""", con=engine)
fig5 = px.bar(df5, x='duree_moyenne', y='nom', orientation='h', title='Durée moyenne des locations par client')
fig5.show()

# Exemple 6 : Top 5 des villes avec le plus de départs de locations
df6 = pd.read_sql("""
    SELECT villeD, COUNT(*) AS nb_departs 
    FROM location 
    GROUP BY villeD 
    ORDER BY nb_departs DESC 
    LIMIT 5
""", con=engine)
fig6 = px.sunburst(df6, path=['villeD'], values='nb_departs', title='Top 5 villes de départ')
fig6.show()

# Exemple 7 : Histogramme des propriétaires ayant le plus de voitures
query7 = """
    SELECT proprietaire.pseudo, COUNT(voiture.immat) AS nb_voitures
    FROM proprietaire
    JOIN voiture ON proprietaire.codeP = voiture.codeP
    GROUP BY proprietaire.pseudo
"""
df7 = pd.read_sql(query7, con=engine)
fig7 = px.bar(df7, x='nb_voitures', y='pseudo', orientation='h', title='Propriétaires avec le plus de voitures')
fig7.show()

# Exemple 8 : Répartition des clients par tranche d'âge
query8 = """
    SELECT CASE 
        WHEN age BETWEEN 18 AND 25 THEN '18-25'
        WHEN age BETWEEN 26 AND 35 THEN '26-35'
        WHEN age BETWEEN 36 AND 50 THEN '36-50'
        ELSE '51+' END AS age_tranche,
        COUNT(*) AS nb_clients
    FROM client
    GROUP BY age_tranche
"""
df8 = pd.read_sql(query8, con=engine)
fig8 = px.bar(df8, x='age_tranche', y='nb_clients', title='Répartition des clients par tranche d\'âge')
fig8.show()

# Exemple 9 : Évolution des prix moyens des voitures par année d'achat
query9 = "SELECT achatA, AVG(prixJ) as prix_moyen FROM voiture GROUP BY achatA"
df9 = pd.read_sql(query9, con=engine)
fig9 = px.area(df9, x='achatA', y='prix_moyen', title='Évolution des prix moyens par année d\'achat')
fig9.show()

# Exemple 10 : Corrélation entre kilométrage et durée des locations
query10 = "SELECT compteur, duree FROM voiture JOIN location ON voiture.immat = location.immat"
df10 = pd.read_sql(query10, con=engine)
fig10 = px.scatter(df10, x='compteur', y='duree', title='Corrélation entre kilométrage et durée de location')
fig10.show()

# Fermez la connexion
engine.dispose()
