## Практическое задание 2

А. В. Кузнецов ИКБО-62-23

# Задание 1

```
pip show matplotlib
```
![image](https://github.com/user-attachments/assets/6626a986-dfae-49a8-b229-30d9aeef9131)
![image](https://github.com/user-attachments/assets/3bfc6c54-acdc-483f-a34b-648abaac8098)
```
pipdeptree --packages matplotlib
```
![image](https://github.com/user-attachments/assets/9e0b0e10-b66a-4935-ba25-47d4969b1bab)

# Задание 2

```
nmp install express
```

```
nmp view express
```

```
npm ls --depth=[depth]
```

# Задание 3

```
digraph {
    matplotlib [label=matplotlib]
    pyparsing [label=pyparsing]
    matplotlib -> pyparsing
    cycler [label=cycler]
    matplotlib -> cycler
    numpy [label=numpy]
    matplotlib -> numpy
    kiwisolver [label=kiwisolver]
    matplotlib -> kiwisolver
    pillow [label=pillow]
    matplotlib -> pillow
    "python-dateutil" [label="python-dateutil"]
    matplotlib -> "python-dateutil"
    express [label="plotly express"]
    plotly [label=plotly]
    express -> plotly
    pandas [label=pandas]
    express -> pandas
    numpy [label=numpy]
    express -> numpy
    matplotlib -> numpy
    express -> numpy
}
```
![image](https://github.com/user-attachments/assets/acf98db3-821f-4cff-aa25-3c8e97b97053)

# Задание 4

```
include "alldifferent.mzn";  

array[1..6] of var 0..9: digits;  
constraint
    digits[1] + digits[2] + digits[3] = digits[4] + digits[5] + digits[6];
constraint
    all_different(digits);
var int: sum_of_three = digits[1] + digits[2] + digits[3];
solve minimize sum_of_three;
```

![image](https://github.com/user-attachments/assets/9bb4a668-6e82-42c5-a4a3-6d3287f10cec)

# Задание 5

```
array[1..6] of int: menu_versions = [100, 110, 120, 130, 140, 150];       
array[1..5] of int: dropdown_versions = [180, 200, 210, 220, 230];
array[1..2] of int: icons_versions = [100, 200];            

var 1..6: menu_version;      
var 1..5: dropdown_version;   
var 1..2: icons_version;      

constraint menu_version >= 1 /\ menu_version <= 6;
constraint icons_version >= 1 /\ icons_version <= 2;

constraint dropdown_version >= 1 /\ dropdown_version <= 5;

constraint menu_version >= dropdown_version; 

array[1..3] of var int: versions = [menu_version, dropdown_version, icons_version];

solve minimize max(versions);
```
![image](https://github.com/user-attachments/assets/50a59a7c-3588-4256-96d6-576bc73229ce)

# Задание 6

```
var 0..2: root_version;   
var 0..2: foo_version;     
var 0..2: left_version;    
var 0..2: right_version;   
var 0..2: shared_version;  
var 0..2: target_version;   

% root 1.0.0 зависит от foo ^1.0.0 и target ^2.0.0
constraint root_version = 1 /\ foo_version >= 1 /\ target_version >= 2;
% foo 1.1.0 зависит от left ^1.0.0 и right ^1.0.0
constraint foo_version = 1 -> (left_version >= 1 /\ right_version >= 1);
% foo 1.0.0 не имеет зависимостей
constraint foo_version = 0 -> (left_version = 0 /\ right_version = 0);
% left 1.0.0 зависит от shared >= 1.0.0
constraint left_version = 1 -> (shared_version >= 1);
% right 1.0.0 зависит от shared < 2.0.0
constraint right_version = 1 -> (shared_version < 2);
% shared 2.0.0 не имеет зависимостей
constraint shared_version = 2 -> (target_version = 0 \/ target_version = 1 \/ target_version = 2);
% shared 1.0.0 зависит от target ^1.0.0
constraint shared_version = 1 -> (target_version >= 1);

constraint target_version >= 1 /\ target_version <= 2;

solve satisfy;
```
![image](https://github.com/user-attachments/assets/5ff137a6-0ee9-41e0-98cb-cbfa59f86507)

# Задание 7

```
packages = {
    "root": {
        "version": "1.0.0",
        "dependencies": {
            "foo": "^1.0.0",
            "target": "^2.0.0"
        }
    },
    "foo": {
        "version": "1.1.0",
        "dependencies": {
            "left": "^1.0.0",
            "right": "^1.0.0"
        }
    },
    "left": {
        "version": "1.0.0",
        "dependencies": {
            "shared": ">=1.0.0"
        }
    },
    "right": {
        "version": "1.0.0",
        "dependencies": {
            "shared": "<2.0.0"
        }
    },
    "shared": {
        "version": "2.0.0",
        "dependencies": {}
    },
    "target": {
        "version": "2.0.0",
        "dependencies": {}
    }
}
def build_constraints(packages):
    constraints = []
    for package, info in packages.items():
        version_constraint = f"{package}_version = {info['version']}"
        constraints.append(version_constraint)

        for dependency, version_spec in info['dependencies'].items():
            if version_spec.startswith("^"):
                constraints.append(f"{dependency}_version >= {version_spec[1:]}")
            elif version_spec.startswith(">="):
                constraints.append(f"{dependency}_version >= {version_spec[2:]}")
            elif version_spec.startswith("<"):
                constraints.append(f"{dependency}_version < {version_spec[1:]}")

    return constraints
constraints = build_constraints(packages)

for constraint in constraints:
    print(constraint)
```
![image](https://github.com/user-attachments/assets/1079ca83-4906-4bb0-9512-8c263c320b76)
