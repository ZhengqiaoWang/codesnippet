'''
Author: 王政乔 me@zhengqiao.wang
Date: 2022-10-01 00:00:00
LastEditors: 王政乔 me@zhengqiao.wang
LastEditTime: 2022-10-01 00:00:00
FilePath: /codesnippet/python/test_excel_oper.py
Description: excel操作ut
Website: https://www.zhengqiao.wang
'''

import os
import pytest
import openpyxl
from excel_oper import ExcelOper

ABC = [
    "a",
    "b",
    "c",
    "d",
    "a",
    "b",
    "c",
    "d",
    "a",
    "b",
    "c",
    "d",
    "a",
    "b",
    "c",
    "d",
    "a",
    "b",
    "c",
    "d",
]

XLSFilePath = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "resource", "excel_oper.xls")
XLSXFilePath = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "resource", "excel_oper.xlsx")


@pytest.fixture
def rmXlsxFile():
    os.remove(XLSXFilePath)


def test_open_xls(rmXlsxFile):
    eo = ExcelOper(ExcelOper.translateToXLSX(XLSFilePath), 0)
    eo.setStartLine(2).setEndLine(-2).registColGet("列one",
                                                   2).registColGet("列six", 7)
    i = 1
    for row_record in eo.getDatas():
        assert(i == int(row_record["列one"]))
        assert(row_record["列six"] == ABC[i-1])
        i += 1


def test_open_xls_failed():
    eo = ExcelOper(XLSFilePath, 0)
    eo.setStartLine(2).setEndLine(-2).registColGet("列one",
                                                   2).registColGet("列six", 7)
    result = eo.getDatas()
    with pytest.raises(openpyxl.utils.exceptions.InvalidFileException) as e:
        next(result)


def test_trans_xls_failed():
    with pytest.raises(RuntimeError) as e:
        ExcelOper.translateToXLSX(".")
