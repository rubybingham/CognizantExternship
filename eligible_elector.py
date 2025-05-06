# get age from user
age = int(input("How old are you? "))
# verify 18 or older
if age >= 18:
    print("You are eligible to vote! Make your voice heard!")
# if not 18 or older, calculate time left until 18 and output
else:
    print("You can't vote yet, but you can in ", 18 - age, " years!")
