# Assignment 1 - Calculator 

# In this assignment you are going to build a calculator. You are going to take three inputs from the user.  
# ```
# Input 1 - Represents the first number 

# Input 2 - Represents the operand (+ ,  - , * , /) 

# Input 3 - Represents the second number 
# ```


# Based on the operand you are going to perform the math operation and print the result on the terminal. 

# Make sure each math operation is a separate function. 

def calc_input():
    num1 = float(input("Please enter your first number: "))
    operand = input("Please enter your operand (+ , - , * , /): ")
    num2 = float(input("Please enter your second number: "))
    if operand == "+":
        add(num1, num2, operand)
    elif operand == "-":
        subtract(num1, num2, operand)
    elif operand == "*":
        multiply(num1, num2, operand)
    elif operand == "/":
        divide(num1, num2, operand)

def add(num1, num2, operand):
    result = num1 + num2
    display(result)

def subtract(num1, num2, operand):
    result = num1 - num2
    display(result)

def multiply(num1, num2, operand):
    result = num1 * num2
    display(result)

def divide(num1, num2, operand):
    result = num1 / num2
    display(result)

def display(result):
    str_result = str(round(result, 2))
    print("Your result is " + str_result)

calc_input()
