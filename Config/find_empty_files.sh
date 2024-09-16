#!/bin/bash
 
if [ $# -ne 1]; then
    echo "Использование: $0 <путь>"
    exit 1
fi
 
directory="$1"
 
find "$directory" -type f -empty -exec file {} \; | grep "empty" | cut -d: -f1
