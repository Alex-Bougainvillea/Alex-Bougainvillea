#!/bin/bash

if [ -z "$1" ]; then
  echo "Использование: $0 <путь>"
  exit 1
fi

search_f="$1"

find "$search_f" -type f -exec sha256sum {} + | sort | awk '{
  hash=$1;
  file=$2;
  files[hash] = (files[hash] ? files[hash] ORS file : file);
} 
END {
  for (hash in files) {
    split(files[hash], arr, ORS);
    if (length(arr) > 1) {
      print "Дубликаты для хеша " hash ":";
      for (i in arr) {
        print " " arr[i];
      }
      print "";
    }
  }
}'
