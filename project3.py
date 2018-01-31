# Author: Vivian Long
# Assignment: Project 3
# Completed:

import sys
from math import sqrt


# Problem 1
print("Fahrenheit (\u00b0F) \t Celsius (\u00b0C) \t Description")  # Header
print('{:>14}'.format("-459.67 \u00b0F"), "\t", '{:>15}'.format("-273.15 \u00b0C"),
      "\t", '{:<30}'.format("absolute zero temperature"))  # Absolute zero
for i in range(-50, 31, 10):
    celc = ((i - 32) * 5) / 9
    print('{:>11}'.format(i), "\u00b0F", "\t", '{:>12}'.format(round(celc, 2)), "\u00b0C")  # -50 to 30 F
print('{:>14}'.format("32 \u00b0F"), "\t", '{:>15}'.format("0 \u00b0C"),
      "\t", '{:<30}'.format("freezing/melting point of water"))  # Freezing point
for i in range(40, 61, 10):
    celc = ((i - 32) * 5) / 9
    print('{:>11}'.format(i), "\u00b0F", "\t", '{:>12}'.format(round(celc, 2)), "\u00b0C")  # 40 to 60 F
print('{:>14}'.format("70 \u00b0F"), "\t", '{:>15}'.format("21.11 \u00b0C"),
      "\t", '{:<30}'.format("room temperature"))  # Room temp
for i in range(80, 91, 10):
    celc = ((i - 32) * 5) / 9
    print('{:>11}'.format(i), "\u00b0F", "\t", '{:>12}'.format(round(celc, 2)), "\u00b0C")  # 80 to 90 F
print('{:>14}'.format("98.6 \u00b0F"), "\t", '{:>15}'.format("37 \u00b0C"),
      "\t", '{:<30}'.format("average body temperature"))  # Avg body temp
for i in range(100, 201, 10):
    celc = ((i - 32) * 5) / 9
    print('{:>11}'.format(i), "\u00b0F", "\t", '{:>12}'.format(round(celc, 2)), "\u00b0C")  # 100 to 200 F
print('{:>14}'.format("212 \u00b0F"), "\t", '{:>15}'.format("100 \u00b0C"),
      "\t", '{:<30}'.format("boiling point of water"))  # Boiling point


# Problem 2
count = 0  # Invalid input counter
ans = "yes"
while ans == "yes" or ans == "y":
    try:
        x0 = float(input("Enter circle 1's center x coordinate: "))
        y0 = float(input("Enter circle 1's center y coordinate: "))
        r0 = float(input("Enter circle 1's radius: "))
        x1 = float(input("Enter circle 2's center x coordinate: "))
        y1 = float(input("Enter circle 2's center y coordinate: "))
        r1 = float(input("Enter circle 2's radius: "))

    except (NameError, ValueError):
        print("Please enter a real number.")
        count += 1
        if count == 3:
            sys.exit(0)

    else:
        d = sqrt(((x1 - x0) ** 2) + ((y1 - y0) ** 2))

        if d > (r0 + r1):
            print("The circles do not intersect and are completely separate.")

        elif d < abs(r0 - r1):
            print("The two circles do not intersect and one is contained within the other.")

        elif d == r0 + r1:
            print("The two circles intersect a single point.")

        elif d == 0 and r0 == r1:
            print("The two circles are coincident.")

        else:
            print("The two circles intersect at two points.")

        ans = input("Would you like to compare two circles again? (yes/no): ").lower()
