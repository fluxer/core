# Entropy?
Yes, random bits I use to build environments according to my current interests
and needs. In the past I've build environments that use musl libc, run games
via Wine and whatnot. Some one-offs, some made available to the public.
Currently, it uses pkgsrc on top of custom package manager and some other
goodies so I do not have to run VMs to test Katie and Katana port files.

# Ports
For more ports use pkgsrc, either https://github.com/fluxer/pkgsrc (with Linux
build fixes) or https://github.com/NetBSD/pkgsrc.

To bootstrap pkgsrc:
```
export SH=/bin/bash
cd /usr
git clone --depth=1 https://github.com/fluxer/pkgsrc
cd /usr/pkgsrc/bootstrap
./bootstrap --abi 64
```

Add the following to `/usr/pkg/etc/mk.conf`:
```
TOOLS_PLATFORM.paxctl?=         /bin/true

PKG_DEFAULT_OPTIONS=            -debug -doc -introspection
CFLAGS=                         -march=x86-64 -mtune=native -pipe -O2
CXXFLAGS=                       -march=x86-64 -mtune=native -pipe -O2
LDFLAGS=                        -Wl,-O1,--sort-common,--as-needed,--no-keep-memory
MAKE_JOBS=                      4
```

Make sure `bmake` and the the package tools are in `PATH`, use `bmake` to build
ports as you would on NetBSD.
