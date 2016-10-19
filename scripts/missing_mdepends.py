#!/usr/bin/python2

import libpackage
db = libpackage.Database()

print('Searching for missing dependencies...')
for target in db.remote_all():
    starget = target.replace('/var/cache/spm/repositories/', '')
    # print(starget)
    bdepends = db.remote_metadata(target, 'depends')
    bdepends.extend(db.remote_metadata(target, 'makedepends'))
    bdepends.extend(db.remote_metadata(target, 'optdepends'))
    bdepends.extend(db.remote_metadata(target, 'checkdepends'))
    for dep in bdepends:
        if not db.remote_search(dep):
            print('Missing dependency of ' + starget, dep)