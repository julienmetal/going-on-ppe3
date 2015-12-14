#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Code écrit par Grégory David
import sqlalchemy
import logging
import sys
import toolbox.configuration

metadata = sqlalchemy.MetaData()
tableMorceaux = sqlalchemy.Table(
#Création de la table morceaux avec les champs que l'on veut allimenter lorsqu'on prend les données de la base.
    'morceaux', metadata,
    sqlalchemy.Column('titre', sqlalchemy.String, nullable=False),
    sqlalchemy.Column('album', sqlalchemy.String),
    sqlalchemy.Column('artiste', sqlalchemy.String),
    sqlalchemy.Column('genre', sqlalchemy.String),
    sqlalchemy.Column('sousgenre', sqlalchemy.String),
    sqlalchemy.Column('duree', sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column('format', sqlalchemy.String),
    sqlalchemy.Column('polyphonie', sqlalchemy.Integer),
    sqlalchemy.Column('chemin', sqlalchemy.String, nullable=False, primary_key=True),
)
#Connexion a la base de données.
engineURL = sqlalchemy.engine.url.URL(toolbox.configuration.DB_DRIVERNAME, #pointeur vers le nom du driver
                                      username=toolbox.configuration.DB_USER, #pointeur vers le nom de l'utilisateur pour se connecter a la base de donnée
                                      password=toolbox.configuration.DB_USER_PASSWORD, # pointeur vers le mot de passe de l'utilisateur
                                      host=toolbox.configuration.DB_HOST, #pointeur de l'adresse du driver
                                      port=toolbox.configuration.DB_PORT, #pointeur du port
                                      database=toolbox.configuration.DB_DATABASE, # ponteur vers la base de donéées a prendre
                                  )
try:
    engine = sqlalchemy.create_engine(engineURL)
except sqlalchemy.exc.NoSuchModuleError: #Gére les expception lorsqu'un un problème survient concernant l'adresse URL
    logging.error("Engine '"+repr(toolbox.configuration.DB_DRIVERNAME)+"' is not recognized, please correct the DB_ENGINE value in the 'toolbox/configuration.py' file")
    sys.exit(1)

connection = None
#connection = engine.connect()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
