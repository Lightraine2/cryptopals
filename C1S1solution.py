#!/usr/bin/python

import binascii
import base64

def hexToBase64(s):
    decoded = binascii.unhexlify(s)
    return base64.b64encode(decoded).decode('ascii')

x = raw_input("Input your hex encoded string here:")
print "Taking hex encoded string and outputting to base64 encoded"
y = hexToBase64(x)
print "your Base64 encoded string is:"
print(y)
