#!/usr/bin/python3
"""test console"""
import unittest
from unittest.mock import patch
from io import StringIO

from console import HBNBCommand
from models import storage
from models.user import User

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.patcher = patch('sys.stdout', new=StringIO())
        self.mock_stdout = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_create(self):
        with patch('sys.stdin', return_value=StringIO('create User\n')) as f:
            self.console.onecmd("create User")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_show(self):
        with patch('sys.stdin', return_value=StringIO('create User\n')) as f:
            self.console.onecmd("create User")
            created_output = self.mock_stdout.getvalue().strip()
            instance_id = created_output.split()[3][1:-1]

        with patch('sys.stdin', return_value=StringIO(f'show User {instance_id}\n')) as f:
            self.console.onecmd(f"show User {instance_id}")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_destroy(self):
        with patch('sys.stdin', return_value=StringIO('create User\n')) as f:
            self.console.onecmd("create User")
            created_output = self.mock_stdout.getvalue().strip()
            instance_id = created_output.split()[3][1:-1]

        with patch('sys.stdin', return_value=StringIO(f'destroy User {instance_id}\n')) as f:
            self.console.onecmd(f"destroy User {instance_id}")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

        with patch('sys.stdin', return_value=StringIO(f'show User {instance_id}\n')) as f:
            self.console.onecmd(f"show User {instance_id}")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_all(self):
        with patch('sys.stdin', return_value=StringIO('all\n')) as f:
            self.console.onecmd("all")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_all_class(self):
        with patch('sys.stdin', return_value=StringIO('create User\n')) as f:
            self.console.onecmd("create User")
            created_output = self.mock_stdout.getvalue().strip()
            instance_id = created_output.split()[3][1:-1]

        with patch('sys.stdin', return_value=StringIO(f'all User\n')) as f:
            self.console.onecmd(f"all User")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_update(self):
        with patch('sys.stdin', return_value=StringIO('create User\n')) as f:
            self.console.onecmd("create User")
            created_output = self.mock_stdout.getvalue().strip()
            instance_id = created_output.split()[3][1:-1]

        with patch('sys.stdin', return_value=StringIO(f'update User {instance_id} name "John"\n')) as f:
            self.console.onecmd(f"update User {instance_id} name \"John\"")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

        with patch('sys.stdin', return_value=StringIO(f'show User {instance_id}\n')) as f:
            self.console.onecmd(f"show User {instance_id}")
            output = self.mock_stdout.getvalue().strip()
            self.assertIn("John", output)

    def test_count(self):
        with patch('sys.stdin', return_value=StringIO('create User\n')) as f:
            self.console.onecmd("create User")

        with patch('sys.stdin', return_value=StringIO('count User\n')) as f:
            self.console.onecmd("count User")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "1")

    def test_show_error(self):
        with patch('sys.stdin', return_value=StringIO('show User 12345\n')) as f:
            self.console.onecmd("show User 12345")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy_error(self):
        with patch('sys.stdin', return_value=StringIO('destroy User 12345\n')) as f:
            self.console.onecmd("destroy User 12345")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_update_error(self):
        with patch('sys.stdin', return_value=StringIO('update User 12345\n')) as f:
            self.console.onecmd("update User 12345")
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_update_error_attr(self):
        with patch('sys.stdin', return_value=StringIO('update User 12345 name "John"\n')) as f:
            self.console.onecmd('update User 12345 name "John"')
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_update_error_value(self):
        with patch('sys.stdin', return_value=StringIO('create User\n')) as f:
            self.console.onecmd("create User")
            created_output = self.mock_stdout.getvalue().strip()
            instance_id = created_output.split()[3][1:-1]

        with patch('sys.stdin', return_value=StringIO(f'update User {instance_id} name\n')) as f:
            self.console.onecmd(f'update User {instance_id} name')
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "** value missing **")

    def test_update_dict(self):
        with patch('sys.stdin', return_value=StringIO('create User\n')) as f:
            self.console.onecmd("create User")
            created_output = self.mock_stdout.getvalue().strip()
            instance_id = created_output.split()[3][1:-1]

        with patch('sys.stdin', return_value=StringIO(f'update_dict User {instance_id} {{"name": "John", "age": 25}}\n')) as f:
            self.console.onecmd(f'update_dict User {instance_id} {{"name": "John", "age": 25}}')
            output = self.mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

        with patch('sys.stdin', return_value=StringIO(f'show User {instance_id}\n')) as f:
            self.console.onecmd(f'show User {instance_id}')
            output = self.mock_stdout.getvalue().strip()
            self.assertIn("John", output)
            self.assertIn("25", output)

if __name__ == '__main__':
    unittest.main()
