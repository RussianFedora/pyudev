#!/bin/sh

PYUDEV_VERSION=0.12
GIT_DATE=20110715

PYUDEV_NAME=pyudev-${PYUDEV_VERSION}.git${GIT_DATE}

git clone git://github.com/lunaryorn/pyudev.git > /dev/null
cd pyudev
rm -rf .git
cd ..
mv pyudev $PYUDEV_NAME
tar cfjv $PYUDEV_NAME.tar.bz2 $PYUDEV_NAME > /dev/null
