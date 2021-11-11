#!/bin/bash

{
echo -n "Initializing environment..."

until [ -e ready.txt ]
do
    echo -n "..."
    sleep 3
done

echo "Ready!"

} 2>/dev/null

rm ready