if [ -d /usr/local/lib/pkgconfig ] ; then
        pathappend /usr/local/lib/pkgconfig PKG_CONFIG_PATH
fi
if [ -d /usr/local/bin ]; then
        pathprepend /usr/local/bin
fi
if [ -d /usr/local/sbin -a $EUID -eq 0 ]; then
        pathprepend /usr/local/sbin
fi

# Set some defaults before other applications add to these paths.
pathappend /usr/share/man  MANPATH
pathappend /usr/share/info INFOPATH 

# pkgsrc paths.
if [ -d /usr/pkg/bin ]; then
        pathappend /usr/pkg/bin
fi

if [ -d /usr/pkg/sbin -a $EUID -eq 0 ]; then
        pathappend /usr/pkg/sbin
fi

if [ -d /usr/pkg/man ]; then
        pathappend /usr/pkg/man MANPATH
fi

if [ -d /usr/pkg/man ]; then
        pathappend /usr/pkg/man MANPATH
fi

if [ -d /usr/pkg/share ]; then
        pathappend /usr/pkg/share XDG_DATA_DIRS
fi
