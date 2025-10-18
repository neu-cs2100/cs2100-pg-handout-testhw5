# tests/test_fileprocessor.py
import os
import unittest
from fingerprint import FingerPrint
import fileprocessor

class TestFileProcessor(unittest.TestCase):
    """
    Tests for fileprocessor.py module using .txt files under root/data/.
    """
    @classmethod
    def setUpClass(cls):
        # Locate the data directory at project root
        tests_dir = os.path.dirname(__file__)
        project_root = os.path.abspath(os.path.join(tests_dir, '..'))
        cls.data_dir = os.path.join(project_root, 'data')
        # TODO: assert that data_dir exists and contains .txt files
        cls.sample_files = [
            os.path.join(cls.data_dir, fn)
            for fn in os.listdir(cls.data_dir)
            if fn.lower().endswith('.txt')
        ]

    def test_load_fingerprint(self):
        """
        For each real fingerprint file, load it and verify header fields.
        """
        for path in self.sample_files:
            with self.subTest(file=path):
                # TODO: Read the first four lines of 'sample file (path)' manually
                # TODO: Load the fingerprint
                # TODO: Assert get_name(), get_year(), get_rows(), get_cols()
                pass

    def test_main_access_granted(self):
        """
        Simulate entering the original file path and expect access granted.
        """
        # TODO: Set fileprocessor.original to the original.txt file.
        # Pass that as input into the method which compares two fingerprints,
        # the second fingerprint being the same one as the original.
        # Use assertions to verify that the access is granted successfully when fingerprints match.
        
        # TODO: Use one of the variation.txt files, these are the original finagerprint with a few characters changed.
        # Now test that the access is granted successfully, given that
        # the error threshold is met. (Print the error threshold alongside the match % for easier readability)
        pass

    def test_main_delegates_authentication(self):
        """
        Simulate main() calling IncidentResponse.authenticate.
        """
        # 1. Use unittest.mock.patch to replace IncidentResponse.authenticate
        #    so it records how it was called, e.g.:
        #       with patch('IncidentResponse.authenticate') as mock_auth:
        #
        # 2. Provide a fake sequence of user inputs for file names:
        #    - First input: the path to a valid fingerprint file (e.g. 'data/User1.txt')
        #    - Second input: something to make the loop exit after authenticate returns True
        #    You can patch builtins.input() to return these values in order.
        #
        # 3. Also patch load_fingerprint so it returns a FingerPrint object
        #    without reading disk, if you like:
        #       with patch('fileprocessor.load_fingerprint') as mock_loader:
        #           mock_loader.return_value = FingerPrint('data/User1.txt')
        #
        # 4. Call fileprocessor.main().
        #
        # 5. After main() finishes, assert that:
        #       mock_auth.assert_called_once_with(mock_loader.return_value)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)