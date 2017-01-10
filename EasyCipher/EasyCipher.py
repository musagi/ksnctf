#!/usr/bin/python

import codecs

input = open('EasyCipher.txt', 'r').read()
print codecs.decode(input, 'rot13')
