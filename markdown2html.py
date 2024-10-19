#!/usr/bin/python3

"""
Script using python.
"""
import sys
import os.path
import re
import hashlib

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        exit(1)

        length = len(line)
headings = line.lstrip('#')
heading_num = length - len(headings)

# Headings parsing
if 1 <= heading_num <= 6:
    line = '<h{}>'.format(heading_num) + headings.strip() + '</h{}>\n'.format(heading_num)
