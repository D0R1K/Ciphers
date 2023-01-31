import pytest
from main import Hill

@pytest.mark.parametrize("lang, str, key, is_encr, ans",
                         [('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'НЕДОВЕРЯЙВИКТОРУ', 'БВГЖ', '1', 'ЬЭПНРЁНЪПБИЬЮККИ'),
                          ('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'ЬЭПНРЁНЪПБИЬЮККИ', 'БВГЖ', '2', 'НЕДОВЕРЯЙВИКТОРУ'),
                          ('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'МАКСИМ', 'БВГЕ', '1', 'МЩЯМОР'),
                          ('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'МЩЯМОР', 'БВГЕ', '2', 'МАКСИМ')
                          ])

def test_good(lang, str, key, is_encr, ans):
    assert Hill(lang, str, key, is_encr) == ans


@pytest.mark.parametrize("lang, str, key, is_encr, ans",
                         [('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'НЕ ДОВЕРЯЙ ВИКТОРУ', 'АААА', '1', ''),
                          ('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'МАКСИМ', 'АБАБ', '2', ''),
                          ('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'МАКСИМ', 'БВГ', '1', ''),
                          ('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'НЕ ДОВЕРЯЙ ВИКТОРУ', 'АГБВ', '1', '')
                          ])

def test_bad(lang, str, key, is_encr, ans):
    assert Hill(lang, str, key, is_encr) == ans
