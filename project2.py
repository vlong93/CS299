# Author: Vivian Long
# Assignment: Project 2
# Completed:

# Problem 1

import sys

# Asks user for metric or English system
system = str(input("Would you like to use the metric or English system? Enter 'm' for metric or 'e' for English: "))

# User chooses metric
if system == 'm':
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))

    bmi = round(weight / (height ** 2), 2)

# User choose English
elif system == 'e':
    weight = float(input("Enter weight in lbs: "))
    height = float(input("Enter height in inches: "))

    bmi = round(weight / (height ** 2) * 703, 2)

else:
    print("Please enter a valid response.")
    sys.exit(0)

print("BMI:", bmi)

if bmi <= 24:
    print("Your BMI is normal.")
elif 25 <= bmi <= 29:
    print("Your BMI indicates you are overweight.")
elif 30 <= bmi <= 39:
    print("Your BMI indicates you are obese.")
elif bmi >= 40:
    print("Your BMI indicates you are extremely obese.")
