MAX_YEARS = 10

salary = float(input("Enter the starting yearly salary: "))
increase = float(input("Enter the annual % increase: "))
years = int(input("Enter the number of years: "))

increase /= 100
increase += 1

print("%-4s%9s" % ("Year", "Salary"))
for i in range(1, years+1):
    print("%-6d$ %6.2f" % (i, salary))

    if(i <= MAX_YEARS):
        salary *= increase
