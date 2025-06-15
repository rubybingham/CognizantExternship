# Task 1

try:
    user_num = int(input("Enter a number to divide 100 by: "))
    print(100/user_num)
except ZeroDivisionError:
    print("You can't divide by zero.")
except ValueError:
    print("Please enter a valid number.")

# Task 2
# create list for IndexError
fruit_list = ["apple", "banana,", "peach", "strawberry", "blueberry"]
# try to access an index that doesn't exist
try:
    value = fruit_list[9] # throws an IndexError
except IndexError:
    # prevents program from closing due to the error.
    print("IndexError occurred. List index out of range.")
# create dictionary for KeyError
about_me = {"name": "Ruby", "age": 31, "city": "Farmington, NM"}
# try to access key that doesn't exist
try:
    bad_key = about_me["color"] # thorws KeyError
except KeyError:
    # prevents program from closing due to the error.
    print("KeyError occurred. Key not in dictionary.")
# TypeError adding a string and integer
try:
    answer = "no" + 2 # throws a KeyError
except TypeError:
    # prevents program from closing due to the error.
    print("TypeError has occurred. Unsupported operand types.")

# Task 3
try:
    numerator = int(input("Enter a number: "))
    denominator = int(input("Enter another number to divide by: "))
    answer = numerator / denominator
except ZeroDivisionError:
    print("You can't divide by zero.")
except ValueError:
    print("Please enter a valid number.")
else:
    print(f'{numerator} divide by {denominator} equals {answer}')
finally:
    print("Thanks for using the program.")