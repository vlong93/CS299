# Author: Vivian Long
# Assignment: Lab 5
# Completed: 2/7/2018

from math import sqrt, degrees, atan
import sys


# 1a: Function calculates hypotenuse given length of legs
def hypotenuse(a, b):
    c = sqrt(a ** 2 + b ** 2)
    return c


# 1b: Function calculates angle A given length of legs
def angle(a, b):
    bac = degrees(atan(a / b))
    return bac


# 1c: Triangle main function
def triangle_main():
    print("1. The hypotenuse is", hypotenuse(7.5, 7.5))
    print("2. The hypotenuse is", hypotenuse(7.5, 10.0))
    print("3. The hypotenuse is", hypotenuse(6.0, 4.5))

    print("1. The angle of A is", angle(7.5, 7.5))
    print("2. The angle of A is", angle(7.5, 10.0))
    print("3. The angle of A is", angle(6.0, 4.5))


triangle_main()  # Triangle main function call


# Task 2: Prime checker
def isPrime(n):
    i = 2
    while n > i:  # Input is greater than 2; 1 & 2 are prime
        if n % i == 0 and i != n:  # Divides evenly by some number other than itself
            return False
        i += 1
    else:
        return True


#  2: Prime main function
def prime_main():
    try:
        n = int(input("Enter a positive integer: "))

    except ValueError:
        print("Not an integer.")
        sys.exit(0)

    else:
        if n <= 1:
            print("Not a positive number.")
            sys.exit(0)
        else:
            if isPrime(n):
                print(n, "is prime")
            else:
                print(n, "is not prime")


prime_main()  # Prime main function call



'''
Task 1:
1. The hypotenuse is 10.606601717798213
2. The hypotenuse is 12.5
3. The hypotenuse is 7.5
1. The angle of A is 45.0
2. The angle of A is 36.86989764584402
3. The angle of A is 53.13010235415598

Task 2:
Enter a positive integer: 1
Not a positive number.
Enter a positive integer: 2
2 is prime
Enter a positive integer: 17
17 is prime
Enter a positive integer: 27
27 is not prime
Enter a positive integer: 61
61 is prime
Enter a positive integer: 237
237 is not prime
Enter a positive integer: 255
255 is not prime
'''