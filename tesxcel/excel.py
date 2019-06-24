import os
import tempfile
import unittest

import xlrd


class ExcelTestCase(unittest.TestCase):
    def assert_excel_content(self, actual_content: bytes, expected_file_path: str):
        with tempfile.TemporaryDirectory() as temp_dir:
            with open(
                    os.path.join(temp_dir, "actual_excel_file.xlsx"), "wb"
            ) as temp_file:
                temp_file.write(actual_content)

            actual_workbook = xlrd.open_workbook(temp_file.name)

            expected_workbook = xlrd.open_workbook(expected_file_path)

            self.assertCountEqual(actual_workbook.sheet_names(), expected_workbook.sheet_names())

            for sheet_name in actual_workbook.sheet_names():
                self._assert_sheet_content(
                    actual_workbook.sheet_by_name(sheet_name),
                    expected_workbook.sheet_by_name(sheet_name),
                )

    def _assert_sheet_content(self, actual_worksheet, expected_worksheet):
        self.assertEqual(
            actual_worksheet.nrows,
            expected_worksheet.nrows,
            "Different number of rows.",
        )
        self.assertEqual(
            actual_worksheet.ncols,
            expected_worksheet.ncols,
            "Different number of columns.",
        )

        for row_index, actual_row in enumerate(actual_worksheet.get_rows()):
            expected_row = expected_worksheet.row(row_index)
            for cell_index, actual_cell in enumerate(actual_row):
                expected_cell = expected_row[cell_index]
                self.assertEqual(
                    actual_cell.ctype,
                    expected_cell.ctype,
                    f"Different cell type in row {row_index}, column {cell_index}.",
                )
                self.assertEqual(
                    actual_cell.value,
                    expected_cell.value,
                    f"Different cell in row {row_index}, column {cell_index}.",
                )
