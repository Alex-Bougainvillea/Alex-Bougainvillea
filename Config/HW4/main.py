import argparse
import struct
import xml.etree.ElementTree as ET


def assemble(input_file, binary_output, log_output):
    """Ассемблер: преобразует текстовый код в бинарный и логирует процесс в XML."""
    commands = {
        "LOAD_CONST": 0x00,
        "LOAD_MEM": 0x4F,
        "STORE_MEM": 0x66,
        "NOT": 0x04,
    }

    binary_data = bytearray()
    root = ET.Element("log")

    with open(input_file, "r") as f:
        for line in f:
            parts = line.strip().split()
            cmd = parts[0]
            a = commands[cmd]
            b = int(parts[1])

            if cmd == "STORE_MEM":
                # Для STORE_MEM записываем 1 байт команды + 4 байта адреса
                binary_data.extend(struct.pack("<BIB", a, b, 0))  # 1 byte for command, 4 bytes for address
                binary_data = binary_data[:-1]
                instruction_bytes = binary_data[-5:]  # последние 5 байтов (1 для команды и 4 для адреса)
            elif cmd == "NOT":
                # Для NOT добавляем дополнительные 2 байта (00 00) для достижения 5 байтов в логе
                binary_data.extend(struct.pack("<BH", a, b))  # 1 byte for command, 2 bytes for operand
                binary_data.extend(b'\x00\x00')  # Добавляем два дополнительных байта
                instruction_bytes = binary_data[-5:]  # последние 5 байтов (1 для команды, 2 для операнда и 2 для заполнения)
            else:
                # Для остальных команд
                binary_data.extend(struct.pack("<BH", a, b))  # для LOAD_CONST и LOAD_MEM
                instruction_bytes = binary_data[-3:]  # последние 3 байта

            # Добавление инструкции в XML лог
            instruction = ET.SubElement(root, "instruction")
            instruction.set("command", cmd)
            instruction.set("binary", " ".join(f"{byte:02X}" for byte in instruction_bytes))

    with open(binary_output, "wb") as f:
        f.write(binary_data)

    tree = ET.ElementTree(root)
    tree.write(log_output)
    print(f"Assembly complete. Binary saved to {binary_output}, log saved to {log_output}.")


import struct
import xml.etree.ElementTree as ET

def interpret(binary_file, memory_range, result_file):
    """Интерпретатор: выполняет бинарный код и сохраняет память в XML."""
    with open(binary_file, "rb") as f:
        binary_data = f.read()

    memory = [0] * 2048  # Массив памяти размером 2048 ячеек
    stack = []
    pc = 0  # Program counter

    while pc < len(binary_data):
        cmd = binary_data[pc]
        pc += 1

        if cmd == 0x00:  # LOAD_CONST
            b = struct.unpack("<H", binary_data[pc:pc + 2])[0]
            pc += 2
            stack.append(b)
        elif cmd == 0x4F:  # LOAD_MEM
            if len(stack) > 0:  # Проверяем, что в стеке есть хотя бы один элемент
                b = struct.unpack("<H", binary_data[pc:pc + 2])[0]
                pc += 2
                addr = stack.pop() + b
                # Проверяем, что адрес находится в пределах памяти (0 <= addr < 2048)
                if 0 <= addr < len(memory):
                    stack.append(memory[addr])
                else:
                    print(f"Ошибка: адрес {addr} выходит за пределы памяти.")
                    return  # Прерываем выполнение программы, если адрес выходит за пределы
            else:
                print("Ошибка: стек пуст, не удается выполнить LOAD_MEM.")
                return  # Прерываем выполнение программы, если стек пуст
        elif cmd == 0x66:  # STORE_MEM
            b = struct.unpack("<I", binary_data[pc:pc + 4])[0]
            pc += 4
            if stack:  # Проверяем, что в стеке есть значение для сохранения
                memory[b] = stack.pop()
            else:
                print("Ошибка: стек пуст, не удается выполнить STORE_MEM.")
                return  # Прерываем выполнение программы, если стек пуст
        elif cmd == 0x04:  # NOT
            if not stack:
                stack.append(0)
            stack.append(~stack.pop() & 0xFFFF)  # Выполняем операцию NOT
            break

    # Записываем память в XML
    start, end = memory_range
    root = ET.Element("memory")
    for i in range(start, end):
        mem_cell = ET.SubElement(root, "cell", address=str(i))
        mem_cell.text = str(memory[i])

    tree = ET.ElementTree(root)
    tree.write(result_file)
    print(f"Interpretation complete. Memory saved to {result_file}.")



def main():
    parser = argparse.ArgumentParser(description="Учебная виртуальная машина (УВМ)")
    subparsers = parser.add_subparsers(dest="mode", required=True, help="Режим работы")

    # Ассемблер
    asm_parser = subparsers.add_parser("assemble", help="Ассемблировать текстовую программу")
    asm_parser.add_argument("input_file", type=str, help="Файл с текстовой программой")
    asm_parser.add_argument("binary_output", type=str, help="Файл для сохранения бинарного кода")
    asm_parser.add_argument("log_output", type=str, help="Файл для сохранения XML-лога")

    # Интерпретатор
    int_parser = subparsers.add_parser("interpret", help="Интерпретировать бинарный код")
    int_parser.add_argument("binary_file", type=str, help="Бинарный файл с кодом")
    int_parser.add_argument("start", type=int, help="Начальный адрес диапазона памяти")
    int_parser.add_argument("end", type=int, help="Конечный адрес диапазона памяти")
    int_parser.add_argument("result_file", type=str, help="Файл для сохранения результата")

    args = parser.parse_args()

    if args.mode == "assemble":
        assemble(args.input_file, args.binary_output, args.log_output)
    elif args.mode == "interpret":
        interpret(args.binary_file, (args.start, args.end), args.result_file)


if __name__ == "__main__":
    main()
