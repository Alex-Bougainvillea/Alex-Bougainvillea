# Практическое задание 1. Введение, основы работы в командной строке

А. В. Кузнецов ИКБО-62-23

## Задание 1

```
grep '.*' /etc/passwd | cut -d: -f1 | sort
```

![image](https://github.com/user-attachments/assets/16b692a4-213d-4c70-98cf-76a430df3d0a)

## Задание 2

```
awk '{print $2, $1}' /etc/protocols | sort -nr | head -n 5
```

![image](https://github.com/user-attachments/assets/3ee87b19-dc62-4c05-8c59-4c6e52831fc7)

## Задание 3

```
nano banner.sh

#!/bin/bash
text=$*
length=${#text}
for i in $(seq 1 $((length + 2))); do
     line+="-"
done
echo "+${line}+"
echo "| ${text} |"
echo "+${line}+"

chmod +x banner.sh
./banner.sh Hello from RTU MIREA!
```

![image](https://github.com/user-attachments/assets/a86714b9-0a9e-42ad-8ad2-7a6a75dd9ea4)

## Задание 4

```
nano ident.sh

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

chmod +x ident.sh
./ident.sh hello.c
```

![image](https://github.com/user-attachments/assets/7d27bfed-5dc9-4e5f-bd35-6c6a77ee5862)

## Задание 5

```
nano reg

#!/bin/bash
 
if [ $# -ne 1 ]; then
    echo "Использование: $0 <файл>"
    exit 1
fi
 
Comm=$1
 
if [ ! -f "$Comm" ]; then
    echo "Ошибка: файл '$Comm' не существует."
    exit 1
fi
 
sudo cp "$Comm" /usr/local/bin/
 
sudo chmod 755 /usr/local/bin/"$Comm"
 
echo "Команда '$Comm' успешно установлена с правами"

chmod +x reg
./reg banner.txt
```

![image](https://github.com/user-attachments/assets/59da4b57-a3a3-4093-b61b-41442582a2e4)

## Задание 6

```
nano cheker.sh

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

chmod +x cheker.sh
./cheker.sh
```

![image](https://github.com/user-attachments/assets/3b3d119f-ec70-4916-9997-2fb31f26f881)

## Задание 7

```
nano f_duplic.sh

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

chmod +x f_duplic.sh
./f_duplic.sh <путь_к_каталогу_подкаталогу>
```

![image](https://github.com/user-attachments/assets/11aee96f-9ec8-4ebc-8a0b-bcf684b65c5e)

## Задание 8

```
nano archive_files.sh

#!/bin/bash

if [ $# -ne 2 ]; then
  echo "Использование: $0 <путь> <расширение>"
  exit 1
fi

direct="$1"
exten="$2"
archive_name="archive_$extension.tar"

find "$direct" -type f -name "*.$exten" -print0 | tar --null -cvf "$archive_name" --files-from -

echo "Архив $archive_name создан."
```

## Задание 9
