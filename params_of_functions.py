# Task 1
def greet_user(name):
    print(f"Hello, {name}!")

def add_numbers(a, b):
    return(a + b)
# output
user_name = input("Enter your name: ")
greet_user(user_name)
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
answer = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is {answer}.")

# Task 2
def describe_pet(pet_name, animal_type = "dog"):
    animal_type = animal_type.lower()
    print(f"I have a {animal_type} named {pet_name}.")

animal_type = input("What type of pet do you have? ")
pet_name = input("What is your pet's name? ")

describe_pet(pet_name, animal_type)

# Task 3
def make_sandwich(*ingredients):
    print(f"Making a sandwich with the following ingredients: ")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwich("lettuce", "tomato", "bacon")

# Task 4

def factorial(n):
    if n ==1:
        return 1
    else:
        return n * factorial(n - 1)
def Fibonacci(n):
    if n <= 0:
        return "Invalid input. n should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (Fibonacci(n - 1) + Fibonacci(n - 2))

# test factorial

n = 5
print("Factorial of 5 is ", factorial(n))

# test fibonacci

n = 10
print("The 10th Fibonacci number is ", Fibonacci(n))