import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    """Unit tests for the HBNBCommand class"""

    def setUp(self):
        """Set up method for the tests"""
        self.cli = HBNBCommand()

    def test_quit(self):
        """Test the quit command"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.cli.onecmd("quit"))
            self.assertEqual(fake_out.getvalue(), '')

    def test_EOF(self):
        """Test the EOF command"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.cli.onecmd("EOF"))
            self.assertEqual(fake_out.getvalue(), '\n')

    def test_emptyline(self):
        """Test the emptyline method"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertFalse(self.cli.onecmd(""))
            self.assertEqual(fake_out.getvalue(), '')

    def test_create_missing_class(self):
        """Test create command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.onecmd("create")
            self.assertEqual(fake_out.getvalue(), "** class name missing **\n")

    def test_create_invalid_class(self):
        """Test create command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.onecmd("create MyModel")
            self.assertEqual(fake_out.getvalue(), "** classname no exist **\n")

    def test_show_missing_class(self):
        """Test show command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.onecmd("show")
            self.assertEqual(fake_out.getvalue(), "** class name missing **\n")

    def test_show_invalid_class(self):
        """Test show command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.onecmd("show MyModel")
            self.assertEqual(fake_out.getvalue(), "** classname no exist **\n")

    def test_show_missing_id(self):
        """Test show command with missing id"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.onecmd("show BaseModel")
            self.assertEqual(fake_out.getvalue(), "** inst id missing **\n")

    def test_show_no_instance(self):
        """Test show command with no instance found"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cli.onecmd("show BaseModel 1234")
            self.assertEqual(fake_out.getvalue(), "** no instance found **\n")


if __name__ == "__main__":
    unittest.main()
