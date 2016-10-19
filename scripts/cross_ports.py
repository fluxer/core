#!/usr/bin/python2

import libpackage, os, sys
db = libpackage.Database()

match = None
for arg in sys.argv[1:]:
   match = arg

if not match:
    print('needs an extra argument')
    sys.exit(1)

print('Searching for cross ports in %s...' % match)
for target in db.remote_all():
    trepo = target.split('/')[5].replace('.git', '')
    if not trepo == match:
        continue
    # print(trepo)
    matches = []
    bdepends = db.remote_metadata(target, 'depends')
    bdepends.extend(db.remote_metadata(target, 'makedepends'))
    bdepends.extend(db.remote_metadata(target, 'optdepends'))
    bdepends.extend(db.remote_metadata(target, 'checkdepends'))
    for b in bdepends:
        bfull = db.remote_search(b)
        if not bfull:
            continue
        brepo = bfull.split('/')[5].replace('.git', '')
        if not brepo == trepo:
            matches.append(b)
    if matches:
       print('Cross port depends of %s: %s' % (os.path.basename(target), matches))