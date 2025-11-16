#Radney Johnson
#11/11/2024
#P2LAB2
#Using dictionaries

cars = {'Camaro':18.21, 'Prius':52.36, 'Model S' :110, 'Silverado' :26}

#Get keys from dict
cars_keys = cars.keys ()

print(cars_keys)

print(*cars_keys, sep = " , ")

#Get a car from user
car_name = input("Enter a car: ")

#Get mpg for the given car
car_mpg = cars[car_name]

print(f"The {car_name} get {car_mpg} miles per gallon. ")

#Get miles from user
miles_driver = float (input(f"How many miles will you drive the {car_name}?"))

#Calculate
gallons_needed = miles_driver/car_mpg

#display results
print(f"{gallons_needed:.2f} gallon(s) are needed to drive the {car_name} [miles_driven] miles")
