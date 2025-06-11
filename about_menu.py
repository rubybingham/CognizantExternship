import turtle
from turtle import *
#display menu
def display_menu():
    print("Menu: ")
    print("1. Calculate the factorial of a number.")
    print("2. Find the nth Fibonacci number.")
    print("3. Draw a recursive fractal pattern.")
    print("4. Exit")
# define factorial function
def factorial(n):
    if n ==1:
        return 1
    else:
        return n * factorial(n - 1)
# define Fibonacci function
def Fibonacci(n):
    if n <= 0:
        return "Invalid input. Integer should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (Fibonacci(n - 1) + Fibonacci(n - 2))
# draw a fractal pattern
def draw_tree():
    speed('fastest')
    rt(-90)
    y(80, 7)
def y(sz, level):
    angle = 30
    if level > 0:
        colormode(255)
        pencolor(0, 255//level, 0)
        fd(sz)
        rt(angle)
        y(0.8 * sz, level - 1)
        pencolor(0, 255 // level, 0)
        lt(2 * angle)
        y(0.8 * sz, level - 1)
        pencolor(0, 255 // level, 0)
        rt(angle)
        fd(-sz)

print("Welcome to the Recursive Artistry Program!")
while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        num = int(input("Enter a positive integer: "))
        if num > 0 :
            fact = factorial(num)
            print(f"The factorial of {num} is {fact}.")
        else:
            print("Incorrect input.")
    elif choice == "2":
        num = int(input("Enter a positive integer:"))
        fib = Fibonacci(num)
        print(f"The {num}th Fibonacci number is {fib}.")
    elif choice == "3":
        print("Drawing fractal tree.")
        draw_tree()
        display_menu()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")