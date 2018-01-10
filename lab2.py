# Author: Vivian Long
# Assignment: Lab 2
# Completed: 1/8/2018

# Initial $1000 and the different interest rates
initial = 1000
rate1 = 3
rate2 = 5
rate3 = 12

# Problem 1
# Calculates the total balance after 18 years of compounded interest
total1 = initial * (1 + (rate1/100)) ** 18
total2 = initial * (1 + (rate2/100)) ** 18
total3 = initial * (1 + (rate3/100)) ** 18

print("The total amount available after 18 years at 3% interest is $" + str(total1))
print("The total amount available after 18 years at 5% interest is $" + str(total2))
print("The total amount available after 18 years at 12% interest is $" + str(total3))

'''
Output:
The total amount available after 18 years at 3% interest is $1702.4330612399046
The total amount available after 18 years at 5% interest is $2406.619233691086
The total amount available after 18 years at 12% interest is $7689.965795021485
'''

# Problem 2
from math import sqrt

# User enters the lengths of the triangle's legs
leg1 = float(input("Enter length of leg 1: "))
leg2 = float(input("Enter length of leg 2: "))

# Calculates the hypotenuse based on lengths entered
hypot = sqrt(leg1 ** 2 + leg2 ** 2)

print("The hypotenuse is", hypot)

'''
Output of Run 1:
Enter length of leg 1: 5
Enter length of leg 2: 6
The hypotenuse is 7.810249675906654

Output of Run 2:
Enter length of leg 1: 7
Enter length of leg 2: 10
The hypotenuse is 12.206555615733702
'''
