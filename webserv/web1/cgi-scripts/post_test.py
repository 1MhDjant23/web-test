#!/usr/bin/env python3

import os, sys

cl = int(os.environ.get("CONTENT_LENGTH", 0))
body = sys.stdin.read(cl) if cl > 0 else ""

print("Content-Type: text/plain")
print()
print("Body:", body)
