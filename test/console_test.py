#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""

import console
import inspect
import pep8
import unittest
HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """
    class created for the testing of documentation of the console
    """
    def test_pep8_conformance_console(self):
        """
        pep8 check for test_console.py
        """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """
        pep8 confirmation of test/test_console.py
        """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/console_test.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """
        test console.py module docstring exist
        """
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """
        test to see if HBNBCommand class docstring exist 
        """
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")
