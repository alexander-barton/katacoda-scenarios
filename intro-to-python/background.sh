#!/bin/bash

#Create the project and venv dir

mkdir -p /home/projects/intro
mkdir -p /home/venvs

sudo apt install python3.8

#unlink python
unlink /usr/bin/python

#Relink with 3.8

ln -s /usr/bin/python3.8 /usr/bin/python