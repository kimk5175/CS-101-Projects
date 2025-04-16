pi = 0
total = 0
iterations = int(input("Enter the number of iterations: "))

m = iterations * 2 + 1
for count in range(1, m, 2):
    if total % 2 == 0:
        pi = pi + 1 / count
    if total % 2 != 0:
        pi = pi - 1 / count
    total = total + 1

pi = pi * 4
print(pi)
