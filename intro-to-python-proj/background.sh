#!/bin/bash

apt-get -y update
echo "done" >> /home/scrapbook/tutorial/apt-update

apt-get -y install python3-venv python3-pip python3-setuptools
apt-get -y install python3.8-dev python3.8-venv python3.8-distutils
echo "done" >> /home/scrapbook/tutorial/apt-install

unlink /usr/bin/python
ln -s /usr/bin/python3.8 /usr/bin/python
echo "done" >> /home/scrapbook/tutorial/linking
