# WEEK 3

## 1. Functions and Scope

### Exercise 1: Functions in Python 

#### Task 1: Create a function called greet_friends. The function should take a list of names as a parameter and print a greeting for each name in the list. The greeting should be "Hello " followed by the name. For example, if the list contains the names "John", "Jane" and "Jack", the output should be as follows:

# Hello John!
# Hello Jane!
# Hello Jack!

# Note: You can use the for loop syntax to iterate over the list of names and use the following list as a starting point:

print("Hellow World")
def greet_user():
    print("Hello!")
greet_user()

def greet_user(name):
    print(f"Hello {name}!")
greet_user("John")

def greet_user(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")
greet_user("John", "smith")
greet_user(last_name="smith", first_name="John")

def greet_user(first_name, last_name, university="UWS"):
    print(f"Hello {first_name} {last_name} from {university}!")
greet_user("John", "Smith") # default UWS
greet_user("John", "Smith", "UWS London")# wzplixiT argument
# or
greet_user("John", "Smith", university="UWS London")




friend_list = ["John", "Jane", "Jack"]
# fucntion code goes here
def greet_friends(names):
    for name in names:
        print(f"Hello {name}!")
greet_friends(friend_list)

def add_numbers(num1, num2):
    return num1 + num2
def add_numbers(num1, num2):
    result = num1 + num2
    return result
result = add_numbers(5, 10)
print(result)
def add_and_multiply_numbers(num1, num2):
    return num1 + num2, num1 * num2
def add_and_multiply_numbers(num1, num2):
    sum = num1 + num2
    product = num1 * num2
    return sum, product
sum, product = add_and_multiply_numbers(5, 10)
print(sum)
print(product)


#### Task 2: Task Tax Calculation: 
    # 1.Define a function called calculate_tax that takes two arguments: income and tax_rate. 
    # 2.Inside the function, calculate the tax amount by multiplying income by tax_rate. 
    # 3.Return the tax amount as the result. 
    # 4.Call the calculate_tax function with an income of 50,000£ and a tax rate of 0.2 and print the calculated tax. 
    # 5.Try using different incomes and tax rates in this function. 

def calculate_tax(income, tax_rate):
    tax_amount= income * tax_rate
    return tax_amount
calc_tax = calculate_tax(50000, 0.2)
print(f"The calculated tax is: {calc_tax}$")

def compound_interest(principal, duration, interest_rate):
    if (interest_rate < 0 or interest_rate > 1):
        print("please enter a decimal number between 0 and 1")
        return None
    if(duration < 0):
        print("please enter a positive number of years")
        return None
    for year in range(1, duration + 1):
        # Calculate the total amount of money earned by the investment for each year
        yearly_amount = principal * (1 + interest_rate) **year
        print (f"The total amount of money earned by the investment in the {year} year is {yearly_amount}$")
        # Return the final investment value as an integer 
        
    #return {"yearly_amount": yearly_amount, "duration": duration}
    #return int(yearly_amount)
    return [duration, int(yearly_amount)]


# Testing the compound_interest function

result=compound_interest(1000, 5, 0.03)
print(result)
print (f"The final investment value after {result[0]} years is: {result[1]}$")
print(result)
print (f"The final investment value is: {result}")


#assert compound_interest(1000,5,0.03)["yearly_amount"]== 1159

assert compound_interest(1000,5,0.03)[1] == 1159

print("Hello, World!")

print("Hello World!")
favourite_fruit = "Apple"
print("My favourite fruit is", favourite_fruit)

number1 = "5" 
number2 = 3
result = number1 + number2
print("The sum is:", result)
fruits = ["apple", "banana", "cherry"]
print(fruits[3])

# Index Error: 
#Correct the index error by accessing the second element (index 1) of the list and printing it. 

fruits = ["apple", "banana", "cherry"]
print(fruits[3])


fruits = ["apple", "banana", "cherry"]
print(fruits[2]) 
# Accessing the third element with index 2 of the list not 3


# Indentation Error: 
# Fix the indentation error so the code correctly prints

time = 11
if time <12:
    print("Good morning!")

time = 11
if time < 12:
    print("Good morning!")
    





