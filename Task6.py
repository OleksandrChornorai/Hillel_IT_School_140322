#####################################################
# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.
print("\n#1.")
my_list = ['Anna', 'John', 'Aleksandr', 'Tom', 'Vladimir', 'Nick', 'Tatyana', 'Ben']
new_list = []
for index, value in enumerate(my_list):
    if index % 2:
        new_list.append(value[::-1])
    else:
        new_list.append(value)
print(new_list)
#####################################################
# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
print("\n#2.")
my_list = ['Anna', 'Ivan', 'Anton', 'Aleksandr', 'Vladimir', 'Tatyana']
new_list = []
symbol = 'A'
for value in my_list:
    if value.startswith(symbol):
        new_list.append(value)
print(new_list)
#####################################################
# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
print("\n#3.")
my_list = ['Anna', 'John', 'Aleksandr', 'Vladimir', 'Tom', 'Tatyana', 'Jennifer']
new_list = []
symbol = 'a'
for value in my_list:
    if value.count(symbol):
        new_list.append(value)
print(new_list)
#####################################################
# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Создать список и поместить туда имя самого молодого человека. Если возраст совпадает - поместить все имена самых молодых.
# б) Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.
# в) Посчитать среднее количество лет всех людей из начального списка.
print("\n#4.")
persons = [{"name": "John", "age": 25},
           {"name": "Tom", "age": 43},
           {"name": "Donald", "age": 8},
           {"name": "Ben", "age": 15},
           {"name": "Michael", "age": 31},
           ]
age = []
name = []
for value in persons:
    age.append(value["age"])
    name.append(len(value["name"]))
min_age = min(age)
long_name = max(name)
for value in persons:
    if value['age'] == min_age:
        print(f'Самый молодой: {value["name"]}')
for value in persons:
    if len(value['name']) == long_name:
        print(f'Самое длинное имя: {value["name"]}')
av_age = sum(age) / len(age)
print(f'Средний возраст: {av_age}')
#####################################################
# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
#
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}
print("\n#5.")
my_dict_1 = {'name': 'John', 'docs': 'passport'}
my_dict_2 = {'s_name': 'Smith', 'docs': 'driver licence'}
list_same = []
list_dif = []
new_dict = {}
untd_dict = {}

for key in my_dict_1:
    if key in my_dict_2:
        list_same.append(key)
print(f'Ключ в обоих словарях: {list_same}')
for key in my_dict_1:
    if key not in my_dict_2:
        list_dif.append(key)
print(f'Уникальный ключ: {list_dif}')
for key, value in my_dict_1.items():
    if key not in my_dict_2:
        new_dict[key] = value
print(f'Новый словарь: {new_dict}')
for key, value in my_dict_1.items():
    for key2, value2 in my_dict_2.items():
        if key not in my_dict_2:
            untd_dict[key] = value
        elif key2 not in my_dict_1:
            untd_dict[key2] = value2
        else:
            untd_dict[key] = [value, value2]
print(f'Объединенный словарь: {untd_dict}')