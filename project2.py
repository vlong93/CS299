# Author: Vivian Long
# Assignment: Project 2
# Completed: 1/17/2018


# Problem 1

import sys

# Asks user for metric or English system
system = str(input("Would you like to use the metric or English system? Enter 'm' for metric or 'e' for English: "))

# User chooses metric system
if (system == 'm') or (system == 'M'):
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))

    bmi = round(weight / (height ** 2), 2)

# User chooses English system
elif (system == 'e') or (system == 'E'):
    weight = float(input("Enter weight in lbs: "))
    height = float(input("Enter height in inches: "))

    bmi = round(weight / (height ** 2) * 703, 2)

# User enters something else
else:
    print("Please enter a valid response.")
    sys.exit(0)

# Output BMI and appropriate corresponding message
print("BMI:", bmi)

if bmi <= 24:
    print("Your BMI is normal.")
elif 24 < bmi <= 29:
    print("Your BMI indicates you are overweight.")
elif 29 < bmi < 40:
    print("Your BMI indicates you are obese.")
elif bmi > 40 :
    print("Your BMI indicates you are extremely obese.")

'''
Test 1: English, normal BMI
========= RESTART: /Users/vlong/Documents/project/CS299/project2.py =========
Would you like to use the metric or English system? Enter 'm' for metric or 'e' for English: e
Enter weight in lbs: 160
Enter height in inches: 69
BMI: 23.63
Your BMI is normal.

Test 2: English, overweight
========= RESTART: /Users/vlong/Documents/project/CS299/project2.py =========
Would you like to use the metric or English system? Enter 'm' for metric or 'e' for English: e
Enter weight in lbs: 155
Enter height in inches: 65
BMI: 25.79
Your BMI indicates you are overweight.

Test 3: English, obese
========= RESTART: /Users/vlong/Documents/project/CS299/project2.py =========
Would you like to use the metric or English system? Enter 'm' for metric or 'e' for English: E
Enter weight in lbs: 200
Enter height in inches: 67
BMI: 31.32
Your BMI indicates you are obese.

Test 4: English, extreme obesity
========= RESTART: /Users/vlong/Documents/project/CS299/project2.py =========
Would you like to use the metric or English system? Enter 'm' for metric or 'e' for English: E
Enter weight in lbs: 300
Enter height in inches: 65
BMI: 49.92
Your BMI indicates you are extremely obese.

Test 5: Metric, normal
========= RESTART: /Users/vlong/Documents/project/CS299/project2.py =========
Would you like to use the metric or English system? Enter 'm' for metric or 'e' for English: m
Enter weight in kg: 50
Enter height in meters: 1.6
BMI: 19.53
Your BMI is normal.

Test 6: Metric, overweight
========= RESTART: /Users/vlong/Documents/project/CS299/project2.py =========
Would you like to use the metric or English system? Enter 'm' for metric or 'e' for English: m
Enter weight in kg: 65
Enter height in meters: 1.6
BMI: 25.39
Your BMI indicates you are overweight.

Test 7: Metric, obese
========= RESTART: /Users/vlong/Documents/project/CS299/project2.py =========
Would you like to use the metric or English system? Enter 'm' for metric or 'e' for English: M
Enter weight in kg: 80
Enter height in meters: 1.63
BMI: 30.11
Your BMI indicates you are obese.

Test 8: Metric, extreme obesity
========= RESTART: /Users/vlong/Documents/project/CS299/project2.py =========
Would you like to use the metric or English system? Enter 'm' for metric or 'e' for English: m
Enter weight in kg: 103
Enter height in meters: 1.59
BMI: 40.74
Your BMI indicates you are extremely obese.

Test 9: Error due to wrong data format
========= RESTART: /Users/vlong/Documents/project/CS299/project2.py =========
Would you like to use the metric or English system? Enter 'm' for metric or 'e' for English: j
Please enter a valid response.

Test 10: Error due to wrong data values
========= RESTART: /Users/vlong/Documents/project/CS299/project2.py =========
Would you like to use the metric or English system? Enter 'm' for metric or 'e' for English: e
Enter weight in lbs: -10
Enter height in inches: 2
BMI: -1757.5
Your BMI is normal.

Test 11: Error
========= RESTART: /Users/vlong/Documents/project/CS299/project2.py =========
Would you like to use the metric or English system? Enter 'm' for metric or 'e' for English: e
Enter weight in lbs: 145
Enter height in inches: 5'7
Traceback (most recent call last):
  File "/Users/vlong/Documents/project/CS299/project2.py", line 23, in <module>
    height = float(input("Enter height in inches: "))
ValueError: could not convert string to float: "5'7"

Test 12: Error
========= RESTART: /Users/vlong/Documents/project/CS299/project2.py =========
Would you like to use the metric or English system? Enter 'm' for metric or 'e' for English: m
Enter weight in kg: 60
Enter height in meters: 170
BMI: 0.0
Your BMI is normal.
'''




# Problem 2

import random

rps = ["Rock", "Paper", "Scissors"]

# Computer randomly generates string from list
npc = random.choice(rps)

# Asks user for choice
user = str(input("Rock, paper, or scissors? "))

# User chooses rock
if (user == "rock") or (user == "Rock"):
    print("You chose", user)
    print("NPC chose", npc)
    if (npc == "Rock"):                
        print("It's a tie")
    elif (npc == "Paper"):
        print("You lose")
    elif (npc == "Scissors"):
        print("You win!")

# User chooses paper
elif (user == "paper") or (user == "Paper"):
    print("You chose", user)
    print("NPC chose", npc)
    if (npc == "Rock"):                
        print("You win!")
    elif (npc == "Paper"):
        print("It's a tie")
    elif (npc == "Scissors"):
        print("You lose")

# User chooses scissors
elif (user == "scissors") or (user == "Scissors"):
    print("You chose", user)
    print("NPC chose", npc)
    if (npc == "Rock"):
        print("You lose")
    elif (npc == "Paper"):
        print("You win!")
    elif (npc == "Scissors"):
        print("It's a tie")

# User enters something else
else:
    print("Please enter a valid response")
    
'''
Output 1
========= RESTART: /Users/vlong/Documents/project/CS299/project2.py =========
Rock, paper, or scissors? rock
You chose rock
NPC chose Rock
It's a tie

Output 2
========= RESTART: /Users/vlong/Documents/project/CS299/project2.py =========
Rock, paper, or scissors? paper
You chose paper
NPC chose Scissors
You lose

Output 3
========= RESTART: /Users/vlong/Documents/project/CS299/project2.py =========
Rock, paper, or scissors? scissors
You chose scissors
NPC chose Paper
You win!

Output 4
========= RESTART: /Users/vlong/Documents/project/CS299/project2.py =========
Rock, paper, or scissors? Paper
You chose Paper
NPC chose Paper
It's a tie

Output 5
========= RESTART: /Users/vlong/Documents/project/CS299/project2.py =========
Rock, paper, or scissors? Rock
You chose Rock
NPC chose Scissors
You win!

Output 6
========= RESTART: /Users/vlong/Documents/project/CS299/project2.py =========
Rock, paper, or scissors? hello
Please enter a valid response

Output 7
========= RESTART: /Users/vlong/Documents/project/CS299/project2.py =========
Rock, paper, or scissors? 1234
Please enter a valid response


'''
