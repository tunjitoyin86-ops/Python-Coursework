##Exercise 1: Comparisons and conditionals
# == Equal to
# != Not Equal to
# > Greater than
# < Less than
# >= Greater than or Equals to
# <= Less than or Equals to

x = 7
y = 3
print(x == y)
# returns False because 7 is not equal to 3

x = 6
y = 6
print(x != y)
# returns False because 6 is equal to 6

x = 4
y = 8
print(x > y)
# returns False because 4 is greater than 8

x = 7
y = 3
print(x < y)
# returns False because 7 is not less than 3

x = 3
y = 5
print(x >= y)
# returns False because  is not greater than or equal to 3

x = 9
y = 3
print(x <= y)
# returns False because 9 is not less than or equal to 3

##Exercise 2: Logical Operators
#The and operator returns True if both operands are True
age = 27
print(age > 20 and age < 25)

#The or operator returns True if at least one operand is True
age = 27
print(age > 20 or age < 25)

#The not-operator returns True if the operand is False and vice versa.
age = 27
print(not(age > 20 or age > 25))

##Excercise 3: if Conditionals
age = 19
age_group = "child"
if age > 18:
    age_group = "adult"
    print(f"The age group is {age_group}")
# checking the age of the user
age_group = "child"
if (age <18):
    age_group = "child"
    print(f"you are {age} years old, youre and adult {age_group} you can vote")
else:
    print(f"you are a child, youre {age_group}, wait till youre 18.")

##Excercise 4: if - else conditionals
# wind speed above 15
wind_speed = 15
if wind_speed > 15:
    print("The wind speed is low. its a clam day")
else: 
    print("The wind speed is high. its a windy day")

# wind speed below 15
wind_speed = 15
if wind_speed > 15:
    print("The wind speed is high. its a windy day")
else:
    print("The wind speed is low. its a calm day")

##Excercise 5: if – elif - else Conditionals
# Task compare Temperature
temperature_1 = 20
temperature_2 = 20
if temperature_1 == temperature_2:
    print("Yes, the temparature are the same")
else:
    print("No, the temparature are not the same")

## Python List:
#Excercise 1: creating list
City_list = ["Glasgow", "London", "Edinburgh"]

#Excercise 2: Accessing a list
#print the third item in the list:
City_list = ["Glasgow", "London", "Edinburgh"]
last_item = City_list[-1]
print(f" the third item in the list is {last_item}")
#print the last two item in the list:
City_list = ["Glasgow", "London", "Edinburgh"]
last_two_item = City_list[1:3]
print(f"the last two item in the list is {last_two_item}")

#Excercise 3: Modifying a list
#Adding Mancheste to the end of the list
City_list = ["Glasgow", "London", "Edinburgh"]
City_list.append("Manchester")
print(f"updating the city list{City_list}.")
#Changing change the second item in theity_list list to "Birmingham".
City_list[1] = "Birmingham"
print(f"updating the city list{City_list}.")

#Exercise 4: summary Task
#creating list of colours
colours = ["Red", "Green", "Yellow"]
print(f"the colour's list is represented as {colours}.")
#Accessing second element of the colours list
second_colour = colours[1]
print(f"The second colour in the list is {second_colour}.")
#Modifying the first Element to a new colour
colours[0] = "grey"
print(f"updating the colour in the list {colours}.")
#check the lenght of the colours
colours_lenght = len(colours)
print(f"the numbers of the colours in the list is {colours_lenght}.")
#check if "Red" is the colour
if "red" in colours:
    print(f"Red is in the list.")
else:
    print(f"Red is not in the list.")
# using slicing to create a new list named selected_colours
selected_colours = colours[1:3]
print(f"selected colours list is {selected_colours}.")

##Python Loops
#Excercise 2: For loops : create a for loops that print each item in the city_list list.
print("the list contains the following city")
for city in City_list:
    print(city)

#Exercise 3: Loop Keywords: Range, break and continue: Modify the above code to print the numbers 0 through 4, but stop the loop when i is equal to 3
for i in range(5):
    if i == 2:
        break
print(i)
for i in range(5):
    if i == 3:
        break
print(i)







