#Author: Vivian Long
#Assignment: Lab 1
#Completed: 1/8/2018


name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
company = input("Enter the company you wish to work: ")
wage = int(input("Enter monthly salary you wish to earn in dollars: "))
salary = wage * 12

print("My name is " + name + ", my age is " + str(age))
print("I hope to work for " + company + " and earn $" + str(salary) + " per year")

'''
Please enter your name: Vivian
Please enter your age: 24
Enter the company you wish to work: Google
Enter monthly salary you wish to earn in dollars: 10000
My name is Vivian, my age is 24
I hope to work for Google and earn $120000 per year

Please enter your name: Jane
Please enter your age: 20
Enter the company you wish to work: Microsoft
Enter monthly salary you wish to earn in dollars: 9000
My name is Jane, my age is 20
I hope to work for Microsoft and earn $108000 per year
'''

weight = int(input("Please enter your weight in lbs: "))
height = int(input("Please enter your height in inches: "))
bmi = weight / (height ** 2) * 703

print("Your BMI is", bmi)

'''
Please enter your weight in lbs: 140
Please enter your height in inches: 67
Your BMI is 21.924704834038764

Please enter your weight in lbs: 130
Please enter your height in inches: 64
Your BMI is 22.31201171875
'''
