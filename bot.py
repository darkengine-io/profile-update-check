#! /usr/bin/python3
try:
  import settings
except ImportError as e:
    print("ERROR: Failed to import settings.py. Make sure it exists and that no syntax errors are present. Detailed error follows.")
    print("-----------------------------------------------------------------------------------------------------------------------")
    print(e)
    exit()

import re
import urllib.request
from xml.dom import minidom

versions = {}

for f in settings.fullPath:
  data = open(f).read().split('\n')

  for s in data:
    if s[:7] == 'project' and '][version]' in s:
      versions[(s[s.index('[')+1:s.index(']')])] = re.sub('[ "]', '', s[s.index('=')+1:])

for project in versions.items():
  manifest = minidom.parseString(urllib.request.urlopen("http://updates.drupal.org/release-history/"+project[0]+"/7.x").read())
  latestversion = manifest.getElementsByTagName("version")[0].childNodes[0].nodeValue[4:]
  if project[1] != latestversion:
    print(project[0])
    print(latestversion)
    print(project[1])
    print('')
