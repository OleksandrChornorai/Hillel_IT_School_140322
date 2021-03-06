#####################################################
# 1. Дано целое число (int). Определить сколько нулей в этом числе.
print("\n#1.")
number = 10203040
symbol = 0
result = str(number).count(str(symbol))
print(result)
#####################################################
# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля
print("\n#2.")
number = 1002000
str_number = str(number)
result = (len(str_number) - len(str_number.rstrip('0')))
print(result)
#####################################################
# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
print("\n#3.")
my_list_1 = [1, -1, 2, -2, 3, -3]
my_list_2 = [-4, 4, -5, 5, -6, 6]
my_result = []
my_result += list(my_list_1[::2])
my_result += list(my_list_2[1::2])
print(my_result)
#####################################################
# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
print("\n#4.")
my_list = [1, 2, 3, 4]
new_list = []
new_list.extend(my_list[1:] + my_list[:1])
print(new_list)
#####################################################
# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)
print("\n#5.")
my_list = [1, 2, 3, 4]
print(id(my_list))
value = my_list.pop(0)
my_list.append(value)
print(my_list, id(my_list))
#####################################################
# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)
print("\n#6.")
my_str = "43 больше чем 34 но меньше чем 56"
new_str = my_str.split()
my_list = []
for symbol in new_str:
    if symbol.isdigit():
        value = int(symbol)
        my_list.append(value)
result = sum(my_list)
print(result)
#####################################################
# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
print("\n#7.")
my_str = 'hillel it school'
l_limit = 'l'
r_limit = 'o'
index_1 = my_str.find(l_limit) + 1
index_2 = my_str.rfind(r_limit)
sub_str = my_str[index_1:index_2]
print(sub_str)
#####################################################
# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)
print("\n#8.")
my_str = 'abcdefg'
new_str = len(my_str)
my_list =[]
if new_str % 2:
    my_str += '_'
for symbol in range(0, new_str, 2):
    my_list.append(my_str[symbol:symbol + 2])
print(my_list)
#####################################################
# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
print("\n#9.")
my_list = [2, 4, 1, 5, 3, 9, 0, 7]
value = 0
for symbol in range(1, len(my_list) - 1):
    if my_list[symbol] > (my_list[symbol - 1] + my_list[symbol + 1]):
        value += 1
print(value)
#####################################################
# 10. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.
print("\n#10.")
my_list = [1, 2, 3, "11", "22", 33]
new_list =[]
for symbol in my_list:
    if type(symbol) == str:
        new_list.append(symbol)
print(new_list)
#####################################################
# 11. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке ТОЛЬКО ОДИН раз.
print("\n#11.")
my_str = 'Hillel'
my_list =[]
for symbol in set(my_str):
    if my_str.count(symbol) == 1:
        my_list.append(symbol)
print(my_list)
#####################################################
# 12. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
print("\n#12.")
str_1 = 'string1'
str_2 = 'ssiiing2'
my_list = list(set(str_1).intersection(set(str_2)))
print(my_list)
#####################################################
# 13. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой ТОЛЬКО ПО ОДНОМУ разу.
# Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"], т.к. эти символы есть в каждой строке по одному разу
print("\n#13.")
str_1 = 'aaaasdf1'
str_2 = 'asdfff2'
my_list = []
set_1 = set(str_1)
set_2 = set(str_2)
result_intersection = set_1.intersection(set_2)
for symbol in result_intersection:
    if str_1.count(symbol) == 1 and str_2.count(symbol) == 1:
        my_list.append(symbol)
print(my_list)