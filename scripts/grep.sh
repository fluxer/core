#!/bin/sh

find -name SRCBUILD -exec grep -H "$@" {} +
