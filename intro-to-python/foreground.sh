#!/bin/bash

{
echo -n "Initializing environment..."

until [ -e /tmp/ready.txt ]
do
    echo -n "..."
    sleep 3
done

echo "Ready!"
cd /root/notebooks
} 2>/dev/null