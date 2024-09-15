# Практическое задание 1. Введение, основы работы в командной строке

А. В. Кузнецов ИКБО-62-23

## Задача 1

```
grep '.*' /etc/passwd | cut -d: -f1 | sort
```

![image](https://github.com/user-attachments/assets/16b692a4-213d-4c70-98cf-76a430df3d0a)

## Задание 2

```
awk '{print $2, $1}' /etc/protocols | sort -nr | head -n 5
```

![image](https://github.com/user-attachments/assets/3ee87b19-dc62-4c05-8c59-4c6e52831fc7)

## Задание 2

```
#!/bin/bash
text=$*
length=${#text}
for i in $(seq 1 $((length + 2))); do
     line+="-"
done
echo "+${line}+"
echo "| ${text} |"
echo "+${line}+"
```

![image](https://github.com/user-attachments/assets/a86714b9-0a9e-42ad-8ad2-7a6a75dd9ea4)
