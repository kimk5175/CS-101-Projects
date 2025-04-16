"""
Program: employeepay.py
Author: Kalani Kim

Calculate total weekly pay for an employee.

1. The inputs are
       hourly wage 
       total regular hours
       total overtime hours
3. Computations:
       total_pay = (hourly_wage * total_regular_hours) + (total_overtime_hours
       * hourly_wage * 1.5)

4. The outputs are
       the total weekly pay
"""
hourly_wage = float(input("Enter the hourly wage: "))
total_regular_hours = int(input("Enter the total regular hours: "))
total_overtime_hours = int(input("Enter the total overtime hours: "))

total_pay = (hourly_wage * total_regular_hours) + (total_overtime_hours * hourly_wage * 1.5)

print("The employees total weekly pay is: $", total_pay, ".")
