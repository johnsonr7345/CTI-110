#Radney Johnson
#11/29/2025
#P4LAB2
#use whole loop and for loop together

run_again = "yes"

while run_again != "no":

    # Ask user for an integer

    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
        # Display multiplication table from 1 to 12
        print(f"Multiplication table for {user_num}:")
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        print("This program does not accept negative values.")

    # Ask user if they want to run the program again
    run_again = input("Do you want to run the program again? (yes/no): ")

#Loop has broken. User entered 'no'
print("Program is ending.....")