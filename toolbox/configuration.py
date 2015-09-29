# -*- coding: utf-8 -*-

min_version_python = (3,2)

# DATABASE: see http://docs.sqlalchemy.org/en/rel_0_9/core/engines.html#sqlalchemy.engine.url.URL
DB_DRIVERNAME='postgresql'
DB_USER='etudiant'
DB_USER_PASSWORD=None
DB_HOST='172.16.99.2'
DB_PORT=None
DB_DATABASE='radio_libre'
DB_QUERY=None

# CLI
liste_des_formats_de_sortie = ['m3u','xspf','pls']
dictArgumentsCLI = {
    'genre' : {'short':'-g', 'long':'--genre', 'metavar':'GENRE', 'help':'Genre to be included to playlist, followed by the %% quantity'},
    'subgenre' : {'short':'-s', 'long':'--sub-genre', 'metavar':'SUB_GENRE', 'help':"Sub-genre to be included to playlist, followed by the %% quantity"},
    'band' : {'short':'-b', 'long':'--band', 'metavar':'BAND_NAME', 'help':"Band or artist name to be included in playlist, followed by the %% quantity"},
    'album' : {'short':'-a', 'long':'--album', 'metavar':'ALBUM_NAME', 'help':"Album title to be included in playlist, followed by the %% quantity"},
    'title' : {'short':'-t', 'long':'--title', 'metavar':'TRACK_TITLE', 'help':"Track title to be included in playlist, followed by the %% quantity"},
}
