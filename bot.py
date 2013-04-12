#! /usr/bin/python3
import re

data = open("base.make").read().split('\n')
lines = []
versions = {}

for s in data:
  if s[:7] == 'project' and '][version]' in s:
    versions[(s[s.index('[')+1:s.index(']')])] = re.sub('[ "]', '', s[s.index('=')+1:])
    lines.append(s)

print(versions)
