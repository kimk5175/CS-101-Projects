"""
Program: momentum.py
Author: Kalani Kim

Compute an object's momentum.

1. The inputs are
       mass (k/g) 
       velocity (m/s)
3. Computations:
       momentum = mass * velocity
4. The outputs are
       the momentum
"""
mass = float(input("Enter the object's mass (in kilograms): "))
velocity = float(input("Enter the object's velocity (in meters per second): "))
momentum = mass * velocity
print("The momentum of the object is", momentum, "kg*m/s.")
