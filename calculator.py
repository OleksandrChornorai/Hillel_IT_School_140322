input_case = input("Выбери тип операции:\n1 +\n2 -\n3 *\n4 /\n")
try:
    if input_case == '1':
        value_1 = float(input("Введи первое число:"))
        value_2 = float(input("Введи второе число:"))
        result = (value_1 + value_2)
        print(f"= {result}")
    elif input_case == '2':
        value_1 = float(input("Введи первое число:"))
        value_2 = float(input("Введи второе число:"))
        result = (value_1 - value_2)
        print(f"= {result}")
    elif input_case == '3':
        value_1 = float(input("Введи первое число:"))
        value_2 = float(input("Введи второе число:"))
        result = (value_1 * value_2)
        print(f"= {result}")
    elif input_case == '4':
        value_1 = float(input("Введи первое число:"))
        value_2 = float(input("Введи второе число:"))
        result = (value_1 / value_2)
        print(f"= {result}")
    else:
        print("Неверная операция")
except ZeroDivisionError:
    print("На 0 делить нельзя!!!")
except ValueError:
    print("Не корректное значение")
