import json
import pytest
from utlis.functions import import_json, find_operations_json, executed, filter_executed

def test_import_json():
    assert isinstance(import_json(), list) == True

def test_find_operations_json():
    assert isinstance(find_operations_json(), str) == True
    assert isinstance(find_operations_json(name_json='op.json'), str) == False
    assert isinstance(find_operations_json(name_json='op'), str) == False



def test_executed():
    assert executed({"state": "EXECUTED"}) == True
    assert not executed({"state": "PENDING"}) == True


def test_filter_executed(monkeypatch):
    mock_import_json = lambda: [
        {"state": "EXECUTED", "date": "2023-01-01"},
        {"state": "PENDING", "date": "2023-01-02"},
        {"state": "EXECUTED", "date": "2023-01-03"}
    ]
    monkeypatch.setattr("your_module.import_json", mock_import_json)
    assert list(filter_executed()) == [
        {"state": "EXECUTED", "date": "2023-01-01"},
        {"state": "EXECUTED", "date": "2023-01-03"}
    ]

def test_sorted_date(monkeypatch):
    mock_filter_executed = lambda: [
        {"state": "EXECUTED", "date": "2023-01-01"},
        {"state": "EXECUTED", "date": "2023-01-03"}
    ]
    monkeypatch.setattr("your_module.filter_executed", mock_filter_executed)
    assert sorted_date() == [
        {"state": "EXECUTED", "date": "2023-01-03"},
        {"state": "EXECUTED", "date": "2023-01-01"}
    ]