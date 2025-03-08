'''Francisco Perestrello, 39001'''

'''Exercise 1'''

def square(n):
    if n<1:
        print("The number inputed must be a positive integer.")
    else:
        result = 0
        for i in range(1,n):
            result = result + i**2
        print (result)

n = int(input("Please input a positive integer for which you would like to know the sum of the squares of all the positive integeres smaller than that number: "))
square(n)


'''Exercise 2'''

import math

def check(n):
    if n<1:
        print("The number inputed must be a positive integer.")
    else:
        check = math.sqrt(n).is_integer()
        print (check)
    
n = int(input("Please input a positive integer to check if it is a perfect square: "))
check(n)


'''Exercise 3'''

def triangle(a,b,c):
    if ((a<=0) or (b<=0) or (c <= 0)):
        print("\nAll the sides must be positive numbers.")
    else:
        if ((a < b + c) and (b < a + c) and (c < a + b)):
            check = True
            if (a == b == c):
                classification = "Equilateral"
            elif ((a == b != c) or (a == c != b) or (b == c != a)):
                classification = "Isosceles"
            else:
                classification = "Scalene"
            if ((a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2)):
                right = True
            else:
                right = False
            print ("\nThe given inputs can make a triangle: %s.\nThe triangle is: %s.\nThe triangle is right: %s." % (check, classification, right))
        else:
            check = False
            print ("\nThe given inputs can make a triangle: %s." % check)
    
a = float(input("Please input one of the sides: "))
b = float(input("Please input another side: "))
c = float(input("Please input a final side: "))
triangle(a,b,c)