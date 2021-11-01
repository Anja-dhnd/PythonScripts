# Usage : python encrypt.py file.txt

import sys
import os
from Cryptodome.Cipher import AES
from Cryptodome import Random
from binascii import b2a_hex

