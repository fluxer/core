#!/bin/sh

if [ "$EUID" -ne "0" ];then
    export PATH="/usr/lib/ccache/bin/:$PATH"
fi
