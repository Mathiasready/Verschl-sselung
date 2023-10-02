import pytest
import Caesar
import random
import string


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def test_encrypt_random():
    for i in range(1000):
        clear = get_random_string(random.randint(0, 100))
        key = random.randint(0, 100)
        hidden = Caesar.encrypt(clear, key)
        decrypted = Caesar.decrypt(hidden, key)
        assert clear.lower() == decrypted


def test_encrypt_basic():
    assert Caesar.encrypt("abc", 1) == "bcd"
    assert Caesar.encrypt("a", 3) == "d"
    assert Caesar.encrypt("", 1) == ""
    assert Caesar.encrypt("hallo", 2) == "jcnnq"
    assert Caesar.encrypt("Hi", 2) == "jk"
    assert Caesar.encrypt("Hi!", 2) == "jk!"
    assert Caesar.encrypt("9:00", 2) == "1:22"
    assert Caesar.encrypt("xyz", 2) == "zab"
