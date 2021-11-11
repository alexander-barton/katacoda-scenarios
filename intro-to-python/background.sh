#!/bin/bash

# Create the password for the jupyter notebook

export PASSWORD=learning!

# Start jupyter notebook
jupyter notebook --allow-root

# Make file for foreground script
touch /tmp/ready.txt