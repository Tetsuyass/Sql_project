CREATE DATABASE AgenceLocation;
USE AgenceLocation;

CREATE TABLE access (
login varchar (50) ,
password varchar(50),
clientId char(4) UNIQUE REFERENCES Client(codeC), 
access_level char(1) DEFAULT 'L'
);
INSERT INTO access (login, password, codec, access_level)
SELECT 
    concat(codec, '.', IFNULL(prenom, '')) AS login, 
    md5(concat(nom, IFNULL(prenom, ''), codec)) AS password, 
    codec, 
    'L'
FROM client;

CREATE TABLE PROPRIETAIRE (
    codeP CHAR(3) PRIMARY KEY, -- clé primaire
    pseudo VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    CHECK(regexp_like(email, '^[a-zA-Z0-9._%+-]{1,256}@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')),
    ville VARCHAR(50) NOT NULL,
    annee CHAR(4)
);

CREATE TABLE VOITURE (
    immat CHAR(6) PRIMARY KEY, -- clé primaire
    modele VARCHAR(50) NOT NULL,
    marque VARCHAR(50) NOT NULL,
    categorie VARCHAR(50),
    couleur VARCHAR(20),
    places TINYINT CHECK (places > 0) NOT NULL,
    achatA CHAR(4), -- année d'achat de la voiture
    compteur INT CHECK (compteur >= 0) NOT NULL,
    prixJ INT,
    codeP CHAR(3), 
    FOREIGN KEY (codeP) REFERENCES PROPRIETAIRE(codeP) -- référence à PROPRIETAIRE
);

-- Table CLIENT
CREATE TABLE CLIENT (
    codeC CHAR(4) PRIMARY KEY, -- clé primaire
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    age TINYINT,
    permis VARCHAR(20) UNIQUE NOT NULL,
    adresse VARCHAR(200),
    ville VARCHAR(50)
);

-- Table LOCATION
CREATE TABLE LOCATION (
	CodeC CHAR(4), -- clé étrangère
    immat CHAR(6), -- clé étrangère
    annee CHAR(4),
    mois CHAR(1),
    numLoc CHAR(5) PRIMARY KEY, -- clé primaire
    km INT CHECK (km > 0) NOT NULL,
    duree TINYINT CHECK (duree >= 0) NOT NULL,
    villeD VARCHAR(50) NOT NULL, -- ville de départ
    villeA VARCHAR(50) NOT NULL, -- ville d'arrivée
    dateD DATE NOT NULL, -- date de début
    dateF DATE NOT NULL, -- date de fin
    FOREIGN KEY (CodeC) REFERENCES CLIENT(codeC), -- référence à CLIENT
    FOREIGN KEY (immat) REFERENCES VOITURE(immat) -- référence à VOITURE
);

-- Vérifications des contraintes 
INSERT INTO client (`codeC`,`nom`,`prenom`,`age`,`permis`,`adresse`,`ville`) VALUES ('C659','Delon','Gerard',67,null,'rue internationale','Nantes');
INSERT INTO client (`codeC`,`nom`,`prenom`,`age`,`permis`,`adresse`,`ville`) VALUES ('C664','Boon',null,42,'757665','rue des tulipes','Marseille');
INSERT INTO proprietaire (`codeP`,`pseudo`,`email`,`ville`,`annee`) VALUES ('P14','Fred',null,'Paris','2008');
INSERT INTO proprietaire (`codeP`,`pseudo`,`email`,`ville`,`annee`) VALUES ('P37','Georges','gigi@','Neuilly','2015');
INSERT INTO proprietaire (`codeP`,`pseudo`,`email`,`ville`,`annee`) VALUES ('P89','Marcel','bozo@gmail.com','Lyon','2010');
INSERT INTO proprietaire (`codeP`,`pseudo`,`email`,`ville`,`annee`) VALUES ('P89','Marcel','bozo@gmail.com','Lyon','2010');
INSERT INTO location (`codeC`,`immat`,`annee`,`mois`,`numLoc`,`km`,`duree`,`villeD`,`villeA`,`dateD`,`dateF`) VALUES ('C658','23AA46','2015','6','B-264',0,0,'Montreuil','Montreuil','2023-01-01','2023-01-01');
INSERT INTO location (`codeC`,`immat`,`annee`,`mois`,`numLoc`,`km`,`duree`,`villeD`,`villeA`,`dateD`,`dateF`) VALUES (NULL,'71PO37','2015','4','D-49',61,0,'Paris','Neuilly','2023-01-01','2023-01-01');



