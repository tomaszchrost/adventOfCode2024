from .red_nosed_reports import ReportCheck
import pytest

def test_simple():
    assert ReportCheck([[1, 2, 3, 4, 5]], 1, 3, True).total_safe_reports() == 1

def test_first_value_bad():
    assert ReportCheck([[10, 2, 3, 4, 5]], 1, 3, True).total_safe_reports() == 1
