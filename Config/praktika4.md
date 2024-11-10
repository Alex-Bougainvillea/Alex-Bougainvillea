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

## Задача 3

```
$ git init --bare ../server.git

$ git remote add server ../server.git
$ git remote -v
origin  ../server.git (fetch)
origin  ../server.git (push)

$ git push server master

$ git clone ../server.git Coder2_repo
$ cd Coder2_repo
$ git config user.name "Coder2"
$ git config user.email "coder2@corp.com"

$ echo "This is a simple Python program." > readme.md
$ git add readme.md
$ git commit -m "Add readme.md with program description"
$ git push server master

$ cd ../Coder1_repo
$ git pull server master

$ echo -e "\n## Authors\n- Coder1" >> readme.md
$ git add readme.md
$ git commit -m "Add coder1 info to authors section"
$ git push server master

$ cd ../Coder2_repo
$ git pull server master
$ git add readme.md
$ git commit -m "Resolve conflict and add coder2 info to authors section"
$ git push server master

$ cd ../Coder1_repo
$ git pull server master
```

Лог коммитов

```
*   commit a457d748f0dab75b4c642e964172887de3ef4e3e
|\  Merge: 48ce283 d731ba8
| | Author: Coder2 <coder2@corp.com>
| | Date:   Sun Nov 10 16:57:45 2024
| | 
| |     Resolve conflict and add coder2 info to authors section
| | 
| * commit d731ba84014d603384cc3287a8ea9062dbb92303
| | Author: Coder1 <coder1@corp.com>
| | Date:   Sun Nov 10 16:57:45 2024
| | 
| |     Add coder1 info to authors section
| | 
* | commit 48ce28336e6b3b983cbd6323500af8ec598626f1
|/  Author: Coder2 <coder2@corp.com>
|   Date:   Sun Nov 10 16:57:46 2024
|   
|       Add readme.md with program description
| 
* commit ba9dfe9cb24316694808a347e8c36f8383d81bbe
| Author: Coder1 <coder1@corp.com>
| Date:   Sun Nov 10 16:57:46 2024
| 
|     first commit
```
