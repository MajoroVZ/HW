import pytest
from HW.HASH.Hash import *


def test_hash_key():
    assert hash_key("test", capacity=100) == 56
    assert hash_key(" ", capacity=100) == 24
    assert hash_key("👽", capacity=100) == 25
    assert hash_key("фыва", capacity=100) == 64
    assert hash_key("А", capacity=100) == 0
    assert hash_key("", capacity=100) == 0
    assert hash_key("privet", capacity=100) == 5
    assert hash_key("Denistoze", capacity=100) == 60
    assert hash_key("c++", capacity=100) == 57
    assert hash_key("C++", capacity=100) == 49
    assert hash_key("python_the_best", capacity=100) == 68
    assert hash_key("front_govno", capacity=100) == 40
    assert hash_key("EGORnerovn", capacity=100) == 90
    assert hash_key("+", capacity=100) == 49
    assert hash_key("php", capacity=100) == 16


def test_set_value():
    hash_table = init_hash_table(3)
    set_value(hash_table, "key1", "value1")
    assert hash_table == [[], [], [["key1", "value1"]]]

    set_value(hash_table, "key2", "value2")
    assert hash_table == [[], [], [["key1", "value1"], ["key2", "value2"]]]

    set_value(hash_table, "key3", "value3")
    assert hash_table == [[['key3', 'value3']], [], [['key1', 'value1'], ['key2', 'value2']]]


ash_table = init_hash_table()


def test_get_value():
    hash_table = init_hash_table()
    set_value(hash_table, "key1", "value1")
    assert get_value(hash_table, "key1") == "value1"

    set_value(hash_table, "key2", "value2")
    assert get_value(hash_table, "key2") == "value2"


def test_del_value():
    hash_table = init_hash_table()
    set_value(hash_table, "key1", "value1")
    del_value(hash_table, "key1")
    assert get_value(hash_table, "key1") is None

    set_value(hash_table, "key2", "value2")
    set_value(hash_table, "key3", "value3")
    del_value(hash_table, "key2")
    assert get_value(hash_table, "key2") is None


def test_load_factor():
    hash_table = init_hash_table(capacity=10)
    set_value(hash_table, "key1", "value1")
    set_value(hash_table, "key2", "value2")
    set_value(hash_table, "key3", "value3")
    set_value(hash_table, "key4", "value4")
    set_value(hash_table, "key5", "value5")
    set_value(hash_table, "key6", "value6")
    set_value(hash_table, "key7", "value7")
    set_value(hash_table, "key8", "value8")
    assert load_factor(hash_table) == 0.8
