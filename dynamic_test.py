from random import sample, randint
from main import Сaesar, Affine, simple_substitution, Hill, permutation, Vigenere

def Caesar_dynamic_tests():
    print("Caesar")
    alphabet = "".join([chr(i) for i in range(ord("А"), ord("Я") + 1)])
    text = "".join([chr(randint(ord("А"), ord("Я"))) for _ in range(randint(1, 20))])
    key = chr(randint(ord("А"), ord("Я")))
    ciphertext = Сaesar(alphabet, text, key, '1')
    print('alphabet:      ', alphabet)
    print('key:           ', key)
    print('text:          ', text)
    print('ciphertext:    ', ciphertext)
    print('decrypted text:', Сaesar(alphabet, ciphertext, key, '2'))
    if text == Сaesar(alphabet, ciphertext, key, '2'):
        print("OK")
    print()

def Affine_dynamic_tests():
    print("Affine")
    alphabet = "".join([chr(i) for i in range(ord("А"), ord("Я") + 1)])
    text = "".join([chr(randint(ord("А"), ord("Я"))) for _ in range(randint(1, 20))])
    ciphertext = ""
    while ciphertext == "":
        key = chr(randint(ord("А"), ord("Я"))) + chr(randint(ord("А"), ord("Я")))
        ciphertext = Affine(alphabet, text, key, '1')
    print('alphabet:      ', alphabet)
    print('key:           ', key)
    print('text:          ', text)
    print('ciphertext:    ', ciphertext)
    print('decrypted text:', Affine(alphabet, ciphertext, key, '2'))
    if text == Affine(alphabet, ciphertext, key, '2'):
        print("OK")
    print()

def simple_substitution_dynamic_tests():
    print("simple_substitution")
    alphabet = "".join([chr(i) for i in range(ord("А"), ord("Я") + 1)])
    text = "".join([chr(randint(ord("А"), ord("Я"))) for _ in range(randint(1, 20))])
    ciphertext = ""
    while ciphertext == "":
        key = "".join(sample(alphabet, len(alphabet)))
        ciphertext = simple_substitution(alphabet, text, key, '1')
    print('alphabet:      ', alphabet)
    print('key:           ', key)
    print('text:          ', text)
    print('ciphertext:    ', ciphertext)
    print('decrypted text:', simple_substitution(alphabet, ciphertext, key, '2'))
    if text == simple_substitution(alphabet, ciphertext, key, '2'):
        print("OK")
    print()

def Hill_dynamic_tests():
    print("Hill")
    alphabet = "".join([chr(i) for i in range(ord("А"), ord("Я") + 1)])
    text = "".join([chr(randint(ord("А"), ord("Я"))) for i in range(randint(1, 20))])
    ciphertext = ""
    while ciphertext == "":
        key = "".join([chr(randint(ord("А"), ord("Я"))) for _ in range(4)])
        ciphertext = Hill(alphabet, text, key, '1')
    print('alphabet:      ', alphabet)
    print('key:           ', key)
    print('text:          ', text)
    print('ciphertext:    ', ciphertext)
    print('decrypted text:', Hill(alphabet, ciphertext, key, '2'))
    if text == Hill(alphabet, ciphertext, key, '2')[:len(text)]:
        print("OK")
    print()

def permutation_dynamic_tests():
    print("permutation")
    alphabet = "".join([chr(i) for i in range(ord("А"), ord("Я") + 1)])
    text = "".join([chr(randint(ord("А"), ord("Я"))) for i in range(randint(1, 20))])
    ciphertext = ""
    while ciphertext == "":
        key = "".join(sample(alphabet, randint(2, len(alphabet))))
        ciphertext = permutation(alphabet, text, key, '1')
    print('alphabet:      ', alphabet)
    print('key:           ', key)
    print('text:          ', text)
    print('ciphertext:    ', ciphertext)
    print('decrypted text:', permutation(alphabet, ciphertext, key, '2'))
    if text == permutation(alphabet, ciphertext, key, '2')[:len(text)]:
        print("OK")
    print()

def Vigenere_dynamic_tests():
    print("Vigenere")
    alphabet = "".join([chr(i) for i in range(ord("А"), ord("Я") + 1)])
    text = "".join([chr(randint(ord("А"), ord("Я"))) for i in range(randint(1, 20))])
    ciphertext = ""
    while ciphertext == "":
        key = "".join(sample(alphabet, randint(2, len(alphabet))))
        ciphertext = Vigenere(alphabet, text, key, '1')
    print('alphabet:      ', alphabet)
    print('key:           ', key)
    print('text:          ', text)
    print('ciphertext:    ', ciphertext)
    print('decrypted text:', Vigenere(alphabet, ciphertext, key, '2'))
    if text == Vigenere(alphabet, ciphertext, key, '2'):
        print("OK")
    print()

for i in range(10):
    Caesar_dynamic_tests()
for i in range(10):
    Affine_dynamic_tests()
for i in range(10):
    simple_substitution_dynamic_tests()
for i in range(10):
    Hill_dynamic_tests()
for i in range(10):
    permutation_dynamic_tests()
for i in range(10):
    Vigenere_dynamic_tests()