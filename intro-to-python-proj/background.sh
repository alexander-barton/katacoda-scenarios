#!/bin/bash

#apt-get -y update
sleep 5
echo "done" >> /root/apt-update

#apt-get -y install python3-venv python3-pip python3-setuptools
#apt-get -y install python3.8-dev python3.8-venv python3.8-distutils
sleep 7
echo "done" >> /root/apt-install

#unlink /usr/bin/python
#ln -s /usr/bin/python3.8 /usr/bin/python
sleep 10
echo "done" >> /root/tutorial/linking
