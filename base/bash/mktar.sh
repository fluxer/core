#!/bin/sh

set -e

if [ -z "$1" ];then
    echo "Need a depth level argument"
    exit 1
fi
git clone --depth="$1" git://git.sv.gnu.org/bash.git
cd bash
git archive --prefix="bash-4.3.$1/" HEAD | xz > "../bash-4.3.$1.tar.xz"
cd -
rm -rf bash