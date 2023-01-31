from math import gcd, sqrt, floor

def phi(n):
    rslt = n
    for i in range (2, floor(sqrt(n))):
        if n % i == 0:
            while n % i == 0:
                n /= i
            rslt -= rslt / i
    if n > 1:
        rslt -= rslt / n
    return int(rslt)

def Сaesar(lang, str, key, is_encr):
    if (key not in lang):
        print("Неверный ключ!")
        return ""
    else:
        key = lang.index(key)
        if (is_encr == '2'):
            key *= -1
        return ''.join([lang[(lang.index(c) + key) % len(lang)] for c in str])

def Affine(lang, str, key, is_encr):
    if(len(key) != 2):
        print("Неверный формат ключа!")
        return ""
    elif (key[0] not in lang or key[1] not in lang):
       print("Неверный ключ! (не принадлежит алфавиту)")
       return ""
    elif (gcd(len(lang), lang.index(key[0])) != 1):
       print("Неверный ключ! (не простое число)")
       return ""
    else:
       if (is_encr == '1'):
           return ''.join([lang[(lang.index(key[0]) * lang.index(c) + lang.index(key[1])) % len(lang)] for c in str])
       else:
            return ''.join([lang[((lang.index(key[0]) ** (phi(len(lang)) - 1)) * (lang.index(c) - lang.index(key[1])))
                                 % len(lang)] for c in str])

def simple_substitution(lang, str, key, is_encr):
    if (sorted(lang) != sorted(key)):
        print("Неверный ключ!")
        return ""
    else:
        if(is_encr == '1'):
            return "".join([key[lang.index(c)] for c in str])
        else:
            return "".join([lang[key.index(c)] for c in str])

def Hill(lang, str, key, is_encr):
    if (len(key) != 4):
        print("Неверный формат ключа!")
        return ""
    elif (key[0] not in lang) or (key[1] not in lang) or (key[2] not in lang) or (key[3] not in lang):
        print("Неверный ключ! (не принадлежит алфавиту)")
        return ""
    elif ((lang.index(key[0]) * lang.index(key[3]) - lang.index(key[1]) * lang.index(key[2])) % len(lang) == 0):
        print("Неверный ключ! (вырожденная матрица)")
        return ""
    elif (gcd(lang.index(key[0]) * lang.index(key[3]) - lang.index(key[1]) * lang.index(key[2]), len(lang)) != 1):
        print("Неверный ключ! (не взаимно просты)")
        return ""
    else:
        if len(str) % 2 != 0:
            str += lang[0]
        if (is_encr == '1'):
            res = ''
            for i in range(0, len(str), 2):
                res += lang[
                    (lang.index(str[i]) * lang.index(key[0]) + lang.index(str[i + 1]) * lang.index(key[2])) % len(lang)]
                res += lang[
                    (lang.index(str[i]) * lang.index(key[1]) + lang.index(str[i + 1]) * lang.index(key[3])) % len(lang)]
            return res
        else:
            res = ''
            det_1 = (lang.index(key[0]) * lang.index(key[3]) - lang.index(key[1]) * lang.index(key[2])) ** (phi(len(lang)) - 1)
            for j in range(0, len(str), 2):
                res += lang[(det_1 * (lang.index(str[j]) * lang.index(key[3]) - lang.index(str[j + 1])
                                  * lang.index(key[2]))) % len(lang)]
                res += lang[(det_1 * (-lang.index(str[j]) * lang.index(key[1]) + lang.index(str[j + 1])
                                  * lang.index(key[0]))) % len(lang)]
            return res

def permutation(lang, str, key, is_encr):
    for c in key:
        if c not in lang:
            print("Неверный ключ! (не принадлежит алфавиту)")
            return ""
    if (len(key) > len(set([i for i in key]))):
        print("Неверный ключ! (повтор символов)")
        return ""
    else:
        lst2 = [i for i in key]
        lst1 = sorted(lst2)
        if (len(str) % len(key) != 0):
            for _ in range(len(key) - (len(str) % len(key))):
                str += lang[0]
        res = ""
        if (is_encr == '1'):
            for i in range(0, len(str), len(key)):
                for j in range(len(key)):
                    res += str[i + lst2.index(lst1[j])]
            return res
        else:
            for i in range(0, len(str), len(key)):
                for j in range(len(key)):
                    res += str[i + lst1.index(lst2[j])]
            return res

def Vigenere(lang, str, key, is_encr):
    for c in key:
        if (c not in lang):
            print("Неверный ключ!")
            return ""
    new_key = key
    for i in range(len(str) - len(key)):
        new_key += key[i % len(key)]
    if (is_encr == '1'):
        return "".join([lang[(lang.index(str[i]) + lang.index(new_key[i])) % len(lang)] for i in range(len(str))])
    else:
        return "".join([lang[(lang.index(str[i]) - lang.index(new_key[i])) % len(lang)] for i in range(len(str))])

if __name__ == '__main__':
    try:
        with open('alphabet.txt', 'r') as f_alph:
            abc = f_alph.readline()
            if (len(abc) == 0):
                abc = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
            if len(set([i for i in abc])) != len(abc):
                print("Символы не уникальны!")
                exit(666)
        print("Алфавит:", abc, sep='\n')  # некорректный алфавит!!!

        with open('in.txt', 'r') as f_in:
            text = f_in.readline()
            for c in text:
                if (c not in abc):
                    print("Символ", c, "не является символом алфавита!")  # завершить нормально!!!
                    exit(666)
        print("Входной текст:", text, sep='\n')

        with open('key.txt', 'r') as f_key:
            k = f_key.readline()
    except IOError as e:
        print(u'Не удалось открыть файл!')

    while (True):
        print("Выберите операцию:", "зашифрование (введите '1')", "расшифрование (введите '2')", sep='\n')
        a = input()
        if (a == '1') or (a == '2'):
            break
    while (True):
        print("Выберите шифр:", "Шифр сдвига (введите '1')", "Афинный шифр (введите '2')",
              "Шифр простой замены (введите '3')", "Шифр Хилла (введите '4')",
              "Шифр перестановки (введите '5')", "Шифр Виженера (введите '6')", sep='\n')
        b = input()
        if (len(b) == 1 and ord('1') <= ord(b) <= ord('6')):
            break

    ciphers = {
        1: Сaesar,
        2: Affine,
        3: simple_substitution,
        4: Hill,
        5: permutation,
        6: Vigenere
    }

    print(ciphers[int(b)](abc, text, k, a))
