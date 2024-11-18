import os
import subprocess
import argparse


def get_git_commit_data(repo_path):
    """Собирает данные о коммитах и изменениях в файлах."""
    os.chdir(repo_path)
    # Получение списка коммитов с их хэшами
    log_output = subprocess.check_output(['git', 'log', '--pretty=format:%H'], text=True).strip().split('\n')

    commit_data = {}
    for commit_hash in log_output:
        # Получение изменённых файлов для каждого коммита
        files = subprocess.check_output(['git', 'show', '--name-only', '--pretty=format:', commit_hash],
                                        text=True).strip().split('\n')
        commit_data[commit_hash] = files
    return commit_data


def build_dependency_graph(commit_data):
    """Формирует граф зависимостей на основе данных о коммитах."""
    graph = []
    for commit, files in commit_data.items():
        for file in files:
            graph.append(f'"{commit}" --> "{file}"')
    return graph


def generate_plantuml_code(graph):
    """Генерирует код PlantUML для графа."""
    plantuml_code = ["@startuml"]
    plantuml_code.extend(graph)
    plantuml_code.append("@enduml")
    return '\n'.join(plantuml_code)


def save_to_file(content, file_path):
    """Сохраняет содержимое в файл."""
    with open(file_path, 'w') as file:
        file.write(content)


def visualize_graph(plantuml_tool_path, file_path):
    """Открывает граф с помощью указанного инструмента визуализации."""
    subprocess.run([plantuml_tool_path, file_path])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Визуализатор графов зависимостей для git-репозитория.")
    parser.add_argument("--plantuml_tool", required=True, help="Путь к программе для визуализации графов.")
    parser.add_argument("--repo_path", required=True, help="Путь к анализируемому репозиторию.")
    parser.add_argument("--output_path", required=True, help="Путь к файлу-результату в виде кода.")
    args = parser.parse_args()

    # Основной процесс
    commit_data = get_git_commit_data(args.repo_path)
    graph = build_dependency_graph(commit_data)
    plantuml_code = generate_plantuml_code(graph)
    save_to_file(plantuml_code, args.output_path)
    visualize_graph(args.plantuml_tool, args.output_path)
