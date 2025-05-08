# password checker

user_pass = str(input("Please enter a password: "))
length = len(user_pass)
upper = any(char.isupper() for char in user_pass)
lower = any(char.islower() for char in user_pass)
digit = any(char.isdigit() for char in user_pass)
pass_strength = 10
special = False
for char in user_pass:
    if char in "!@#$%^&*/<>":
        special = True
        break
is_strong = True
if length < 8:
    print("Your password is too short.")
    is_strong = False
    pass_strength = 0
else:
    if not upper:
        print("Your password needs as least one uppercase letter.")
        is_strong = False
        pass_strength -= 2
    if not lower:
        print("Your password needs as least one lowercase letter.")
        is_strong = False
        pass_strength -= 2
    if not digit:
        print("Your password needs as least one digit.")
        is_strong = False
        pass_strength -= 2
    if not special:
        print("Your password needs at least one special character.")
        is_strong = False
        pass_strength -= 2
    if is_strong:
        print("Your password is strong!")
print("Password strength: ", pass_strength, "/10")