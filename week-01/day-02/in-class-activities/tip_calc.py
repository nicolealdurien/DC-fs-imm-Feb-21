# Tip Calculator

# In this optional assignment, you are going to ask the user for the two inputs as shown below:

# 1) Enter the total amount

# 2) Enter the tip percentage amount

# After the user has entered both inputs, the application calculates the tip amount and displays it to the user.

total = float(input("Please enter your total: $"))
tip_percent = float(input("Please enter your desired tip percentage as a whole number: "))
tip = (tip_percent/100) * total
str_tip = str(round(tip, 2))
print("Your tip amount is $" + str_tip)
