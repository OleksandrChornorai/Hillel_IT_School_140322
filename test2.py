my_value_1 = 2
my_value_2 = "4"
my_value_2 = int(my_value_2)
result = my_value_1 * my_value_2
print(result)

my_value_1 = 2
my_value_2 = "4"
my_value_1 = str(my_value_1)
my_value_2 = int(my_value_2)
result = my_value_1 * my_value_2
print(result)

my_value_1 = 2
my_value_2 = "4"
my_value_1 = str(my_value_1)
result = my_value_1 + my_value_2
print(result)

my_value = 12
my_bool = my_value % 3 #!=0
print(my_bool)

www = "www.google.com"
if "com" in www:
    print("com in www")
else:
    print("com not in www")

www = "www.command_and_conquer.net"
if "com" in www:
    print("com in www")
else:
    print("com not in www")

www = "www.conquer_and_command.net"
if "com" in www:
    print("com in www")
else:
    print("com not in www")

www = "www.conquer_and_command.net"
if ".com" in www:
    print("com in www")
else:
    print("com not in www")