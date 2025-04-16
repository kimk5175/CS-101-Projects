"""
Program: equilateral.py
Author: Kalani Kim

Indicate whether or not a triangle is an equilateral triangle.

1. The inputs are
       length of side a, b and c
2. Computations:
       compare sides a and b and b and c
4. The outputs are
       whether the triangle is equilateral or not
"""
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

if(a == b and b == c):
 print("The triangle is equilateral.")
else:
 print("The triangle is not equilateral.")
