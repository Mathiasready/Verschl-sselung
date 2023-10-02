import pytest
import Caesar

def test_encrypt_basic():
    assert Caesar.encrypt("abc",1) == "bcd"
    assert Caesar.encrypt("abc",1) == "bcd"
    assert Caesar.encrypt("a",6) == "f"
    assert Caesar.encrypt("ac",1) == "bd"
    assert Caesar.encrypt("9:00",1) == "9:00"

