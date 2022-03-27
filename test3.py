value = 123
my_str = str(value) if value < 200 else str(value % 10)
print(my_str)

value = 123
my_str = str(value) if value > 200 else str(value % 10)
print(my_str)

value = 321
my_str = str(value) if value > 200 else str(value % 10)
print(my_str)

value = 321
my_str = str(value) if value < 200 else str(value % 10)
print(my_str)

value = 123
my_str = str(value) if value > 200 else str(value)[::-1]
print(my_str)

value = "123456789"
my_str = value if len(value) < 5 else value[::-1]
print(my_str)

value = "123456789"
my_str = value if len(value) < 5 else value[::2]
print(my_str)

value = "123456789"
my_str = value if len(value) > 5 else value[::2]
print(my_str[::-1])

value = "123456789"
my_str = value if len(value) < 5 else value[::2]
print(my_str[::-1])

value = "123456789"
my_str = value if len(value) < 5 else value[1::2]
print(my_str[::-1])