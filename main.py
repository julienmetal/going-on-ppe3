#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import argparse
import logging

liste_des_format_de_sortie = ['m3u','xspf','pls']
mes_args = argparse.Namespace()


def setLoggingLevelAccordingToCLI(logLevel):
    logging.basicConfig(level=getattr(logging,logLevel), format='%(asctime)s %(levelname)s:%(message)s')


def validerQuantite(quantite):
    try:
        good = int(quantite)
        if good <= 0:
            raise Exception('UnderGround')
        logging.debug("Quantity '%i' is correct")
        return good
    except ValueError:
        logging.error("Quantity Input value is Not A Number (NaN): '" + quantite + "'")
        exit(1)
    except Exception as err:
        if err.args[0] == 'UnderGround':
            logging.error("Quantity Input value can not be negative: '%i'" % good)
            exit(1)


def parsingCLI():
    global mes_args
    mon_parser_general = argparse.ArgumentParser()
    non_regexp_group = mon_parser_general.add_argument_group("Simple filtering options")
    regexp_group = mon_parser_general.add_argument_group("RegExp filtering")
    mon_parser_general.add_argument("--log", choices=['DEBUG','INFO','WARNING','ERROR','CRITICAL'], default='WARNING')
    mon_parser_general.add_argument("--time", required=True, type=int, help="Total playlist length, in minutes")
    mon_parser_general.add_argument("--output", nargs=2, help="Output format "+str(liste_des_format_de_sortie)+" followed by filename (absolute or relative path, or '-' for stdout)", default=['m3u','-'])

    non_regexp_group.add_argument("-g", "--genre", nargs=2, metavar=('GENRE','QUANTITY'), help="Genre to include to playlist, followed by the %% quantity")
    non_regexp_group.add_argument("-s", "--sub-genre", nargs=2, metavar=('SUB_GENRE','QUANTITY'), help="Sub-genre to include to playlist, followed by the %% quantity")
    non_regexp_group.add_argument("-b", "--band", nargs=2, metavar=('BAND_NAME','QUANTITY'), help="Band or artist name to include in playlist, followed by the %% quantity")
    non_regexp_group.add_argument("-a", "--album", nargs=2, metavar=('ALBUM_NAME','QUANTITY'), help="Album title to include in playlist, followed by the %% quantity")
    non_regexp_group.add_argument("-t", "--title", nargs=2, metavar=('TRACK_TITLE','QUANTITY'), help="Track title to include in playlist, followed by the %% quantity")

    regexp_group.add_argument("-G", "--RE-genre", nargs=2, metavar=('GENRE','QUANTITY'), help="Genre to include to playlist, followed by the %% quantity")
    regexp_group.add_argument("-S", "--RE-sub-genre", nargs=2, metavar=('SUB_GENRE','QUANTITY'), help="Sub-genre to include to playlist, followed by the %% quantity")
    regexp_group.add_argument("-B", "--RE-band", nargs=2, metavar=('BAND_NAME','QUANTITY'), help="Band or artist name to include in playlist, followed by the %% quantity")
    regexp_group.add_argument("-A", "--RE-album", nargs=2, metavar=('ALBUM_NAME','QUANTITY'), help="Album title to include in playlist, followed by the %% quantity")
    regexp_group.add_argument("-T", "--RE-title", nargs=2, metavar=('TRACK_TITLE','QUANTITY'), help="Track title to include in playlist, followed by the %% quantity")
    mes_args = mon_parser_general.parse_args()


def main():
    global mes_args
    parsingCLI()
    setLoggingLevelAccordingToCLI(mes_args.log)
    logging.debug("Command line arguments:" + repr(mes_args))
    logging.debug("Validating arguments:")
    mes_args.genre[1] = validerQuantite(mes_args.genre[1])


if __name__ == "__main__":
    min_version = (3,2)
    if sys.version_info < min_version :
        logging.critical("Python %i.%i is required" % (min_version[0],min_version[1]))
        sys.exit(1)
    main()
