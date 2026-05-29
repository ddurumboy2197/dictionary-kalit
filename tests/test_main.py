# test_dict.py
import pytest
from dictionary_utils import get_all_keys

def test_get_all_keys():
    dict1 = {"a": 1, "b": 2, "c": 3}
    assert get_all_keys(dict1) == ["a", "b", "c"]

def test_get_all_keys_empty_dict():
    dict1 = {}
    assert get_all_keys(dict1) == []

def test_get_all_keys_dict_with_nested_dict():
    dict1 = {"a": 1, "b": {"c": 2, "d": 3}}
    assert get_all_keys(dict1) == ["a", "b", "c", "d"]

def test_get_all_keys_dict_with_list():
    dict1 = {"a": 1, "b": [2, 3]}
    with pytest.raises(TypeError):
        get_all_keys(dict1)
