
# Assignment 3: Write a Fizz Buzz application. 

# Take input from the user. If the input is divisible by 3 then print **"Fizz"**, if the input it divisible by 5 then print **"Buzz"**. If the input is divisible by 3 and 5 then print **"Fizz Buzz"**. 

def fizz_buzz_input():
    num = int(input("Please enter an integer: "))
    fizz_buzz(num)

def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print("Your number is not divisible by 3 or 5.")

fizz_buzz_input()