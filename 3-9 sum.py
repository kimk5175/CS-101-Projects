theSum = 0.0
count = 0
data = input("Enter a number or press Enter to quit: ")
while data != "":
    number = float(data)
    theSum += number
    count += 1
    data = input("Enter a number or press Enter to quit: ")
    print("The sum is", theSum)
    average = (theSum / count)
    print("The average is,", average)
