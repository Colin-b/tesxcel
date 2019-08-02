<h2 align="center">Ensure Microsoft Excel books content with pytest</h2>

<p align="center">
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href='https://pse.tools.digital.engie.com/drm-all.gem/job/team/view/Python%20modules/job/tesxcel/job/master/'><img src='https://pse.tools.digital.engie.com/drm-all.gem/buildStatus/icon?job=team/tesxcel/master'></a>
<a href='https://pse.tools.digital.engie.com/drm-all.gem/job/team/view/Python%20modules/job/tesxcel/job/master/cobertura/'><img src='https://pse.tools.digital.engie.com/drm-all.gem/buildStatus/icon?job=team/tesxcel/master&config=testCoverage'></a>
<a href='https://pse.tools.digital.engie.com/drm-all.gem/job/team/view/Python%20modules/job/tesxcel/job/master/lastSuccessfulBuild/testReport/'><img src='https://pse.tools.digital.engie.com/drm-all.gem/buildStatus/icon?job=team/tesxcel/master&config=testCount'></a>
</p>

Ensure that two Microsoft Excel files have the same cell types and content in every sheet.

```python
import tesxcel

def test_excel_file():
    received_excel_content: bytes = None
    tesxcel.assert_excel_content(received_excel_content, "/path/to/the/excel_file_to_compare.xlsx")
```

## How to install
1. [python 3.7+](https://www.python.org/downloads/) must be installed
2. Use pip to install module:
```sh
python -m pip install tesxcel -i https://all-team-remote:tBa%40W%29tvB%5E%3C%3B2Jm3@artifactory.tools.digital.engie.com/artifactory/api/pypi/all-team-pypi-prod/simple
```
