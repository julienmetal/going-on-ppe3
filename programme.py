#!/usr/bin/python3

import argparse

liste_des_format_de_sortie = ['m3u','xspf','pls']

mon_parser_general = argparse.ArgumentParser()
non_regexp_group = mon_parser_general.add_argument_group("Options simples de filtrage", "Spécifier simplement les termes à rechercher, auxquels il faut ajouter la quantité souhaitée en %")
regexp_group = mon_parser_general.add_argument_group("Filtrage RegExp", "Spécifier les termes à rechercher par des expressions rationnelles, auxquels il faut ajouter la quantité souhaitée")

mon_parser_general.add_argument("--time", required=True, type=int, help="Donner la durée totale de la playlist en minutes")
mon_parser_general.add_argument("--output", nargs=2, help="Donner le format de sortie de la playlist "+str(liste_des_format_de_sortie)+" suivi du nom du fichier de sauvegarde de la playlist (chemin absolu ou relatif, ou '-' pour stdout)")

non_regexp_group.add_argument("-g", "--genre", nargs=2, help="Spécifier le genre à intégrer à la playlist suivi de la quantité escompté en %%")
non_regexp_group.add_argument("-s", "--sous-genre", nargs=2, help="Spécifier le sous-genre à intégrer à la playlist suivi de la quantité escompté en %%")
non_regexp_group.add_argument("-b", "--band", nargs=2, help="Spécifier le nom de l'artiste ou du groupe (band) à intégrer à la playlist suivi de la quantité escompté en %%")
non_regexp_group.add_argument("-a", "--album", nargs=2, help="Spécifier l'album à intégrer à la playlist suivi de la quantité escompté en %%")
non_regexp_group.add_argument("-t", "--title", nargs=2, help="Spécifier le titre à intégrer à la playlist suivi de la quantité escompté en %%")

regexp_group.add_argument("-G", "--RE-genre", nargs=2, help="Spécifier le genre à intégrer à la playlist suivi de la quantité escompté en %%")
regexp_group.add_argument("-S", "--RE-sub-genre", nargs=2, help="Spécifier le sous-genre à intégrer à la playlist suivi de la quantité escompté en %%")
regexp_group.add_argument("-B", "--RE-band", nargs=2, help="Spécifier le nom de l'artiste ou du groupe (band) à intégrer à la playlist suivi de la quantité escompté en %%")
regexp_group.add_argument("-A", "--RE-album", nargs=2, help="Spécifier l'album à intégrer à la playlist suivi de la quantité escompté en %%")
regexp_group.add_argument("-T", "--RE-title", nargs=2, help="Spécifier le titre à intégrer à la playlist suivi de la quantité escompté en %%")


mes_args = mon_parser_general.parse_args()

print(mes_args)








