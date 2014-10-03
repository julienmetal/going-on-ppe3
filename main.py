#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import logging
import toolbox.configuration as conf
import toolbox.cli

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(filename)s(%(process)s) %(levelname)s:%(message)s')

    if sys.version_info < conf.min_version_python :
        logging.critical("Python %i.%i is required" % (conf.min_version_python[0], conf.min_version_python[1]))
        sys.exit(255)

    command_line = toolbox.cli.CLI()
    command_line.performParsingCLI()
    logging.getLogger().setLevel(getattr(logging, command_line.arguments.log))
    logging.debug("Command line arguments:" + repr(command_line.arguments))
    logging.shutdown()
