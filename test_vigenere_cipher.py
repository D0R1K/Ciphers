import pytest
from main import Vigenere

@pytest.mark.parametrize("lang, str, key, is_encr, ans",
                         [('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'ПРАВИТЕЛЬСТВОМ',  'ЖИЗНЬ', '1', 'ЦЩЗПЕЩНУЙНЩКЦЪ'),
                          ('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'ЦЩЗПЕЩНУЙНЩКЦЪ',  'ЖИЗНЬ', '2', 'ПРАВИТЕЛЬСТВОМ'),
                          ('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'НЕДОВЕРЯЙВИКТОРУ', 'КЛЮЧ', '1', 'ШРВЁМРОЦФНЖВЭЪОК'),
                          ('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'ШРВЁМРОЦФНЖВЭЪОК', 'КЛЮЧ', '2', 'НЕДОВЕРЯЙВИКТОРУ')
                          ])

def test_good(lang, str, key, is_encr, ans):
    assert Vigenere(lang, str, key, is_encr) == ans

@pytest.mark.parametrize("lang, str, key, is_encr, ans",
                         [('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'ПРАВИТЕЛЬСТВОМ', 'LIFE', '1', ''),
                          ('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'ШРВЁМРОЦФНЖВЭЪОК', 'HI КЛЮЧ', '2', '')
                          ])

def test_bad(lang, str, key, is_encr, ans):
    assert Vigenere(lang, str, key, is_encr) == ans
