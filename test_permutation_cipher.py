import pytest
from main import permutation

@pytest.mark.parametrize("lang, str, key, is_encr, ans",
                         [('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'ОВДНЕЕВИЙРЯКУСРТОР', 'ПРИВЕТ', '2', 'НЕДОВЕРЯЙВИКТОРУСР'),
                          ('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'НЕДОВЕРЯЙВИКТОРУСР', 'ПРИВЕТ', '1', 'ОВДНЕЕВИЙРЯКУСРТОР'),
                          ('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'ТВЕУЖДЕРАААН', 'ФЛОТ', '2', 'УТВЕРЖДЕНААА'),
                          ('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'УТВЕРЖДЕНААА', 'ФЛОТ', '1', 'ТВЕУЖДЕРАААН')
                          ])

def test_good(lang, str, key, is_encr, ans):
    assert permutation(lang, str, key, is_encr) == ans

@pytest.mark.parametrize("lang, str, key, is_encr, ans",
                         [('АБВГДЕЁ', 'ОВДНЕЕВИЙРЯКУСРТОР', 'ПРИВЕТ', '2', ''),
                          ('АБВГДЕЁЖЗИЙКМНПРСУХЦЧШЩЪЫЬЭЮЯ', 'ВЕУЖДЕРАААН', 'ФЛОТ', '2', ''),
                          ('АБВ', 'АБВ', 'АБВВ', '1', '')
                          ])

def test_bad(lang, str, key, is_encr, ans):
    assert permutation(lang, str, key, is_encr) == ans
