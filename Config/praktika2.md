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
