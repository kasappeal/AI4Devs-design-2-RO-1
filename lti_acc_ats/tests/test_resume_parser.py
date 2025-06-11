import unittest
import os
from PyPDF2 import PdfWriter

# Adjust the import path based on your project structure.
# This assumes lti_acc_ats is in the PYTHONPATH or the tests are run from the project root.
from lti_acc_ats.core.resume_parser import ResumeParser, CorruptedFileError, PasswordProtectedFileError

class TestResumeParser(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures, if any."""
        self.parser = ResumeParser()
        self.test_files_dir = "lti_acc_ats_test_temp_files" # Define a temporary directory for test files
        os.makedirs(self.test_files_dir, exist_ok=True)

    def tearDown(self):
        """Tear down test fixtures, if any."""
        # Clean up the temporary directory and its contents
        for f in os.listdir(self.test_files_dir):
            os.remove(os.path.join(self.test_files_dir, f))
        os.rmdir(self.test_files_dir)

    def _get_test_filepath(self, filename):
        """Helper to get full path for a test file."""
        return os.path.join(self.test_files_dir, filename)

    def test_parse_corrupted_pdf(self):
        """Test parsing a corrupted (empty) PDF file."""
        corrupted_filepath = self._get_test_filepath("corrupted.pdf")
        with open(corrupted_filepath, 'w') as f:
            # An empty file is not a valid PDF and will cause PdfReadError
            pass

        with self.assertRaises(CorruptedFileError) as context:
            self.parser.parse_document(corrupted_filepath)
        self.assertTrue(f"Failed to parse document due to corruption or read error: {corrupted_filepath}" in str(context.exception))

    def test_parse_password_protected_pdf(self):
        """Test parsing a password-protected PDF file."""
        protected_filepath = self._get_test_filepath("protected.pdf")
        writer = PdfWriter()
        writer.add_blank_page(width=8.5 * 72, height=11 * 72)  # Standard letter size
        writer.encrypt('testpassword')
        with open(protected_filepath, 'wb') as f:
            writer.write(f)

        with self.assertRaises(PasswordProtectedFileError) as context:
            self.parser.parse_document(protected_filepath)
        self.assertEqual(str(context.exception), f"File is password-protected: {protected_filepath}")

    def test_parse_valid_dummy_pdf(self):
        """Test parsing a simple, valid (non-encrypted) PDF file."""
        valid_filepath = self._get_test_filepath("valid.pdf")
        writer = PdfWriter()
        writer.add_blank_page(width=8.5 * 72, height=11 * 72)
        with open(valid_filepath, 'wb') as f:
            writer.write(f)

        expected_result = {"status": "success", "message": "File processed successfully."}
        actual_result = self.parser.parse_document(valid_filepath)
        self.assertEqual(actual_result, expected_result)

    def test_parse_non_pdf_file(self):
        """Test parsing a non-PDF file (e.g., a text file)."""
        text_filepath = self._get_test_filepath("sample.txt")
        with open(text_filepath, 'w') as f:
            f.write("This is a test text file, not a PDF.")

        # This should also return the standard success message as it's not a PDF
        # and thus won't trigger PDF-specific encryption checks.
        # The current implementation only performs special checks for .pdf files.
        expected_result = {"status": "success", "message": "File processed successfully."}
        actual_result = self.parser.parse_document(text_filepath)
        self.assertEqual(actual_result, expected_result)

    def test_parse_pdf_corrupted_after_opening(self):
        """Test parsing a PDF that becomes corrupted after initial open (simulated)."""
        # This test is a bit more conceptual for the current implementation,
        # as the f.read(10) is the main check after open.
        # If a file is truly malformed, PyPDF2's PdfReader instantiation would fail.
        corrupted_data_filepath = self._get_test_filepath("corrupted_data.pdf")
        # Create a file that looks like a PDF but has bad data where PdfReader expects good data
        with open(corrupted_data_filepath, 'wb') as f:
            f.write(b"%PDF-1.4\n%fake content that will cause issues\n")
            # This is a simplified way; real PDF corruption is more complex.
            # PyPDF2 might error out just trying to read the header or cross-reference table.

        with self.assertRaises(CorruptedFileError):
            self.parser.parse_document(corrupted_data_filepath)


if __name__ == '__main__':
    unittest.main()
