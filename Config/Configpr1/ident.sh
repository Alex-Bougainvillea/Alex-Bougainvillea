#!/bin/bash
if [ $# -ne 1 ]; then
    echo "Использование: $0 <файл>"
    exit 1
fi
 
file="$1"
 
if [ ! -f "$file" ]; then
    echo "Файл не найден: $file"
    exit 1
fi
 
grep -o -E '\b[a-zA-Z_][a-zA-Z0-9_]*\b' "$file" | sort -u
