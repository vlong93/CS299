# Author: Vivian Long
# Assignment: Lab 3
# Completed: 1/12/2018

from math import sqrt

# User enters the a, b, and c values of quadratic formula
a = int(input("Enter a of ax^2 + bx + c = 0: "))
b = int(input("Enter b of ax^2 + bx + c = 0: "))
c = int(input("Enter c of ax^2 + bx + c = 0: "))

if a == 0:
    print("Not a quadratic equation")

# Calculates the two answers of the quadratic formula based on values entered

root1 = (-1 * b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
if b ** 2 - 4 * a * c < 0:
    root1 = 
root2 = (-1 * b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
if b ** 2 - 4 * a * c < 0:
    root2 = null

print("Answer 1:", root1)
print("Answer 2:", root2)
