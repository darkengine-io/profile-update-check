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
import xml.etree.ElementTree as ET

versions = {}

for f in settings.fullPath:
  data = open(f).read().split('\n')

  for s in data:
    if s[:7] == 'project' and '][version]' in s:
      versions[(s[s.index('[')+1:s.index(']')])] = re.sub('[ "]', '', s[s.index('=')+1:])

for project in versions.items():
  try:
    manifest = ET.fromstring(urllib.request.urlopen("http://updates.drupal.org/release-history/"+project[0]+"/7.x").read())
    rec_major = manifest.find('recommended_major').text
    for release in manifest.find('releases').findall('release'):
      if release.find('version_major').text == rec_major:
        latestversion = release.find('version').text[4:]
        break

    if project[1] != latestversion:
      print(project[0])
      print(latestversion)
      print(project[1])
      print('')
  except:
    print('Couldn\'t fetch ' + project[0]+'\n')
