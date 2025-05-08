# string slicing and indexing
print("Task 1")
string = "Python is amazing!"
first_word = string[0:6]
amazing = string[10:17]
backwards = string[::-1]
print("First word: ", first_word)
print("Amazing part: ", amazing)
print("Reversed string: ", backwards)

# string methods
print("Task 2")
string = " hello, python world! "
stripped = string.strip()
capped = stripped.capitalize()
universe = string.replace("world","universe")
uppercase = string.upper()
print(string)
print(stripped)
print(capped)
print(universe)
print(uppercase)

# check for palindromes
print("Task 3")
user_string = str(input("Please enter a word: "))
backwards = user_string[::-1]
if user_string == backwards:
    print(user_string, "is a palindrome!")
else:
    print(user_string, "is not a palindrome.")
