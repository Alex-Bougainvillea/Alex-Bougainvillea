import os
import shutil
import getpass
import stat

class ShellEmulator:
    def __init__(self, vfs_path):
        self.cwd = vfs_path
        self.username = getpass.getuser()
        self.base_dir = os.path.abspath(vfs_path)
        self.cwd = self.base_dir

    def run_command(self, command):
        parts = command.split()
        cmd = parts[0]
        args = parts[1:]

        if cmd == "ls":
            return self.ls(args)
        elif cmd == "cd":
            return self.cd(args[0] if args else "")
        elif cmd == "exit":
            return self.exit()
        elif cmd == "cp":
            return self.cp(args[0], args[1])
        elif cmd == "who":
            return self.who()
        elif cmd == "chmod":
            return self.chmod(args[0], args[1])
        else:
            return "Command not found"

    def ls(self, args):
        detailed = "-l" in args
        entries = os.listdir(self.cwd)
        if detailed:
            result = []
            for entry in entries:
                full_path = os.path.join(self.cwd, entry)
                permissions = stat.filemode(os.stat(full_path).st_mode)
                size = os.path.getsize(full_path)
                result.append(f"{permissions} {size} {entry}")
            return "\n".join(result)
        else:
            return "\n".join(entries)

    def cd(self, path):
        if not path:
            path = self.base_dir

        new_path = os.path.abspath(os.path.join(self.cwd, path))
        if not new_path.startswith(self.base_dir):
            return "Error: out of range directory"

        if os.path.isdir(new_path):
            self.cwd = new_path
            return ""
        else:
            return f"No such directory: {path}"

    def exit(self):
        return ""

    def cp(self, src, dst):
        try:
            shutil.copy(src, dst)
            return "File copied"
        except Exception as e:
            return str(e)

    def who(self):
        return f"Current user: {self.username}"

    def chmod(self, mode, file):
        try:
            file_path = os.path.join(self.cwd, file)
            os.chmod(file_path, int(mode, 8))
            return "Permissions changed"
        except Exception as e:
            return str(e)
