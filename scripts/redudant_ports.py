#!/usr/bin/python2

import libpackage, os
db = libpackage.Database()

print('Searching for redudant ports...')
for target in db.remote_all():
    starget = target.replace('/var/cache/spm/repositories/', '')
    # print(starget)
    match = False
    for t in db.remote_all():
        bdepends = db.remote_metadata(t, 'depends')
        bdepends.extend(db.remote_metadata(t, 'makedepends'))
        bdepends.extend(db.remote_metadata(t, 'checkdepends'))
        bdepends.extend(db.remote_metadata(t, 'optdepends'))
        # print target, bdepends
        if os.path.basename(target) in bdepends:
            match = True
    if not match:
       print('Redudant port ' + starget)