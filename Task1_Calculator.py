print("\n>>> Calculator by Python ver. 1.0 <<<\n>>> Welcome! <<<\n")
input_case = input("Выбери тип операции:\n1 +\n2 -\n3 *\n4 /\n")
try:
    if input_case == '1':
        value_1 = float(input("Введи первое число:"))
        value_2 = float(input("Введи второе число:"))
        result = (value_1 + value_2)
        print(f"Результат: {result} \n\n>>> Операция завершена <<<")
    elif input_case == '2':
        value_1 = float(input("Введи первое число:"))
        value_2 = float(input("Введи второе число:"))
        result = (value_1 - value_2)
        print(f"Результат: {result} \n\n>>> Операция завершена <<<")
    elif input_case == '3':
        value_1 = float(input("Введи первое число:"))
        value_2 = float(input("Введи второе число:"))
        result = (value_1 * value_2)
        print(f"Результат: {result} \n\n>>> Операция завершена <<<")
    elif input_case == '4':
        value_1 = float(input("Введи первое число:"))
        value_2 = float(input("Введи второе число:"))
        result = (value_1 / value_2)
        print(f"Результат: {result} \n\n>>> Операция завершена <<<")
    else:
        print("\n>>> Неверная операция! <<<")
except ZeroDivisionError:
    print("\n>>> На 0 делить нельзя!!! <<<")
except ValueError:
    print("\n>>> Не корректное значение <<<")
