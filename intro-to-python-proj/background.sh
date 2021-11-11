#!/bin/bash

apt-get -y update
echo "done" >> ~/apt-update

apt-get -y install python3-venv python3-pip python3-setuptools
apt-get -y install python3.8-dev python3.8-venv
echo "done" >> ~/apt-install

unlink /usr/bin/python
ln -s /usr/bin/python3.8 /usr/bin/python
echo "done" >> ~/linking
