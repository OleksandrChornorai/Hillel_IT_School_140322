while True:
    input_case = input("Выбери тип операции:\n1 +\n2 -\n3 *\n4 /\n")
    try:
        value_1 = float(input("Введи первое число:"))
        value_2 = float(input("Введи второе число:"))
        if input_case == '1':
            result = (value_1 + value_2)
            print(f"= {result}")
        elif input_case == '2':
            result = (value_1 - value_2)
            print(f"= {result}")
        elif input_case == '3':
            result = (value_1 * value_2)
            print(f"= {result}")
        elif input_case == '4':
            try:
                result = (value_1 / value_2)
                print(f"= {result}")
            except ZeroDivisionError:
                print("На 0 делить нельзя!!!")
        else:
            print("Неверная операция")
    except ValueError:
        print("Не корректное значение")
