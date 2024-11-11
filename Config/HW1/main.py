import os
import zipfile
import yaml
import tkinter as tk
from shell_emulator import ShellEmulator

# Чтение конфигурации
with open("C:/Users/A.Kuznecov/AppData/Roaming/JetBrains/PyCharmCE2023.3/scratches/config.yml") as f:
    config = yaml.safe_load(f)

# Распаковка виртуальной файловой системы
with zipfile.ZipFile(config['vfs_path'], 'r') as zip_ref:
    zip_ref.extractall("vfs")

# Инициализация эмулятора
emulator = ShellEmulator("vfs")


# GUI на tkinter
class ShellGUI:
    def __init__(self, root, emulator):
        self.root = root
        self.root.title("shellUnix")

        # Настройка Text виджета для консольного вида
        self.text = tk.Text(root, height=20, width=70, bg="black", fg="white",
                            insertbackground="white", font=("Courier", 12), wrap="word")
        self.text.pack()
        self.text.bind("<Return>", self.execute_command)
        self.text.bind("<BackSpace>", self.prevent_backspace_outside_prompt)

        self.emulator = emulator
        self.current_prompt_index = None  # Индекс для отслеживания позиции начала ввода

        self.run_start_script(config['start_script'])
        self.update_prompt()  # Отображение начального пути

    def prevent_backspace_outside_prompt(self, event):
        # Предотвращает удаление текста до текущего пути
        if self.text.index("insert") <= self.current_prompt_index:
            return "break"

    def update_prompt(self):
        """Добавление строки с текущим каталогом перед вводом команды."""
        # Преобразуем текущий путь относительно base_dir
        relative_path = os.path.relpath(self.emulator.cwd, self.emulator.base_dir)
        if relative_path == ".":
            relative_path = "/"  # Если текущий путь совпадает с base_dir, выводим "/"
        else:
            relative_path = "/" + relative_path.replace("\\", "/")  # Преобразование к Unix-формату

        self.text.config(state=tk.NORMAL)
        self.text.insert(tk.END, f"vfs{relative_path} $ ")
        self.current_prompt_index = self.text.index(tk.INSERT)  # Запоминаем позицию ввода
        self.text.see(tk.END)

    def execute_command(self, event):
        # Получаем команду, введенную после текущего пути и символа `$`
        command_start_index = self.current_prompt_index
        command_end_index = self.text.index("end-1c")
        command = self.text.get(command_start_index, command_end_index).strip()

        # Проверка на пустую команду (только нажатие Enter)
        if not command:
            self.text.insert(tk.END, "\n")  # Переход на новую строку
            self.update_prompt()  # Отображение текущего пути на новой строке
            return "break"

        # Удаление введенной команды и добавление ее вывода
        self.text.config(state=tk.NORMAL)
        output = self.emulator.run_command(command)

        # Проверка команды 'exit'
        if command == "exit":
            self.root.quit()  # Закрытие окна tkinter
        else:
            # Печать результата выполнения команды и обновление строки
            self.text.insert(tk.END, f"\n{output}\n")
            self.update_prompt()  # Отображаем новый путь и символ `$`

        # Предотвращает стандартное поведение "Enter"
        return "break"

    def run_start_script(self, script_path):
        with open(script_path) as f:
            for line in f:
                # Вывод текущего пути перед каждой командой из стартового скрипта
                self.update_prompt()
                output = self.emulator.run_command(line.strip())
                self.text.config(state=tk.NORMAL)
                self.text.insert(tk.END, f"{line.strip()}\n{output}\n")
                self.text.config(state=tk.DISABLED)
                self.text.see(tk.END)

root = tk.Tk()
app = ShellGUI(root, emulator)
root.mainloop()
