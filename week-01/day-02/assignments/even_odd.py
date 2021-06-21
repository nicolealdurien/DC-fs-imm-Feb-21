# Assignment 2 - Even Odd 

# Write an app which asks the user for an input and then displays a message indicating whether the number is even or odd. 



def even_odd(num):
    if num % 2 == 0:
        print("Your number is even.")
    else: 
        print("Your number is odd.")

def even_odd_input():
    num = int(input("Please enter an integer: "))
    even_odd(num)



even_odd_input()