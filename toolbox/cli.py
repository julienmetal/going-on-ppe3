# -*- coding: utf-8 -*-

import sys
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
        except ValueError:
            logging.warning("Quantity Input value is Not A Number (NaN): '" + values[1] + "'. Using None instead, and apply rules (see man page)")
            values[1] = None
        else:
            values[1] = quantity if quantity <= 100 else None

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
        self.mon_parser_general.add_argument("--log-filename",
                                             nargs='?',
                                             type=str,
                                             metavar="FILENAME",
                                             const="output.log",
                                             help="Output logging filename")
        self.mon_parser_general.add_argument("--output",
                                             nargs=2,
                                             metavar=("{"+','.join(format for format in conf.liste_des_formats_de_sortie)+"}", 'FILENAME'),
                                             help="Output format {"+','.join(format for format in conf.liste_des_formats_de_sortie)+"} followed by filename (absolute or relative path, or '-' for stdout)",
                                             default=['m3u','-'])

        for Argument in conf.dictArgumentsCLI:
            currentArgument = conf.dictArgumentsCLI[Argument]
            self.non_regexp_group.add_argument(currentArgument['short'],
                                               currentArgument['long'],
                                               action=appendTypeQuantity,
                                               dest=Argument,
                                               nargs=2,
                                               metavar=(currentArgument['metavar'], 'QUANTITY'),
                                               help=currentArgument['help']
                                           )
            self.regexp_group.add_argument(currentArgument['short'].upper(),
                                           currentArgument['long'].upper(),
                                           action=appendTypeQuantity,
                                           dest=Argument,
                                           nargs=2,
                                           metavar=(currentArgument['metavar'].upper(), 'QUANTITY'),
                                           help=currentArgument['help']
                                       )
