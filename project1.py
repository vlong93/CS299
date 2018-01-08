# Author: Vivian Long
# Assignment: Project 1
# Completed:

# User enters initial deposit, interest rate, and number of years
b = int(input("Enter the initial deposit: "))
r = int(input("Enter the interest rate: "))
n = int(input("Enter the number of years: "))

# Calculates total balance based on values entered
balance = b * ((1 + r/100) ** n)

print(balance)

'''
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
'''
