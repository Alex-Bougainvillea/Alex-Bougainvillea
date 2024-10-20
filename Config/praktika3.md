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
