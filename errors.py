#!/user/bin/env python3
"""Studing Exceptions in Python."""

import sys
from pathlib import Path

file_path = Path().cwd() / 'names.txt'

names = open(file_path).readlines()

# First Approach
# LBYL (Look Before You Leap)

if len(names) >= 4:
    print(names[3])
else:
    print('Errors: Missing name in the list.')
    sys.exit(1)
