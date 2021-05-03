#!/usr/plocal/bin/python3
import returnCards
from returnCards import *

################################################################################

def side_by_side(strings, size=700, space=4):
    strings = list(strings)
    result = []

    while any(strings):
        line = []

        for i, s in enumerate(strings):
            line.append(s[:size].ljust(size))
            strings[i] = s[size:]

        result.append((" " * space).join(line))

    return "\n".join(result)

###############################################################################

