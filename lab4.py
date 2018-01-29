import random

print("Welcome to California SuperLotto!")

invalid_bills = 1
bills = int(input("Please enter bills to start ($1, $2, $5, $10, $20 allowed): "))
if bills != 1 and bills != 2 and bills != 5 and bills != 10 and bills != 20:
    while invalid_bills < 3:
        bills = int(input(print("Invalid number of bills. Please re-enter bills: ")))
        invalid_bills += 1

invalid_tickets = 1
tickets = int(input("How many ticket would you like to purchase? "))
if tickets > bills:
    while invalid_tickets < 3:
        tickets = int(input(print("Sorry, not enough money. Please re-enter the number of tickets to be purchased: ")))
        invalid_tickets += 1

print("Here are your", tickets, "tickets: ")
for i in range(1, tickets + 1):
    print("#" + str(i) + ": \t", random.randint(1, 47), random.randint(1, 47),
          random.randint(1, 47), random.randint(1, 47),"\t", random.randint(0, 27))

change = bills - tickets
print("Your change is $" + str(change))
print("Thank you for your support to Cal Lottery!")