# create countdown
print("Task 1")
user_num = int(input("Enter a number: "))

while user_num >= 1:
    print(user_num, end=" ")
    user_num -= 1

print("Blast off!")

# multiplication table
print("Task 2")
user_num = int(input("Enter a number: "))
for i in range(1, 11):
    print(user_num, " x ", i, " = ", user_num * i)

# find the factorial
print("Task 3")
user_num = int(input("Enter a number: "))
factorial = 1
for i in range(1, user_num+1):
    factorial *= i
print("The factorial of ", user_num, " is ", factorial)