from typing import Union
import xlrd
from xlrd.sheet import Sheet


def assert_excel_content(
    file_path_or_actual_content: Union[str, bytes], expected_file_path: str
):
    if isinstance(file_path_or_actual_content, str):
        actual_workbook = xlrd.open_workbook(file_path_or_actual_content)
    else:
        actual_workbook = xlrd.open_workbook(file_contents=file_path_or_actual_content)
    expected_workbook = xlrd.open_workbook(expected_file_path)

    assert sorted(actual_workbook.sheet_names()) == sorted(
        expected_workbook.sheet_names()
    ), "Different sheet names"

    for sheet_name in actual_workbook.sheet_names():
        _assert_sheet_content(
            sheet_name,
            actual_workbook.sheet_by_name(sheet_name),
            expected_workbook.sheet_by_name(sheet_name),
        )


def _assert_sheet_content(
    sheet_name: str, actual_worksheet: Sheet, expected_worksheet: Sheet
):
    assert (
        actual_worksheet.nrows == expected_worksheet.nrows
    ), f"Different number of rows in {sheet_name} sheet"
    assert (
        actual_worksheet.ncols == expected_worksheet.ncols
    ), f"Different number of columns in {sheet_name} sheet"

    for row_index, actual_row in enumerate(actual_worksheet.get_rows()):
        expected_row = expected_worksheet.row(row_index)
        for cell_index, actual_cell in enumerate(actual_row):
            expected_cell = expected_row[cell_index]
            assert (
                actual_cell.ctype == expected_cell.ctype
            ), f"Different cell type in row {row_index}, col {cell_index} in {sheet_name} sheet"
            assert (
                actual_cell.value == expected_cell.value
            ), f"Different cell content in row {row_index}, col {cell_index} in {sheet_name} sheet"
