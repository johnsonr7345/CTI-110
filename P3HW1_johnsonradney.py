# radney Johnson
# 11/21/2025
#P3HW1
#Take six number grades, determines the average, and displays the letter grade for that average.

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum, and average for grades
low = min(grades)
high = max(grades)
total_sum = sum(grades)
avg = total_sum / len(grades)

# Display calculated stats
print(f"Lowest grade: {low}")
print(f"Highest grade: {high}")
print(f"Sum of grades: {total_sum}")
print(f"Average grade: {avg:.2f}")


print("\n------------Results------------")

# Determine letter grade for average
if avg >= 90:
    print('Your letter grade is: A')
elif avg >= 80:
    print('Your letter grade is: B')
elif avg >= 70:
    print('Your letter grade is: C')
elif avg >= 60:
    print('Your letter grade is: D')
else:
    print('Your letter grade is: F')

