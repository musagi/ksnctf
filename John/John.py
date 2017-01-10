#!/usr/bin/python

import sys

for line in open('user.txt', 'r'):
    sys.stdout.write(line[7])

