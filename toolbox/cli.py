# -*- coding: utf-8 -*-

import argparse
import logging
import toolbox.configuration as conf

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


class CLI(object):
    def __init__(self):
        self.arguments = argparse.Namespace()
        self.mon_parser_general = argparse.ArgumentParser()
        self.non_regexp_group = self.mon_parser_general.add_argument_group("Simple filtering options")
        self.regexp_group = self.mon_parser_general.add_argument_group("RegExp filtering")
        self.setupParsingCLI()

    def performParsingCLI(self):
        self.arguments = self.mon_parser_general.parse_args()

    def setupParsingCLI(self):
        self.mon_parser_general.add_argument("--time",
                                             required=True,
                                             type=int,
                                             metavar="LENGTH_IN_MINUTES",
                                             help="Total playlist length, in minutes")
        self.mon_parser_general.add_argument("--log",
                                             choices=['DEBUG','INFO','WARNING','ERROR','CRITICAL'],
                                             default='WARNING')
        self.mon_parser_general.add_argument("--output",
                                             nargs=2,
                                             metavar=("{"+','.join(format for format in conf.liste_des_formats_de_sortie)+"}", 'FILENAME'),
                                             help="Output format {"+','.join(format for format in conf.liste_des_formats_de_sortie)+"} followed by filename (absolute or relative path, or '-' for stdout)",
                                             default=['m3u','-'])

        self.non_regexp_group.add_argument("-g", "--genre",
                                           action=appendTypeQuantity,
                                           nargs=2,
                                           metavar=('GENRE','QUANTITY'),
                                           help="Genre to be included to playlist, followed by the %% quantity")
        self.non_regexp_group.add_argument("-s", "--sub-genre",
                                           action=appendTypeQuantity,
                                           nargs=2,
                                           metavar=('SUB_GENRE','QUANTITY'),
                                           help="Sub-genre to be included to playlist, followed by the %% quantity")
        self.non_regexp_group.add_argument("-b", "--band",
                                           action=appendTypeQuantity,
                                           nargs=2,
                                           metavar=('BAND_NAME','QUANTITY'),
                                           help="Band or artist name to be included in playlist, followed by the %% quantity")
        self.non_regexp_group.add_argument("-a", "--album",
                                           action=appendTypeQuantity,
                                           nargs=2,
                                           metavar=('ALBUM_NAME','QUANTITY'),
                                           help="Album title to be included in playlist, followed by the %% quantity")
        self.non_regexp_group.add_argument("-t", "--title",
                                           action=appendTypeQuantity,
                                           nargs=2,
                                           metavar=('TRACK_TITLE','QUANTITY'),
                                           help="Track title to be included in playlist, followed by the %% quantity")

        self.regexp_group.add_argument("-G", "--RE-genre",
                                       action=appendTypeQuantity,
                                       nargs=2,
                                       metavar=('GENRE','QUANTITY'),
                                       help="Genre to be included to playlist, followed by the %% quantity")
        self.regexp_group.add_argument("-S", "--RE-sub-genre",
                                       action=appendTypeQuantity,
                                       nargs=2,
                                       metavar=('SUB_GENRE','QUANTITY'),
                                       help="Sub-genre to be included to playlist, followed by the %% quantity")
        self.regexp_group.add_argument("-B", "--RE-band",
                                       action=appendTypeQuantity,
                                       nargs=2,
                                       metavar=('BAND_NAME','QUANTITY'),
                                       help="Band or artist name to be included in playlist, followed by the %% quantity")
        self.regexp_group.add_argument("-A", "--RE-album",
                                       action=appendTypeQuantity,
                                       nargs=2,
                                       metavar=('ALBUM_NAME','QUANTITY'),
                                       help="Album title to be included in playlist, followed by the %% quantity")
        self.regexp_group.add_argument("-T", "--RE-title",
                                       action=appendTypeQuantity,
                                       nargs=2,
                                       metavar=('TRACK_TITLE','QUANTITY'),
                                       help="Track title to be included in playlist, followed by the %% quantity")
