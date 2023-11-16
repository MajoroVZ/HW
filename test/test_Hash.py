import pytest
from HW.HASH.Hash import *


@pytest.mark.parametrize("key,expected",
                         [("test", 56),
                          ("privet", 5),
                          ("Denistoze", 60),
                          ("c++", 57),
                          ("C++", 49),
                          ("python_the_best", 68),
                          ("front_govno", 40),
                          ("EGORnerovn", 90),
                          ("+", 49),
                          ("php", 16)
                          ])
def test_hash_key(key, expected):
    hash_table = init_hash_table()
    assert hash_key(key, len(hash_table[1])) == expected


@pytest.mark.parametrize("key,value",
                         [("key1", "value1"),
                          ("key2", "value2"),
                          ("key3", "value3"),
                          ("key4", "value4"),
                          ("key5", "value5"),
                          ("key6", "value6"),
                          ("key7", "value7"),
                          ("key8", "value8"),
                          ("key9", "value9"),
                          ("key10", "value10")
                          ])
def test_set_value(key, value):
    hash_table = init_hash_table()
    set_value(hash_table, key, value)
    assert get_value(hash_table, key) == value


@pytest.mark.parametrize("key,value",
                         [("key1", "value1"),
                          ("key2", "value2"),
                          ("key3", "value3"),
                          ("key4", "value4"),
                          ("key5", "value5"),
                          ("key6", "value6"),
                          ("key7", "value7"),
                          ("key8", "value8"),
                          ("key9", "value9"),
                          ("key10", "value10")
                          ])
def test_get_value(key, value):
    hash_table = init_hash_table()
    set_value(hash_table, key, value)
    assert get_value(hash_table, key) == value


@pytest.mark.parametrize("key,value",
                         [("key1", "value1"),
                          ("key2", "value2"),
                          ("key3", "value3"),
                          ("key4", "value4"),
                          ("key5", "value5"),
                          ("key6", "value6"),
                          ("key7", "value7"),
                          ("key8", "value8"),
                          ("key9", "value9"),
                          ("key10", "value10")
                          ])
def test_del_value(key, value):
    hash_table = init_hash_table()
    set_value(hash_table, key, value)
    del_value(hash_table, key)
    assert get_value(hash_table, key) is None


def test_load_factor():
    hash_table = init_hash_table(capacity=100)
    set_value(hash_table, "key1", "value1")
    set_value(hash_table, "key2", "value2")
    set_value(hash_table, "key3", "value3")
    set_value(hash_table, "key4", "value4")
    set_value(hash_table, "key5", "value5")
    set_value(hash_table, "key6", "value6")
    set_value(hash_table, "key7", "value7")
    set_value(hash_table, "key8", "value8")
    set_value(hash_table, "key9", "value9")
    set_value(hash_table, "key10", "value10")
    assert load_factor(hash_table) == 0.1
