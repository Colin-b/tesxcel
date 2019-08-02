import os.path

import pytest

import tesxcel


def test_excel_file_content_with_different_value():
    with open(resource("test_file.xlsx"), "rb") as file:
        with pytest.raises(Exception) as exception_info:
            tesxcel.assert_excel_content(file.read(), resource("test_different_value.xlsx"))
    assert str(exception_info.value) == "Different cell content in row 5, col 1 in Other sheet"


def test_excel_file_content_with_different_format():
    with open(resource("test_file.xlsx"), "rb") as file:
        with pytest.raises(Exception) as exception_info:
            tesxcel.assert_excel_content(file.read(), resource("test_different_format.xlsx"))
    assert str(exception_info.value) == "Different cell type in row 5, col 3 in Sheet1 sheet"


def test_excel_file_content():
    with open(resource("test_file.xlsx"), "rb") as file:
        tesxcel.assert_excel_content(file.read(), resource("test_file_copy.xlsx"))


def resource(file_name: str):
    this_dir = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(this_dir, "resources", file_name)
