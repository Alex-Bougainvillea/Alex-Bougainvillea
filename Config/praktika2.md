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

```
