print("Task 1")
name = "Ruby"
age = 30
height = 5.1
print("Hello, my name is ", name, ". I'm ", age, " years old and I am ", height, " feet short.")

print("Task 2")
num1 = 15
num2 = 3
print("The sum of 15 and 3 is ", num1 + num2)
print("The difference of 15 and 3 is ", num1 - num2)
print("The product of 15 and 3 is", num1 * num2)
print("The quotient of 15 and 3 is", num1 / num2)

print("Task 3")
print("Enter a number.")
user_num = input()
user_num = int(user_num)
if user_num > 0:
    print("This number is positive. Awesome!")
elif user_num < 0:
    print("This number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")