#!/bin/bash
 
for file in *.c *.js *.py; do
    if [[ -f "$file" ]]; then
        f_line=$(head -n 1 "$file")
        if [[ "$file" == *.c || "$file" == *.js ]]; then
            if [[ "$f_line" =~ ^[[:space:]]*// ]]; then
                echo "Файл $file содержит комментарий в первой строке."
            else
                echo "Файл $file не содержит комментарий в первой строке."
            fi
        elif [[ "$file" == *.py ]]; then
            if [[ "$f_line" =~ ^[[:space:]]*# ]]; then
                echo "Файл $file содержит комментарий в первой строке."
            else
                echo "Файл $file не содержит комментарий в первой строке."
            fi
        fi
    fi
done
