# Author: Vivian Long
# Assignment: Project 1
# Completed:
'''
# Problem #1
# User enters initial deposit, interest rate, and number of years
b = int(input("Enter the initial deposit: "))
r = int(input("Enter the interest rate: "))
n = int(input("Enter the number of years: "))

# Calculates total balance based on values entered
balance = b * ((1 + r/100) ** n)

print(balance)


================ RESTART: /Users/vlong/Documents/project1.py ================
Enter the initial deposit: 1000
Enter the interest rate: 0
Enter the number of years: 18
1000.0
>>> 
================ RESTART: /Users/vlong/Documents/project1.py ================
Enter the initial deposit: 1000
Enter the interest rate: 3
Enter the number of years: 18
1702.4330612399046
>>> 
================ RESTART: /Users/vlong/Documents/project1.py ================
Enter the initial deposit: 5000
Enter the interest rate: 5
Enter the number of years: 10
8144.47313388721
>>> 
================ RESTART: /Users/vlong/Documents/project1.py ================
Enter the initial deposit: 5000
Enter the interest rate: 10
Enter the number of years: 10
12968.712300500012
>>>
================ RESTART: /Users/vlong/Documents/project1.py ================
Enter the initial deposit: 10000
Enter the interest rate: 2
Enter the number of years: 8
11716.593810022658
>>> 


# Problem #2
from math import sqrt

# User enters the a, b, and c values of quadratic formula
a = int(input("Enter a of ax^2 + bx + c = 0: "))
b = int(input("Enter b of ax^2 + bx + c = 0: "))
c = int(input("Enter c of ax^2 + bx + c = 0: "))

# Calculates the two answers of the quadratic formula based on values entered
root1 = (-1 * b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
root2 = (-1 * b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)

print("Answer 1:", root1)
print("Answer 2:", root2)


================ RESTART: /Users/vlong/Documents/project1.py ================
Enter a of ax^2 + bx + c = 0: 1
Enter b of ax^2 + bx + c = 0: 4
Enter c of ax^2 + bx + c = 0: 4
Answer 1: -2.0
Answer 2: -2.0
>>> 
================ RESTART: /Users/vlong/Documents/project1.py ================
Enter a of ax^2 + bx + c = 0: 4
Enter b of ax^2 + bx + c = 0: -4
Enter c of ax^2 + bx + c = 0: 1
Answer 1: 0.5
Answer 2: 0.5
>>> 
================ RESTART: /Users/vlong/Documents/project1.py ================
Enter a of ax^2 + bx + c = 0: 3
Enter b of ax^2 + bx + c = 0: 7
Enter c of ax^2 + bx + c = 0: 2
Answer 1: -0.3333333333333333
Answer 2: -2.0
>>>
'''


# Problem #3

