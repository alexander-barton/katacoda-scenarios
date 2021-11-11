#!/bin/bash

sleep 5
echo "done" | tee /root/apt-update

echo "Installing packages..."

/usr/local/bin/deploy.sh

echo "done" | tee /root/ready
