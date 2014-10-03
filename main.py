#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import argparse
import logging

def setLoggingLevelAccordingToCLI(logLevel):
    logging.getLogger().setLevel(getattr(logging,logLevel))


class appendTypeQuantity(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs == 2:
            super(appendTypeQuantity, self).__init__(option_strings, dest, nargs=nargs, **kwargs)
        else:
            logging.error("Option %s must have 2 arguments in its definition" % option_strings)
    def __call__(self, parser, namespace, values, option_string=None):
        try:
            quantity = abs(int(values[1]))
            values[1] = quantity if 100 >= quantity > 0 else None
        except ValueError:
            logging.error("Quantity Input value is Not A Number (NaN): '" + quantite + "'")
            sys.exit(1)
        current_dest_value = getattr(namespace, self.dest)
        if type(current_dest_value) is list:
            current_dest_value.append(values)
            setattr(namespace, self.dest, current_dest_value)
        else:
            logging.debug(values)
            setattr(namespace, self.dest, [values])


def parsingCLI():
    global mes_args
    mon_parser_general = argparse.ArgumentParser()
    non_regexp_group = mon_parser_general.add_argument_group("Simple filtering options")
    regexp_group = mon_parser_general.add_argument_group("RegExp filtering")
    mon_parser_general.add_argument("--time",
                                    required=True,
                                    type=int,
                                    metavar="LENGTH_IN_MINUTES",
                                    help="Total playlist length, in minutes")
    mon_parser_general.add_argument("--log",
                                    choices=['DEBUG','INFO','WARNING','ERROR','CRITICAL'],
                                    default='WARNING')
    mon_parser_general.add_argument("--output",
                                    nargs=2,
                                    metavar=("{"+','.join(format for format in liste_des_formats_de_sortie)+"}", 'FILENAME'),
                                    help="Output format {"+','.join(format for format in liste_des_formats_de_sortie)+"} followed by filename (absolute or relative path, or '-' for stdout)",
                                    default=['m3u','-'])

    non_regexp_group.add_argument("-g", "--genre",
                                  action=appendTypeQuantity,
                                  nargs=2,
                                  metavar=('GENRE','QUANTITY'),
                                  help="Genre to be included to playlist, followed by the %% quantity")
    non_regexp_group.add_argument("-s", "--sub-genre",
                                  nargs=2,
                                  metavar=('SUB_GENRE','QUANTITY'),
                                  help="Sub-genre to be included to playlist, followed by the %% quantity")
    non_regexp_group.add_argument("-b", "--band",
                                  nargs=2,
                                  metavar=('BAND_NAME','QUANTITY'),
                                  help="Band or artist name to be included in playlist, followed by the %% quantity")
    non_regexp_group.add_argument("-a", "--album",
                                  nargs=2,
                                  metavar=('ALBUM_NAME','QUANTITY'),
                                  help="Album title to be included in playlist, followed by the %% quantity")
    non_regexp_group.add_argument("-t", "--title",
                                  nargs=2,
                                  metavar=('TRACK_TITLE','QUANTITY'),
                                  help="Track title to be included in playlist, followed by the %% quantity")

    regexp_group.add_argument("-G", "--RE-genre",
                              nargs=2,
                              metavar=('GENRE','QUANTITY'),
                              help="Genre to be included to playlist, followed by the %% quantity")
    regexp_group.add_argument("-S", "--RE-sub-genre",
                              nargs=2,
                              metavar=('SUB_GENRE','QUANTITY'),
                              help="Sub-genre to be included to playlist, followed by the %% quantity")
    regexp_group.add_argument("-B", "--RE-band",
                              nargs=2,
                              metavar=('BAND_NAME','QUANTITY'),
                              help="Band or artist name to be included in playlist, followed by the %% quantity")
    regexp_group.add_argument("-A", "--RE-album",
                              nargs=2,
                              metavar=('ALBUM_NAME','QUANTITY'),
                              help="Album title to be included in playlist, followed by the %% quantity")
    regexp_group.add_argument("-T", "--RE-title",
                              nargs=2,
                              metavar=('TRACK_TITLE','QUANTITY'),
                              help="Track title to be included in playlist, followed by the %% quantity")
    mes_args = mon_parser_general.parse_args()


''' Main bloc'''
if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(filename)s(%(process)s) %(levelname)s:%(message)s')

    global mes_args
    global my_error

    my_error = 0
    liste_des_formats_de_sortie = ['m3u','xspf','pls']
    mes_args = argparse.Namespace()
    min_version_python = (3,2)

    if sys.version_info < min_version_python :
        logging.critical("Python %i.%i is required" % (min_version_python[0],min_version_python[1]))
        sys.exit(255)

    parsingCLI()
    setLoggingLevelAccordingToCLI(mes_args.log)
    logging.debug("Command line arguments:" + repr(mes_args))

    if my_error>0:
        sys.exit(my_error)

    logging.shutdown()
