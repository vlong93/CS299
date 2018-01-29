# Author: Vivian Long
# Assignment: Lab 4
# Completed: 1/28/2018

import sys
import random

print("Welcome to California SuperLotto!")

invalid_bills = 1
bills = int(input("Please enter bills to start ($1, $2, $5, $10, $20 allowed): "))
while bills != 1 and bills != 2 and bills != 5 and bills != 10 and bills != 20:
    if invalid_bills < 3:
        print("Invalid number of bills. Please re-enter bills: ")
        bills = int(input())
        invalid_bills += 1
    else:
        sys.exit(0)

invalid_tickets = 1
tickets = int(input("How many ticket would you like to purchase? "))
while tickets > bills:
    if invalid_tickets < 3:
        print("Sorry, not enough money. Please re-enter the number of tickets to be purchased: ")
        tickets = int(input())
        invalid_tickets += 1
    else:
        sys.exit(0)

print("Here are your", tickets, "tickets: ")
for i in range(1, tickets + 1):
    print("#" + str(i) + ": \t", random.randint(1, 47), random.randint(1, 47),
          random.randint(1, 47), random.randint(1, 47),"\t", random.randint(0, 27))

change = bills - tickets
print("Your change is $" + str(change))
print("Thank you for your support to Cal Lottery!")

'''
Test 1:
=========== RESTART: /Users/vlong/Documents/project/CS299/lab4.py ===========
Welcome to California SuperLotto!
Please enter bills to start ($1, $2, $5, $10, $20 allowed): 9
Invalid number of bills. Please re-enter bills: 
8
Invalid number of bills. Please re-enter bills: 
7
>>>

Test 2:
=========== RESTART: /Users/vlong/Documents/project/CS299/lab4.py ===========
Welcome to California SuperLotto!
Please enter bills to start ($1, $2, $5, $10, $20 allowed): 5
How many ticket would you like to purchase? 6
Sorry, not enough money. Please re-enter the number of tickets to be purchased: 
7
Sorry, not enough money. Please re-enter the number of tickets to be purchased: 
4
Here are your 4 tickets: 
#1: 	 1 32 11 1 	 1
#2: 	 21 38 24 26 	 13
#3: 	 24 39 4 26 	 11
#4: 	 35 29 40 8 	 9
Your change is $1
Thank you for your support to Cal Lottery!
>>>

Test 3:
=========== RESTART: /Users/vlong/Documents/project/CS299/lab4.py ===========
Welcome to California SuperLotto!
Please enter bills to start ($1, $2, $5, $10, $20 allowed): 10
How many ticket would you like to purchase? 6
Here are your 6 tickets: 
#1: 	 47 5 30 37 	 15
#2: 	 46 4 33 8 	 3
#3: 	 5 21 13 14 	 6
#4: 	 35 45 6 46 	 10
#5: 	 20 8 16 6 	 10
#6: 	 7 47 22 14 	 8
Your change is $4
Thank you for your support to Cal Lottery!
>>> 

'''
