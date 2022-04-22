

def create_domains_list(file1: str) -> list:
    domains_list = []
    with open(file1, 'r') as file:
        data = file.read()
    for line in data.split('\n'):
        if line:
            domain = line.replace('.', '')
            domains_list.append(domain)
    return domains_list


def create_names_list(file2: str) -> list:
    names_list = []
    with open(file2, 'r') as file:
        data = file.read()
    for line in data.split('\n'):
        if line:
            name = line.split('\t')[1]
            names_list.append(name)
    return names_list


def create_authors_list(file3: str) -> list:
    authors_list = []
    with open(file3, 'r') as file:
        data = file.read()
    for line in data.split('\n'):
        if '-' in line:
            author = line.split('-')[0]
            authors_list.append({'date': author})
    return authors_list


file1 = f"../Hillel_IT_School_140322/txt_files/domains.txt"
file2 = f"../Hillel_IT_School_140322/txt_files/names.txt"
file3 = f"../Hillel_IT_School_140322/txt_files/authors.txt"
result1 = create_domains_list(file1)
result2 = create_names_list(file2)
result3 = create_authors_list(file3)
print(f'\n#1\n{result1}\n\n#2\n{result2}\n\n#3\n{result3}\n\n')

# Все пункты сделать как отдельные функции и их вызовы.
#
# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).
#
# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"
#
# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt.txt) и возвращает список
# словарей вида {"date": date}
# в которых date - это дата из строки (если есть),
# Например [{"date": "1st January 1919"}, {"date": "8th February 1828"},  ...]
#
# По просьбам некоторых студентов начну включать дополнительные задания.
# 4* (*сдавать не обязательно, но если будете сдавать, то ошибки будут учитываться тоже).
# Написать функцию, которая получает в виде параметра имя файла (authors.txt.txt) и возвращает список
# словарей вида {"date_original": date_original, "date_modified": date_modified}
# в которых date_original - это дата из строки (если есть),
# а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]
