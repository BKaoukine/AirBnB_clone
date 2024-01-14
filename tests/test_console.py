#!/usr/bin/python3
"""Defines unittests for console.py.
Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""

import unittest
from unittest.mock import patch
from io import StringIO
from models import storage
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class."""

    @classmethod
    def setUpClass(cls):
        """Set up the test class."""
        cls.console = HBNBCommand()
        cls.held_output = StringIO()

    @classmethod
    def tearDownClass(cls):
        """Tear down the test class."""
        cls.held_output.close()

    def setUp(self):
        """Set up the test."""
        storage.reload()

    def tearDown(self):
        """Tear down the test."""
        storage.reset()

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, mock_stdout):
        """Assert that the stdout matches the expected output."""
        self.console.cmdloop()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_create(self):
        """Test the create command."""
        with patch('builtins.input', return_value="create BaseModel"):
            self.assert_stdout("** class name missing **\n")
        with patch('builtins.input', return_value="create InvalidModel"):
            self.assert_stdout("** class doesn't exist **\n")
        with patch('builtins.input', return_value="create User"):
            self.assert_stdout("** class doesn't exist **\n")
        with patch('builtins.input', return_value="create BaseModel"):
            self.assert_stdout("\n")
        with patch('builtins.input', return_value="show BaseModel 1234"):
            self.assert_stdout("** instance id missing **\n")
        with patch('builtins.input', return_value="show BaseModel"):
            self.assert_stdout("** instance id missing **\n")

    def test_show(self):
        """Test the show command."""
        with patch('builtins.input', return_value="show BaseModel"):
            self.assert_stdout("** instance id missing **\n")
        with patch('builtins.input', return_value="show BaseModel 1234"):
            self.assert_stdout("** no instance found **\n")
        with patch('builtins.input', return_value="create BaseModel"):
            self.assert_stdout("\n")
        with patch('builtins.input', return_value="show BaseModel"):
            self.assert_stdout("\n")

    def test_destroy(self):
        """Test the destroy command."""
        with patch('builtins.input', return_value="destroy BaseModel"):
            self.assert_stdout("** instance id missing **\n")
        with patch('builtins.input', return_value="destroy BaseModel 1234"):
            self.assert_stdout("** no instance found **\n")
        with patch('builtins.input', return_value="create BaseModel"):
            self.assert_stdout("\n")
        with patch('builtins.input', return_value="destroy BaseModel"):
            self.assert_stdout("** instance id missing **\n")
        with patch('builtins.input', return_value="destroy InvalidModel 1234"):
            self.assert_stdout("** class doesn't exist **\n")

    def test_all(self):
        """Test the all command."""
        with patch('builtins.input', return_value="all"):
            self.assert_stdout("[]\n")
        with patch('builtins.input', return_value="all BaseModel"):
            self.assert_stdout("['[<BaseModel>] (<unknown>) {}\']\n")
        with patch('builtins.input', return_value="create BaseModel"):
            self.assert_stdout("\n")
        with patch('builtins.input', return_value="all BaseModel"):
            self.assert_stdout("['[<BaseModel>] (<unknown>) {}']\n")

    def test_update(self):
        """Test the update command."""
        with patch('builtins.input', return_value="update BaseModel"):
            self.assert_stdout("** instance id missing **\n")
        with patch('builtins.input', return_value="update BaseModel 1234"):
            self.assert_stdout("** no instance found **\n")
        with patch('builtins.input', return_value="create BaseModel"):
            self.assert_stdout("\n")
        with patch('builtins.input', return_value="update BaseModel 1234"):
            self.assert_stdout("** attribute name missing **\n")
        with patch('builtins.input', return_value="update BaseModel 1234 name"):
            self.assert_stdout("** value missing **\n")
        with patch('builtins.input', return_value="update BaseModel 1234 name 'new_name'"):
            self.assert_stdout("\n")


if __name__ == '__main__':
    unittest.main()
