input_case = input("Выбери тип операции:\n1 +\n2 -\n3 *\n4 /\n")
value_1 = float(input("Введи первое число:"))
value_2 = float(input("Введи второе число:"))
try:
    if input_case == '1':
        result = value_1 + value_2
    elif input_case == '2':
        result = value_1 - value_2
    elif input_case == '3':
        result = value_1 * value_2
    elif input_case == '4':
        try:
            result = value_1 /value_2
        except ZeroDivisionError:
            print("На 0 делить нельзя!!!")
    else:
        print("Неверная операция")
        print(result)
    print(f"= {result}")
except ValueError:
    print("Не корректное значение")
    pass

