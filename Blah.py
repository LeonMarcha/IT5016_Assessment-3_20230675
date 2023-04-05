# 1. Write a program that displays a welcome message.
# 2. Write a program that displays the result of adding 2 integers.
#    The integers must be defined in the add_numbers( ) function.
#    After that displays the result of subtracting 2 integers.
#    The integers must be defined in the sub_numbers( ) function.
# 3. Write a program using function to expect 2 arguments your first name and
#    last name, and gets 2 arguments:
# 4. Write a program that stores an integer value x and a string of value y
#    (you can choose these values).
#    The program must use a method that displays the y text, x number of times.
# 5. Write a Python function to sum all the numbers in a list. Sample List: (2, 9, 3, 1, 5)
# 6. Write a Python function to multiply all the numbers in a list.
#    Sample List: (6, 2, 7, 8, 4)

print("Welcome")


def add_numbers(first_int, second_int):
    return first_int + second_int


def sub_numbers(first_int, second_int):
    return first_int - second_int


first_int = int(input("Enter first value:"))
second_int = int(input("Enter second value:"))
function = input("Enter 'sub' to subtract, 'add' to perform an addition:")

A_result = add_numbers(first_int, second_int)
S_result = sub_numbers(first_int, second_int)

if function.lower() == "sub":
    print("The sum of these values is:", S_result)
elif function.lower() == "add":
    print("The sum of these values is:", A_result)
else:
    print("Invalid request.")

