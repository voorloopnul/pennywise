#!/usr/bin/env python
"""Naval Fate.

Usage:
  ditto fastANI
  ditto prokka
  ditto quast
  ditto spades
  ditto trimmomatic
  ditto (-h | --help)
  ditto --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""
import os
import sys
from docopt import docopt
from ditto.tools.q import Quast
from ditto.tools.f import FastANI
from ditto.tools.p import Prokka
from ditto.tools.s import Spades
from ditto.tools.t import Trimmomatic

if __name__ == '__main__':
    arguments = docopt(__doc__, argv=sys.argv[1:2], version='Ditto v0.0.1')
    current_dir = os.getcwd()

    if arguments["fastANI"]:
        FastANI().run(sys.argv[2:], current_dir)
    elif arguments["quast"]:
        Quast().run(sys.argv[2:], current_dir)
    elif arguments["prokka"]:
        Prokka().run(sys.argv[2:], current_dir)
    elif arguments["trimmomatic"]:
        Trimmomatic().run(sys.argv[2:], current_dir)
    elif arguments["spades"]:
        Spades().run(sys.argv[2:], current_dir)
    else:
        print("Ditto can't change into this tool.")
