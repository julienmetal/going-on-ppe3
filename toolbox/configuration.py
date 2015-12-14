# -*- coding: utf-8 -*-
#Code written by Gregory David.
#Minimal version of python required to use this code.
min_version_python = (3,2)

# DATABASE: see http://docs.sqlalchemy.org/en/rel_0_9/core/engines.html#sqlalchemy.engine.url.URL
#Drivername of the BDD.(pointer)
DB_DRIVERNAME='postgresql'
#Username.(pointer)
DB_USER='etudiant'
#User password (pointer)
DB_USER_PASSWORD=None
#Host address. (pointer)
DB_HOST='172.16.99.2'
#Database port. (pointer)
DB_PORT=None
#Database targeted. (pointer)
DB_DATABASE='radio_libre'
#Database request. (pointer)
DB_QUERY=None

# CLI
#Output format. (pointer)
liste_des_formats_de_sortie = ['m3u','xspf','pls']
#Parser's optional arguments.
dictArgumentsCLI = {
#Argument specifying a kind.
    'genre' : {'short':'-g', 'long':'--genre', 'metavar':'GENRE', 'help':'Genre to be included to playlist, followed by the %% quantity'},
#Argument specifying a lesser kind.   
    'subgenre' : {'short':'-s', 'long':'--sub-genre', 'metavar':'SUB_GENRE', 'help':"Sub-genre to be included to playlist, followed by the %% quantity"},
#Argument specifying a band.
    'band' : {'short':'-b', 'long':'--band', 'metavar':'BAND_NAME', 'help':"Band or artist name to be included in playlist, followed by the %% quantity"},
#Argument specifying an album.
    'album' : {'short':'-a', 'long':'--album', 'metavar':'ALBUM_NAME', 'help':"Album title to be included in playlist, followed by the %% quantity"},
#Agrument specifying a title.
    'title' : {'short':'-t', 'long':'--title', 'metavar':'TRACK_TITLE', 'help':"Track title to be included in playlist, followed by the %% quantity"},
#Argument specifying a duration.
    'duration' : {'short':'-d', 'long':'--duration', 'metavar':'PLAYLIST_DURATION', 'help':"Playlist duration to be included in playlist, followed by the min quantity"},
}
