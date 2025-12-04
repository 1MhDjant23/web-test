#!/usr/bin/env python3

import os
qs = os.environ.get("QUERY_STRING", "")

print("Content-Type: text/plain")
print()
print("Query string:", qs)
