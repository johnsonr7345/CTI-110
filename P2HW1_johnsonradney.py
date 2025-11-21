# Radney Johnson
# 11/16/2025
# P2HW1
# this program calculates and displays travel expenses

print("---------Travel expense---------")


# display results

# User inputs
location = input("Enter your travel destination: ")
budget = float(input("Enter your budget: "))
travel_cost = float(input("How much do you think you will spend on gas? "))
hotel_cost = float(input("Approximately, how much will you need for hotel? "))
food_cost = float(input("Last, how much will you need for food? "))

# Calculations

remaining_balance = budget - (travel_cost + hotel_cost + food_cost)

# Display/ output

print("\n------------Travel Expenses------------")

print(f"{'Location:':15} {location}")
print(f"{'Initial Budget:':15} ${budget:,.2f}")
print(f"{'Travel_cost:':15} ${travel_cost:,.2f}")
print(f"{'Hotel_cost:':15} ${hotel_cost:,.2f}")
print(f"{'Food_cost:':15} ${food_cost:,.2f}")

print("\n--------remaining_balance--------")

print(f"{'Remaining_balance:':15} {remaining_balance:,.2f}") 






