# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
my_list1 = ['Anna', 'John', 'Aleksandr', 'Tom', 'Vladimir']


def func1_list(my_list1):
    new_list1 = my_list1.copy()
    for index1, value1 in enumerate(my_list1):
        if index1 % 2:
            new_list1[index1] = value1[::-1]
    return new_list1


result1 = func1_list(my_list1)
# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".


def func2_list(my_list1):
    new_list2 = []
    for symbol2 in my_list1:
        if 'a' == symbol2.lower()[0]:
            new_list2.append(symbol2)
    return new_list2


result2 = func2_list(my_list1)
# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.


def func3_list(my_list1):
    new_list3 = []
    for symbol3 in my_list1:
        if 'a' in symbol3:
            new_list3.append(symbol3)
    return new_list3


result3 = func3_list(my_list1)
# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.
my_list2 = [1, 2, 3, "11", "22", 33, "qwerty"]


def func4_list(my_list2):
    new_list4 = []
    for symbol4 in my_list2:
        if type(symbol4) == str:
            new_list4.append(symbol4)
    return new_list4


result4 = func4_list(my_list2)
# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.
my_str5 = 'Hillel it school'


def func5_list(my_str5):
    my_list5 = []
    for symbol5 in set(my_str5):
        if my_str5.count(symbol5) == 1:
            my_list5.append(symbol5)
    return my_list5


result5 = func5_list(my_str5)
# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
my_str_1 = 'string1'
my_str_2 = 'ssiiing2'


def func6_list(my_str_1, my_str_2):
    my_list6 = list(set(my_str_1).intersection(set(my_str_2)))
    return my_list6


result6 = func6_list(my_str_1, my_str_2)
# 7. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.


def func7_list(my_str_1, my_str_2):
    my_list7 = []
    for symbol7 in set(my_str_1).intersection(set(my_str_2)):
        if my_str_1.count(symbol7) == 1 and my_str_2.count(symbol7) == 1:
            my_list7.append(symbol7)
    return my_list7


result7 = func7_list(my_str_1, my_str_2)
# 8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.

import random
import string

names = ['ben', 'tom', 'john', 'jack']
domains = ['net', 'com', 'ua', 'org']


def create_email(domains, names):
    rdm_names = f'{random.choice(names)}.{str(random.randint(100, 999))}'
    rdm_str = "".join(random.choice(string.ascii_lowercase) for symbol8 in range(random.randint(5, 7)))
    rdm_dmns = f'{rdm_str}.{random.choice(domains)}'
    result8 = f'{rdm_names}@{rdm_dmns}'
    return result8


e_mail = create_email(domains, names)

print(f'#1\n{result1}\n#2\n{result2}\n#3\n{result3}\n#4\n{result4}'
      f'\n#5\n{result5}\n#6\n{result6}\n#7\n{result7}\n#8\n{e_mail}')
# Пример использования функции:
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com
