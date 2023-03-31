# Для VSCode
import os
import sys
sys.path.append(os.getcwd())

import unittest
from task_2 import ya_folder, name_folder


class TestCreateFolder(unittest.TestCase):
    def test_folder_creation(self):
        self.assertEqual(
            ya_folder.folder_creation(name_folder),
            201,
            f"Папка {name_folder} уже существует.",
        )


class TestCreateFolder2:
    def test_name_folder(self):
        assert (
            ya_folder.folder_creation(name_folder) != 409
        ), f"Папка {name_folder} уже существует."


if __name__ == "__main__":
    unittest.main()