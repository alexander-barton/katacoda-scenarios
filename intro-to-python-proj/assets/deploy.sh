#!/bin/bash
cd /root
sleep 5

apt-get -y update

apt-get -y install python3-venv python3-pip python3-setuptools
apt-get -y install python3.8-dev python3.8-venv python3.8-distutils

unlink /usr/bin/python
ln -s /usr/bin/python3.8 /usr/bin/python