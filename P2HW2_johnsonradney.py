# Radney Johnson
#11/16/2025
#P2HW2
# this program displays each grade for every module 

print("---------Grade for each Module---------")

m1 = float(input("Enter grade for Module 1: "))
m2 = float(input("Enter grade for Module 2: "))
m3 = float(input("Enter grade for Module 3: "))
m4 = float(input("Enter grade for Module 4: "))
m5 = float(input("Enter grade for Module 5: "))
m6 = float(input("Enter grade for Module 6: "))



grade_list = [m1, m2, m3, m4, m5, m6]


# Calculations
lowest = min(grade_list)
highest = max(grade_list)
total = sum(grade_list)
average = total / len(grade_list)

print("\n------------Results------------")

print(f"{'Lowest Grade:':15} {lowest}")
print(f"{'Highest Grade:':15} {highest}")
print(f"{'Total Grade:' } {total}")
print(f"{'Average Grade:'} {average} ")
