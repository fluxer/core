#!/bin/sh
set -e
for size in 640x400 800x600 1024x768;do
    convert -resize "$size" "$@" "$size.ppm"
done
