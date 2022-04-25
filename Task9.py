import os


def my_func1(path: str) -> dict:
    dirs_list = []
    files_list = []
    list_dir = os.listdir(path)
    for filename in list_dir:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirs_list.append(filename)
        else:
            files_list.append(filename)
    my_dict = {'filenames': files_list, 'dirnames': dirs_list}
    return my_dict


def my_func2(result1: dict, bool_value: bool) -> dict:
    if bool_value:
        dict_sort_list = {'filesnames': sorted(result1['filenames']), 'dirnames': sorted(result1['dirnames'])}
    else:
        dict_sort_list = {'filesnames': sorted(result1['filenames'], reverse=True),
                          'dirnames': sorted(result1['dirnames'], reverse=True)}
    return dict_sort_list


def my_func3(result1: dict, my_str: str) -> dict:
    if "." in my_str:
        upd_dict = {'filesnames': result1['filenames'] + [my_str]}
    else:
        upd_dict = {'dirnames': result1['dirnames'] + [my_str]}
    return upd_dict


path = 'test_dir'
bool_value = False
my_str = 'str.txt'
result1 = my_func1(path)
result2 = my_func2(result1, bool_value)
result3 = my_func3(result1, my_str)
print(f'\n#1\n{result1}\n\n#2\n{result2}\n\n#3\n{result3}\n\n')

# Все пункты являются частью одного задания, поэтому можно использовать функции несколько раз и не дублировать код.
# Если хотите, можете использовать значения по умолчанию и аннотацию типов.
#
# 1. Написать функцию, которая получает один параметр - имя директории и возвращает словарь вида
# {'filenames': [список файлов в папке], 'dirnames': [список всех подпапок в папке]}.
# Подпапки учитывать только первого уровня вложения. Папка в папке в папке - такое не брать ))
#
# 2. Написать функцию, которая получает два параметра - словарь, описанный в пункте 1
# и булевое значение (True/False) - можно сделать параметром по умолчанию.
# Функция возвращает тот же словарь, но с отсортированными именами файлов и папок в соответствующих списках.
# Булевое значение True означает, что порядок сортировки алфавитный, False - обратный порядок.
#
# 3. Написать функцию, которая получает два параметра - словарь, описанный в пункте 1 и строку, которая может быть
# или именем файла, или именем папки. (В имени файла должна быть точка).
# В зависимости от того, что функция получила (имя файла или имя папки) - записать его в соответствующий список
# и вернуть обновленный словарь.
#
# 4* (*сдавать не обязательно, но если будете сдавать, то ошибки будут учитываться тоже).
# Написать функцию, которая получает два параметра - словарь, описанный в пункте 1 и имя директории.
# Функция проверяет соответствие полученного словаря и реальной файловой системы в полученной папке и,
# если надо, создает нужные папaки и пустые файлы, в соответствии со структурой словаря.
