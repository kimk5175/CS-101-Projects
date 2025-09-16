"""
Program: bouncy.py
Author: Kim

1. The inputs are
       height
       bounciness index
       bounces
2. Computations:
       Ball is dropped from height and bounces up and then down for n number of times
3. The outputs are
       the total distance traveled
"""

height = float(input("Enter the height from which the ball is dropped: "))
bounciness = float(input("Enter the bounciness index of the ball: "))
bounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))
distance = 0

for eachPass in range(bounces):
    distance += height
    height *= bounciness
    distance += height
    print("Total distance traveled is: ", distance, "units.")

