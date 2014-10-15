#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlalchemy
import configuration

metadata = sqlalchemy.MetaData()
tableMorceaux = sqlalchemy.Table(
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
engine = sqlalchemy.create_engine(configuration.DB_ENGINE
                                  +'://'
                                  +configuration.DB_USER
                                  +':'
                                  +configuration.DB_USER_PASSWORD
                                  +'@'
                                  +configuration.DB_HOST
                                  +':'
                                  +configuration.DB_PORT
                                  +'/'
                                  +configuration.DB_DBNAME
)
connection = engine.connect()

if __name__ == '__main__':
    import doctest
    doctest.testmod()