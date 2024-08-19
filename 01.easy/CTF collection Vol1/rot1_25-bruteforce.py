# rot1_25-bruteforce.py
# Это скрипт ротации методом перебора ROT1 в ROT25.
# Вы вводите зашифрованный текст, и скрипт выведет все потенциальные выходные данные в каждой схеме ROT


def  rot_decode ( cipher_text ):
    # Перебрать все возможные значения ROT (от 1 до 25)
    for rot in  range ( 1 , 26 ):
        decoded_text = ""
        # Перебрать каждый символ в зашифрованном тексте
        for c in cipher_text:
            # Проверить, является ли символ буквой
            if c.isalpha():
                # Определить смещение ASCII на основе того, является ли буква заглавной или строчной
                if c.isupper():
                    ascii_offset = 65
                else :
                    ascii_offset = 97
                # Преобразовать символ в его код ASCII
                 c_code = ord (c)
                # Определить новый код ASCII, применив значение ROT
                 new_c_code = (c_code - ascii_offset + rot) % 26 + ascii_offset
                # Преобразовать новый код ASCII обратно в символ
                 new_c = chr (new_c_code)
                decoded_text += new_c
            else :
                # Если символ не является буквой, добавить его к декодированному тексту как есть
                 decoded_text += c
        # Вывести декодированный текст для текущего значения ROT
        print ( f"ROT {rot:02d}    : {decoded_text} " )


# Запросить у пользователя ввод
cipher_text = input ( "Введите зашифрованный текст: " )
rot_decode(cipher_text)