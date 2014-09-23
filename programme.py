#!/usr/bin/python3

import argparse

liste_des_format_de_sortie = ['m3u','xspf','pls']

mon_parser_general = argparse.ArgumentParser()
non_regexp_group = mon_parser_general.add_argument_group("Simple filtering options")
regexp_group = mon_parser_general.add_argument_group("RegExp filtering")

mon_parser_general.add_argument("--time", required=True, type=int, help="Total playlist length, in minutes")
mon_parser_general.add_argument("--output", nargs=2, help="Output format "+str(liste_des_format_de_sortie)+" followed by filename (absolute or relative path, or '-' for stdout)")

non_regexp_group.add_argument("-g", "--genre", nargs=2, help="Genre to include to playlist, followed by the %% quantity")
non_regexp_group.add_argument("-s", "--sub-genre", nargs=2, help="Sub-genre to include to playlist, followed by the %% quantity")
non_regexp_group.add_argument("-b", "--band", nargs=2, help="Band or artist name to include in playlist, followed by the %% quantity")
non_regexp_group.add_argument("-a", "--album", nargs=2, help="Album title to include in playlist, followed by the %% quantity")
non_regexp_group.add_argument("-t", "--title", nargs=2, help="Track title to include in playlist, followed by the %% quantity")

regexp_group.add_argument("-G", "--RE-genre", nargs=2, help="Genre to include to playlist, followed by the %% quantity")
regexp_group.add_argument("-S", "--RE-sub-genre", nargs=2, help="Sub-genre to include to playlist, followed by the %% quantity")
regexp_group.add_argument("-B", "--RE-band", nargs=2, help="Band or artist name to include in playlist, followed by the %% quantity")
regexp_group.add_argument("-A", "--RE-album", nargs=2, help="Album title to include in playlist, followed by the %% quantity")
regexp_group.add_argument("-T", "--RE-title", nargs=2, help="Track title to include in playlist, followed by the %% quantity")

mes_args = mon_parser_general.parse_args()

print(mes_args)








