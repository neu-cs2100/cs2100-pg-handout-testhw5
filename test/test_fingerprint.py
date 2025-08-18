# tests/test_fingerprint.py
import unittest
from fingerprint import FingerPrint
from unittest.mock import patch, mock_open


class TestFingerPrint(unittest.TestCase):
    """
    Create a subclass of unittest.TestCase.
    Put all tests for FingerPrint class inside this class.
    Each test method should start with 'test_'.
    """
    def setUp(self):
        # TODO: initialize all the fingerprints you will be using here
        # Initializing it in the setUp method allows you to reuse it throughout this class
        pass

    def test_direct_constructor(self):
        """Verify direct constructor sets all fields correctly."""
        # TODO: check if all fields are assigned the correct values
        pass

    def test_file_constructor(self):
        """ 
            TODO: Verify file-based constructor reads and sets fields correctly. 
            Read from a real .txt file under root/data/, and verify
            that the file-based constructor parses it correctly.
        """
        pass

    def test_get_number_of_pixels(self):
        """ TODO: Test get_number_of_pixels returns rows * cols."""
        pass

    def test_str(self):
        """ TODO: Test __str__ contains name, year, and pixel count."""
        pass

    def test_display_image(self):
        """ TODO: Test display_image prints the rows correctly."""
        pass

    def test_eq(self):
        """ TODO: Test __eq__ for identical and different fingerprints."""
        pass

    def test_match(self):
        """ 
            TODO: Test the match function between two fingerprints, 
            test at least 3 cases, one with 100% match, 
            one with match > error threshold and the other 
            with match < error threshold.
        """
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)