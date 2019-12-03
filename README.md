<h2 align="center">Ensure Microsoft Excel books content with pytest</h2>

<p align="center">
<a href="https://pypi.org/project/tesxcel/"><img alt="pypi version" src="https://img.shields.io/pypi/v/tesxcel"></a>
<a href="https://travis-ci.org/Colin-b/tesxcel"><img alt="Build status" src="https://api.travis-ci.org/Colin-b/tesxcel.svg?branch=develop"></a>
<a href="https://travis-ci.org/Colin-b/tesxcel"><img alt="Coverage" src="https://img.shields.io/badge/coverage-100%25-brightgreen"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://travis-ci.org/Colin-b/tesxcel"><img alt="Number of tests" src="https://img.shields.io/badge/tests-4 passed-blue"></a>
<a href="https://pypi.org/project/tesxcel/"><img alt="Number of downloads" src="https://img.shields.io/pypi/dm/tesxcel"></a>
</p>

Ensure that two Microsoft Excel files have the same cell types and content in every sheet.

```python
import tesxcel

def test_excel_file_using_path():
    tesxcel.assert_excel_content("/path/to/the/first_file.xlsx", "/path/to/the/second_file.xlsx")

def test_excel_file_using_content():
    received_excel_content: bytes = None
    tesxcel.assert_excel_content(received_excel_content, "/path/to/the/excel_file_to_compare.xlsx")
```

## How to install
1. [python 3.6+](https://www.python.org/downloads/) must be installed
2. Use pip to install module:
```sh
python -m pip install tesxcel
```
