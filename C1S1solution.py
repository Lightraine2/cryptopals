#!/usr/bin/python

import base64

string = input("Input string to encode...")

output = base64.b64encode(bytes('string', 'utf-8'))

print output
