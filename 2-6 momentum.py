"""
Program: momentum.py
Author: Kalani Kim

Compute an object's momentum.

1. The inputs are
       mass (k/g) 
       velocity (m/s)
3. Computations:
       momentum = mass * velocity
       KE = (1/2)mv^2
4. The outputs are
       the momentum
       the kinetic energy
"""
mass = float(input("Enter the object's mass (in kilograms): "))
velocity = float(input("Enter the object's velocity (in meters per second): "))
momentum = mass * velocity
KE = 0.5 * mass * velocity**2
print("The momentum of the object is", momentum, "kg*m/s.")
print("The kinetic energy is", KE, "J.")
