import os.path

import tesxcel


class ExcelTest(tesxcel.ExcelTestCase):
    def test_excel_file_content_with_different_value(self):
        this_dir = os.path.abspath(os.path.dirname(__file__))
        with open(os.path.join(this_dir, "resources", "test_file.xlsx"), "rb") as file:
            with self.assertRaises(Exception) as cm:
                self.assert_excel_content(file.read(), os.path.join(this_dir, "resources", "test_different_value.xlsx"))
        self.assertIn("Different cell in row 5, column 1.", str(cm.exception))

    def test_excel_file_content_with_different_format(self):
        this_dir = os.path.abspath(os.path.dirname(__file__))
        with open(os.path.join(this_dir, "resources", "test_file.xlsx"), "rb") as file:
            with self.assertRaises(Exception) as cm:
                self.assert_excel_content(file.read(), os.path.join(this_dir, "resources", "test_different_format.xlsx"))
        self.assertIn("Different cell type in row 5, column 3.", str(cm.exception))

    def test_excel_file_content(self):
        this_dir = os.path.abspath(os.path.dirname(__file__))
        with open(os.path.join(this_dir, "resources", "test_file.xlsx"), "rb") as file:
            self.assert_excel_content(file.read(), os.path.join(this_dir, "resources", "test_file_copy.xlsx"))
