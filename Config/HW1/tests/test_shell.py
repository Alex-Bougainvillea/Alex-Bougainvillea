import unittest
from shell_emulator import ShellEmulator

class TestShellEmulator(unittest.TestCase):
    def setUp(self):
        self.emulator = ShellEmulator("vfs")

    def test_ls(self):
        self.assertIn("file1.txt", self.emulator.run_command("ls"))

    def test_cd(self):
        self.assertEqual(self.emulator.run_command("cd subdir"), "")
        self.assertEqual(self.emulator.cwd, "vfs/subdir")

    def test_exit(self):
        self.assertEqual(self.emulator.run_command("exit"), "Exiting shell...")

    def test_cp(self):
        self.assertEqual(self.emulator.run_command("cp testfile.txt copy.txt"), "File copied")

    def test_who(self):
        self.assertEqual(self.emulator.run_command("who"), f"Current user: {self.emulator.username}")

    def test_chmod(self):
        self.assertEqual(self.emulator.run_command("chmod 777 file1.txt"), "Permissions changed")

if __name__ == "__main__":
    unittest.main()
