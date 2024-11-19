import sys
import yaml
import argparse
from typing import Any

# Постфиксные операции
OPERATIONS = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "mod": lambda x, y: x % y
}


def parse_postfix(expression: list):
    """Вычисляет постфиксное выражение."""
    stack = []
    for token in expression:
        if isinstance(token, (int, float)):
            stack.append(token)
        elif isinstance(token, str) and token.replace('.', '', 1).isdigit():
            stack.append(float(token) if '.' in token else int(token))
        elif token in OPERATIONS:
            if len(stack) < 2:
                raise ValueError(f"Недостаточно аргументов для операции '{token}'")
            b = stack.pop()
            a = stack.pop()
            stack.append(OPERATIONS[token](a, b))
        else:
            raise ValueError(f"Неизвестный токен '{token}'")
    if len(stack) != 1:
        raise ValueError("Некорректное постфиксное выражение")
    return stack[0]


def yaml_to_config(data: Any) -> str:
    """Преобразует YAML в текст на учебном конфигурационном языке."""
    if isinstance(data, dict):
        result = []
        # Обрабатываем константы на одной строке
        constants = []
        for key, value in data.items():
            if isinstance(value, (int, float)):
                constants.append(f"{key} = {value}")
            elif isinstance(value, list) and all(isinstance(item, (int, float, str)) for item in value):
                try:
                    # Преобразуем постфиксные выражения в их результат
                    result_value = parse_postfix(value)
                    result.append(f"var {key} = {result_value};")
                except ValueError:
                    # Если это не постфиксное выражение, форматируем как массив
                    result.append(f"var {key} = {yaml_to_config(value)};")
            else:
                result.append(f"var {key} = {yaml_to_config(value)};")

        # Формируем строку для констант в одной строке
        if constants:
            result.append(f"constants = {' '.join(constants)};")

        return "\n".join(result)

    elif isinstance(data, list):
        # Обрабатываем массивы
        return f"(list {' '.join(map(yaml_to_config, data))})"

    elif isinstance(data, str):
        if "\n" in data:
            # Многострочный комментарий
            return f"/#\n{data}\n#/"
        else:
            # Простая строка
            return f"[[{data}]]"

    elif isinstance(data, (int, float)):
        return str(data)
    else:
        raise ValueError(f"Некорректный тип данных: {type(data)}")


def main():
    # Парсер аргументов командной строки
    parser = argparse.ArgumentParser(description="Преобразование YAML в учебный конфигурационный язык.")
    parser.add_argument("output", help="Путь к выходному файлу.")
    args = parser.parse_args()

    # Примеры в input_data
    input_data = """
    constants:
      a: 10
      b: 25
      c: 7
    expression_1: [10, 25, "+"]
    expression_2: [25, 7, "mod"]
    nested_expression:
      - [10, 25, "+"]
      - [35, 7, "-"]
      - [28, 5, "mod"]
    comment: |
      Сегодня пасмурно
      пойдет дождь
    array_example:
      - белый
      - синий
      - зеленый
    string_example: "Просто строка"
    """
    try:
        yaml_data = yaml.safe_load(input_data)
    except yaml.YAMLError as e:
        print(f"Ошибка синтаксиса YAML: {e}", file=sys.stderr)
        sys.exit(1)

    # Преобразование в учебный язык
    try:
        config_text = yaml_to_config(yaml_data)
    except ValueError as e:
        print(f"Ошибка преобразования: {e}", file=sys.stderr)
        sys.exit(1)

    # Запись в файл
    with open(args.output, "w") as f:
        f.write(config_text)
    print(f"Конфигурация успешно сохранена в {args.output}")


if __name__ == "__main__":
    main()
