import pytest
from main import Affine

@pytest.mark.parametrize("lang, str, key, is_encr, ans",
                         [('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'ХЛИЁЛЕЧЖМЖ', 'ПЮ', '2', 'СЕКРЕТНОГО'),
                          ('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'СЕКРЕТНОГО', 'ПЮ', '1', 'ХЛИЁЛЕЧЖМЖ'),
                          ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ATTACKATDAWN', 'DE', '1', 'EJJEKIEJNESR'),
                          ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'EJJEKIEJNESR', 'DE', '2', 'ATTACKATDAWN')
                          ])

def test_good(lang, str, key, is_encr, ans):
    assert Affine(lang, str, key, is_encr) == ans

@pytest.mark.parametrize("lang, str, key, is_encr, ans",
                         [('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'ХЛИЁЛЕЧЖМЖ', 'ПЕЕ', '2', ''),
                          ('АБВГЯ', 'СЕКРЕТНОГО', 'ПЮ', 'ENCRYPT', ''),
                          ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'EJJEKIEJNESR', 'АБ', '2', '')
                          ])
def test_bad(lang, str, key, is_encr, ans):
    assert Affine(lang, str, key, is_encr) == ans
