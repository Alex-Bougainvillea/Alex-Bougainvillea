#!/bin/bash
 
if [ $# -ne 2]; then
    echo "Использование: $0 <путь> <расширение>"
    exit 1
fi
 
direct="$1"
exten="$2"
arc_name="archive_$exten.tar"
 
find "$direct" -type f -name "*.$exten" -print0 | tar --null -cvf "$arc_name" ->
 
echo "Архив $arc_name создан."
