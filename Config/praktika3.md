# Практическое занятие 3. Конфигурационные языки

А. В. Кузнецов ИКБО-62-23

## Задача 1

```
local group_count = 24;
local group_name = "ИКБО-%d-20";

{
  groups: [std.format(group_name, i) for i in std.range(1, group_count)],
  students: [
    {
      age: 19,
      group: "ИКБО-4-20",
      name: "Иванов И.И."
    },
    {
      age: 18,
      group: "ИКБО-5-20",
      name: "Петров П.П."
    },
    {
      age: 18,
      group: "ИКБО-5-20",
      name: "Сидоров С.С."
    },
    {
      age: 20,
      group: "ИКБО-6-20",
      name: "Кузнецов К.К."
    }
  ],
  subject: "Конфигурационное управление"
}
```

![image](https://github.com/user-attachments/assets/05e28a01-df59-443a-a8db-5c14d5ae8ddd)

## Задача 2

```
let Prelude = https://prelude.dhall-lang.org/v20.1.0/package.dhall

let Group = Text

let Student =
      { age : Natural, group : Group, name : Text }

let groupCount = 24

let groupName : Natural -> Group = λ(i : Natural) → "ИКБО-${Prelude.Natural.show i}-20"

let groups : List Group = Prelude.List.generate groupCount Text groupName

let students : List Student =
      [ { age = 19, group = "ИКБО-4-20", name = "Иванов И.И." }
      , { age = 18, group = "ИКБО-5-20", name = "Петров П.П." }
      , { age = 18, group = "ИКБО-5-20", name = "Сидоров С.С." }
      , { age = 20, group = "ИКБО-6-20", name = "Кузнецов К.К." }
      ]

let subject = "Конфигурационное управление"

in { groups = groups, students = students, subject = subject }
```

## Задача 3

```
import random

def parse_bnf(text):
    '''
    Преобразовать текстовую запись БНФ в словарь.
    '''
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar

def generate_phrase(grammar, start):
    '''
    Сгенерировать случайную фразу.
    '''
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)

BNF = '''
S = B | C | D | E | F
B = 1 0
C = 1 0 0
D = 1 1
E = 1 0 1 1 0 1
F = 0 0 0
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'S'))
```

![image](https://github.com/user-attachments/assets/f6e5f95b-0e16-48e9-ad47-8b1d83453f3e)

## Задача 4

```
import random

def parse_bnf(text):
    '''
    Преобразовать текстовую запись БНФ в словарь.
    '''
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar

def generate_phrase(grammar, start):
    '''
    Сгенерировать случайную фразу.
    '''
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)

BNF = '''
S = B | C | D | E | F
B = (({((()))}))
C = {}
D = {()}
E = ()
F = {}
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'S'))
```

![image](https://github.com/user-attachments/assets/918ebefe-404f-4718-abf4-fabf0f607af5)

## Задача 5 

```
import random

def parse_bnf(text):
    '''
    Преобразовать текстовую запись БНФ в словарь.
    '''
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar

def generate_phrase(grammar, start):
    '''
    Сгенерировать случайную фразу.
    '''
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)

BNF = '''
S = B | C | D | E | F
B = ((~(y & x)) | (y) & ~x | ~x) & x
C = y & ~(y)
D = (~(y) & y & ~y)
E = ~x
F = ~((x) & y | (y) | (x)) & x | x | (y & ~y)
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'S'))
```

![image](https://github.com/user-attachments/assets/43452aa5-b942-4728-af41-2bf5c4f76952)
