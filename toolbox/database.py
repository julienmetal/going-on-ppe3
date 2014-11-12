#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlalchemy
import logging
import sys
import toolbox.configuration

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
engineURL = sqlalchemy.engine.url.URL(toolbox.configuration.DB_DRIVERNAME,
                                      username=toolbox.configuration.DB_USER,
                                      password=toolbox.configuration.DB_USER_PASSWORD,
                                      host=toolbox.configuration.DB_HOST,
                                      port=toolbox.configuration.DB_PORT,
                                      database=toolbox.configuration.DB_DATABASE,
                                  )
try:
    engine = sqlalchemy.create_engine(engineURL)
except sqlalchemy.exc.NoSuchModuleError:
    logging.error("Engine '"+repr(toolbox.configuration.DB_DRIVERNAME)+"' is not recognized, please correct the DB_ENGINE value in the 'toolbox/configuration.py' file")
    sys.exit(1)

connection = None
#connection = engine.connect()

if __name__ == '__main__':
    import doctest
    doctest.testmod()