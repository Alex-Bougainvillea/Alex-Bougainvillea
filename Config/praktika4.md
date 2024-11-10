# Практическое задание 4. Системы контроля версий

А. В. Кузнецов ИКБО-62-23

## Задача 1

![image](https://github.com/user-attachments/assets/c3816eb8-ecca-4650-92f3-a5d7b49821b5)

## Задача 2

```
$ git init
Initialized empty Git repository in /path/to/repository/.git/

$ git config user.name "Coder1"
$ git config user.email "coder1@corp.com"

$ echo "print('Hello, world!')" > prog.py

$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	prog.py

nothing added to commit but untracked files present (use "git add" to track)

$ git add prog.py

$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   prog.py

$ git commit -m "Add prog.py"
[master (root-commit) 1a2b3c4] Add prog.py with initial data
 1 file changed, 1 insertion(+)
 create mode 100644 prog.py

# Проверяем историю коммитов
$ git log
commit 1a2b3c4d5e6f7g8h9i0j 
Author: Coder1 <coder1@corp.com>
Date:   Sun Nov 10 16:42:11 2024

    Add prog.py
```
