# Exercise 1: tuple

# Create a tuple
fruits = ("apple", "banana", "cherry")

# Print the whole tuple
print("My favorite fruits:", fruits)

# Print the second item (index 1)
print("Second fruit:", fruits[1])

# Loop through the tuple
for fruit in fruits:
    print("Fruit:", fruit)


# Exercise 2: Set

# Create a set
fruits = {"apple", "banana", "orange"}

# Add a new fruit
fruits.add("mango")

# Step 4: Remove a fruit
fruits.remove("banana")

# Step 5: Loop through the set
for fruit in fruits:
    print("Fruit:", fruit)

# Exercise 3: Dictionary

# Create a dictionary
fruits = {
    "apple": "red",
    "banana": "yellow",
    "orange": "orange"
}

# Add a new fruit
fruits["mango"] = "green"

# Change the color of an existing fruit
fruits["apple"] = "green"

# Remove a fruit
del fruits["banana"]

# Loop through and print
for fruit, color in fruits.items():
    print(f"{fruit.capitalize()} is {color}")


# Task 2: sets

set1 = {"Tom", "Jerry", "Hewey", "Dewey", "Louie"}
set2 = {"Tom", "Garfield", "Snoopy", "Hewey", "Dewey"}

common_names = set1.intersection(set2)
print(common_names)


# Task 3: Dictionaries

def histogram(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

# Test the function
my_list = [1, 2, 3, 1, 2, 3, 4]
assert histogram(my_list) == {1: 2, 2: 2, 3: 2, 4: 1}