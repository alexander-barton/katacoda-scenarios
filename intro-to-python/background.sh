#!/bin/bash

#Create the project and venv dir

mkdir -p /home/projects/intro
mkdir -p /home/venvs

cd /home

export HOME=/home

#unlink python
unlink /usr/bin/python

#Relink with 3.8

ln -s /usr/bin/python3.6 /usr/bin/python