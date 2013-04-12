#! /usr/bin/python3
try:
  import settings
except ImportError as e:
    print("ERROR: Failed to import settings.py. Make sure it exists and that no syntax errors are present. Detailed error follows.")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print(e)
    exit()

import re

data = open("base.make").read().split('\n')
lines = []
versions = {}

for s in data:
  if s[:7] == 'project' and '][version]' in s:
    versions[(s[s.index('[')+1:s.index(']')])] = re.sub('[ "]', '', s[s.index('=')+1:])
    lines.append(s)

print(versions)
