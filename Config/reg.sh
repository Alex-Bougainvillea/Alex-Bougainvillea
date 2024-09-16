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
