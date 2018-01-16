# Author: Vivian Long
# Assignment: Lab 3
# Completed: 1/12/2018

import sys
from math import sqrt

# User enters the a, b, and c values of quadratic formula
a = int(input("Enter a of ax^2 + bx + c = 0: "))
b = int(input("Enter b of ax^2 + bx + c = 0: "))
c = int(input("Enter c of ax^2 + bx + c = 0: "))

# If a = 0, the equation is not quadratic
if a == 0:
    print("Not a quadratic equation")
    sys.exit(0)

# Calculates the two answers of the quadratic formula based on values entered
if b ** 2 - 4 * a * c < 0:
    print("No real solutions")
    sys.exit(0)
else:
    root1 = (-1 * b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    root2 = (-1 * b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)

    print("Answer 1:", root1)
    print("Answer 2:", root2)

'''
=========== RESTART: /Users/vlong/Documents/project/CS299/lab3.py ===========
Enter a of ax^2 + bx + c = 0: 2
Enter b of ax^2 + bx + c = 0: -1
Enter c of ax^2 + bx + c = 0: -1
Answer 1: 1.0
Answer 2: -0.5

=========== RESTART: /Users/vlong/Documents/project/CS299/lab3.py ===========
Enter a of ax^2 + bx + c = 0: 3
Enter b of ax^2 + bx + c = 0: 11
Enter c of ax^2 + bx + c = 0: 4
Answer 1: -0.4093327091137449
Answer 2: -3.257333957552922

=========== RESTART: /Users/vlong/Documents/project/CS299/lab3.py ===========
Enter a of ax^2 + bx + c = 0: 3
Enter b of ax^2 + bx + c = 0: 11
Enter c of ax^2 + bx + c = 0: 0
Answer 1: 0.0
Answer 2: -3.6666666666666665

=========== RESTART: /Users/vlong/Documents/project/CS299/lab3.py ===========
Enter a of ax^2 + bx + c = 0: 4
Enter b of ax^2 + bx + c = 0: 0
Enter c of ax^2 + bx + c = 0: -7
Answer 1: 1.3228756555322954
Answer 2: -1.3228756555322954

=========== RESTART: /Users/vlong/Documents/project/CS299/lab3.py ===========
Enter a of ax^2 + bx + c = 0: 1
Enter b of ax^2 + bx + c = 0: 4
Enter c of ax^2 + bx + c = 0: 4
Answer 1: -2.0
Answer 2: -2.0

=========== RESTART: /Users/vlong/Documents/project/CS299/lab3.py ===========
Enter a of ax^2 + bx + c = 0: 0
Enter b of ax^2 + bx + c = 0: 4
Enter c of ax^2 + bx + c = 0: 5
Not a quadratic equation

=========== RESTART: /Users/vlong/Documents/project/CS299/lab3.py ===========
Enter a of ax^2 + bx + c = 0: 1
Enter b of ax^2 + bx + c = 0: 3
Enter c of ax^2 + bx + c = 0: 4
No real solutions
'''
