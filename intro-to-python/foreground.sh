#!/bin/bash

{
echo -n "Initializing environment..."
unti [ -e /tmp/ready.txt ]
do
echo -n "..."
sleep 3
done
echo "Ready!"
cd /root/notebook
} 2>/dev/null