import pytest
from main import Сaesar

@pytest.mark.parametrize("lang, str, key, is_encr, ans",
                         [('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDE', 'A', '1', 'ABCDE'),
                          ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDE', 'A', '2', 'ABCDE'),
                          ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDE', 'C', '1', 'CDEFG'),
                          ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'CDEFG', 'C', '2', 'ABCDE'),
                          ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDE', 'Z', '1', 'ZABCD'),
                          ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ZABCD', 'Z', '2', 'ABCDE'),
                          ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ZABCD', 'Z', '2', 'ABCDE')
                          ])

def test_good(lang, str, key, is_encr, ans):
    assert Сaesar(lang, str, key, is_encr) == ans

@pytest.mark.parametrize("lang, str, key, is_encr, ans",
                         [('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDE', 'AB', '2', ''),
                          ('ABC', 'ABC', 'Z', '1', '')
                          ])

def test_bad(lang, str, key, is_encr, ans):
    assert Сaesar(lang, str, key, is_encr) == ans




