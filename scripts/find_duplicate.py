#!/usr/bin/python2

import os, libpackage
db = libpackage.Database()

processed = []
duplicate = []
print('Searching for duplicate ports...')
for target in db.remote_all():
    base = os.path.basename(target)
    if base in processed:
       duplicate.append(target)
    processed.append(base)

if duplicate:
    print('Duplicate ports: %s' % duplicate)