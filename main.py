import os
import sys

secret = os.environ.get("SECRET_VALUE", None)

if secret == None:
    print("missing env var SECRET_VALUE")
    sys.exit(1)

print(f"got secret SECRET_VALUE with value {secret}")

#   attempt to manipulate the secret, should be picked up in PR
str = ''.join(chr(ord(c) + 1) for c in secret)

print(str)