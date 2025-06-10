# Task 1 working with lists
# create fruit list
fruit_list = ["apple", "banana,", "peach", "strawberry", "blueberry"]
print("Original list:", fruit_list)

# append fruit
fruit_list.append("kumquat")
print("After adding a fruit:",fruit_list)

# remove a fruit
fruit_list.remove("peach")
print("After removing a fruit", fruit_list)
# reverse list
print("Reversed list:", fruit_list[::-1])

# Task 2 Exploring dictionaries
about_me = {"name": "Ruby", "age": 31, "city": "Farmington, NM"}
# add favorite color
about_me["favorite color"] = "blue"
# replace city
about_me["city"] = "Buffalo, NY"

# print dictionary
for key, value in about_me.items():
    print(f"{key}: {value}")

# Task 3 using tuples
my_tuple = ("Mulan Rogue", "Somebody to love", "Catching fire")
print(my_tuple)

# length
print("Length of tuple:", len(my_tuple))

# change an element (impossible and will through an error)
my_tuple[0] = "Star wars"
print(my_tuple)


