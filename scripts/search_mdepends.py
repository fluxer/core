#!/usr/bin/python2

import sys
import libpackage
db = libpackage.Database()

match = None
for arg in sys.argv[1:]:
   match = arg

if not match:
    print('needs an extra argument')
    sys.exit(1)

print('Searching for build dependency of', match)
for target in db.remote_all():
    starget = target.replace('/var/cache/spm/repositories/', '')
    # print(starget)
    bdepends = db.remote_metadata(target, 'depends')
    bdepends.extend(db.remote_metadata(target, 'makedepends'))
    bdepends.extend(db.remote_metadata(target, 'optdepends'))
    bdepends.extend(db.remote_metadata(target, 'checkdepends'))
    if match in bdepends:
        print('Match found in', starget)