#####################################################   1   #####################################################
print('\n_Задача №1_ ')
value = 80
new_value = value / 2 if value < 100 else -value
print(f'\n> Результат: {new_value} <')
#####################################################   2   #####################################################
print('\n\n_Задача №2_')
value = 80
new_value = 1 if value < 100 else 0
print(f'\n> Результат: {new_value} <')
#####################################################   3   #####################################################
print('\n\n_Задача №3_')
value = 80
new_value = True if value < 100 else False
print(f'\n> Результат: {new_value} <')
#####################################################   4   #####################################################
print('\n\n_Задача №4_')
my_str = 'hillel'
if len(my_str) < 5:
    print(f'\n> Результат: {my_str * 2} <')
else:
    print(f'\n> Результат: {my_str} <')
#####################################################   5   #####################################################
print('\n\n_Задача №5_')
my_str = 'py'
if len(my_str) < 5:
    print(f'\n> Результат: {my_str + my_str[::-1]} <')
else:
    print(f'\n> Результат: {my_str} <')
#####################################################   6   #####################################################
print("\n>>> Calculator by Python ver. 2.0 <<<\n>>> Welcome! <<<\n")
while True:
    input_case = input("Выбери тип операции:\n1 +\n2 -\n3 *\n4 /\n")
    if input_case in '1234':
        try:
            value_1 = float(input("Введи первое число:"))
            value_2 = float(input("Введи второе число:"))
            if input_case == '1':
                result = (value_1 + value_2)
                symbol ='+'
            elif input_case == '2':
                result = (value_1 - value_2)
                symbol = '-'
            elif input_case == '3':
                result = (value_1 * value_2)
                symbol = '*'
            else:
                result = (value_1 / value_2)
                symbol = '/'
            print(f"\nРезультат: {value_1} {symbol} {value_2} = {result} \n\n>>> Операция завершена <<<")
        except ZeroDivisionError:
            print("\n>>> На 0 делить нельзя!!! <<<")
        except ValueError:
            print("\n>>> Некорректное значение! <<<")
    else:
        print("\n>>> Неверная операция! <<<")