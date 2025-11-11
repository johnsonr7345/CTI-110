# Radney Johnson
# 11/10/2025
# P1HW2
# this program calculates and displays travel expenses

print("---------Travel expense---------")
print()


Budget = input("Enter budget: ")
Destination = input("Enter the travel destination: ")
Fuel = input ("How much do you think you will spend on fuel? ")
Accommodation_hotel = input ("How much would you need for accommadation/hotel ?")
Food = input ("Last, what is the amount you need for food ? ")

# calculate addition and subtraction
print("---------Travel Expenses---------")
print()

num1 =int(input("Enter an integer to sub:"))
num2 =int(input("Enter an integer to add: "))
num3 =int(input("Enter an integer to add: "))
num4 =int(input("Enter an integer to add: "))

sum_result = num2 + num3 + num4 
finial_result = sum_result - num1

print(Fuel, "+", Accommodation_hotel, "+", Food, "-", Budget,"is equal to", finial_result, "!!")