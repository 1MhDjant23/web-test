#!/usr/bin/env python3

import os

print("Content-Type: text/plain")
print()

print("===== CGI ENVIRONMENT =====\n")
for k, v in sorted(os.environ.items()):
    print(f"{k}={v}")
