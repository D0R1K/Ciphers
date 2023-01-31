import pytest
from main import simple_substitution

@pytest.mark.parametrize("lang, str, key, is_encr, ans",
                         [('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDE', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '1', 'ABCDE'),
                          ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDE', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '2', 'ABCDE'),
                          ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDE', 'ZXOTPCMLHDFKJBRQYGINWEVASU', '1', 'ZXOTP'),
                          ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ZXOTP', 'ZXOTPCMLHDFKJBRQYGINWEVASU', '2', 'ABCDE'),
                          ( 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDE', 'XLBTFSDGWOREPCZVHNQYUAMIJK', '1', 'XLBTF'),
                          ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'XLBTF',  'XLBTFSDGWOREPCZVHNQYUAMIJK', '2', 'ABCDE')
                          ])

def test_good(lang, str, key, is_encr, ans):
    assert simple_substitution(lang, str, key, is_encr) == ans

@pytest.mark.parametrize("lang, str, key, is_encr, ans",
                         [('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDE', 'AAAAAAAAAAAAAAAAAAAAAAAAAA', '1', ''),
                          ('ABCDEFGHIJKLMNOPQRSTUVWXY', 'ABCDE',  'AAAAAAAAAAAAAAAAAAAAAAAAAA', '1', ''),
                          ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'XLBTF',  'XLBTFSDГWOREPCZVHNQMIJK', '2', ''),
                          ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'XLBTF', 'XLBTFSDGWOREPCZVHNQYUMIJK', '1', '')
                          ])

def test_bad(lang, str, key, is_encr, ans):
    assert simple_substitution(lang, str, key, is_encr) == ans
