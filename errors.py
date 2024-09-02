#!/user/bin/env python3
"""Studing Exceptions in Python.

This script demonstrates how to handle exceptions in Python.
"""

import sys
from pathlib import Path

file_path = Path().cwd() / 'names.txt'

# First Approach
# LBYL - Look before you leap.

if file_path.exists():
    names = open(file_path).readlines()
else:
    print('Error: File not found.')
    sys.exit(1)

if len(names) >= 4:
    print(names[3])
else:
    print('Error: Missing name in the list.')
    sys.exit(1)

# Second Approach
# EAFP - Easier to ask for forgiveness than permission.
try:
    names = open(file_path).readlines()
except FileNotFoundError as error:
    print(f'Error: File not {error} found.')
    sys.exit(1)

try:
    print(names[3])
except IndexError as error:
    print(f'Error: {error} Missing name in the list.')
    sys.exit(1)
