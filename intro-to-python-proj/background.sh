#!/bin/bash

apt-get -y update
echo "done" >> /root/apt-update

apt-get -y install python3-venv
apt-get -y install python3.8-dev python3.8-venv
echo "done" >> /root/apt-install

unlink /usr/bin/python
ln -s /usr/bin/python3.8 /usr/bin/python
echo "done" >> /root/linking

rm /root/linking
rm /root/apt-install
rm /root/apt-update