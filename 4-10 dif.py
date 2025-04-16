import os

file1 = input("Enter the file name of the first file to open (include .txt extension): ")

if(os.path.isfile(file1)):
    f1 = open(file1, "r")
else:
    print("The file does not exist.")
    exit(1)

file2 = input("Enter the file name of the second file to open (include .txt extension): ")

if(os.path.isfile(file2)):
    f2 = open(file2, "r")
else:
    print("The file does not exist.")
    exit(1)

different = True
for line_num, (line1, line2) in enumerate(zip(f1,f2), start=1):
    if line1 != line2:
        print("No.")
        print(f"Differing lines at line {line_num}:\nFile 1: {line1.strip()}\nFile 2: {line2.strip()}")
        break
    else:
        print("Yes.")
