#!/usr/bin/env python
from __future__ import division

"""
__init__: DESCRIPTION

data copyright Cynthia Brewer, see her license XXX
"""

__version__ = "$Revision$"

# Copyright 2009 Michael M. Hoffman <mmh1@washington.edu>

from collections import defaultdict
import sys

from pkg_resources import resource_string
from tabdelim import DictReader

try:
    # Python 2.6
    PKG = __package__
except NameError:
    PKG = "colorbrewer"

PKG_DATA = ".".join([PKG, "data"])

RES_COLORBREWER = "ColorBrewer_all_schemes_RGBonly3.csv"

def read_colorbrewer(iterable):
    res = defaultdict(dict)

    reader = DictReader(iterable)

    for row in reader:
        def int_cell(colname):
            return int(row[colname])

        color_name = row["ColorName"]

        if color_name:
            num_of_colors = int_cell("NumOfColors")

            colors = []
            res[color_name][num_of_colors] = colors

        try:
            colors.append(tuple(map(int_cell, "RGB")))
        except ValueError:
            # data section is over
            break

    return res

def _load_schemes():
    lines = resource_string(PKG_DATA, RES_COLORBREWER).splitlines()

    schemes = read_colorbrewer(lines)

    # copy schemes to module global variables
    globals().update(schemes)

_load_schemes()

def colorbrewer(*args):
    pass

def main(args=sys.argv[1:]):
    return colorbrewer(*args)

if __name__ == "__main__":
    sys.exit(main())
