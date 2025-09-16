"""
Program: right.py
Author: Kim

"""

a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the thrid side: "))

square_a = a ** 2
square_b = b ** 2
square_c = c ** 2

if square_a + square_b == square_c or \
 square_b + square_c == square_a or \
 square_a + square_c == square_b:
 print("The triangle is a right triangle.")
else:
 print("The triangle is not a right triangle.")

