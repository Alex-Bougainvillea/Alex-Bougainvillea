import subprocess

def get_git_objects():
    result = subprocess.run(['git', 'rev-list', '--objects', '--all'], capture_output=True, text=True)
    objects = result.stdout.splitlines()
    return [obj.split()[0] for obj in objects if obj]

def show_object_content(obj_hash):
    result = subprocess.run(['git', 'cat-file', '-p', obj_hash], capture_output=True, text=True)
    return result.stdout

def main():
    try:
        subprocess.run(['git', 'rev-parse', '--is-inside-work-tree'], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print("This is not a Git repository.")
        return

    objects = get_git_objects()
    for obj_hash in objects:
        print(f"Object: {obj_hash}")
        print(show_object_content(obj_hash))
        print("=" * 40)  # Разделитель между объектами

if __name__ == "__main__":
    main()
