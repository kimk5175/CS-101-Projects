import os

fileFrom = input("Enter the file name to open (include .txt extension): ")

if(os.path.isfile(fileFrom)):
    ff = open(fileFrom, "r")
else:
    print("The file does not exist.")
    exit(1)

while True:
    fileTo = input("Enter the file name to save to (include .txt extension): ")

    if fileFrom == fileTo:
        print("Error: Input and output filenames must be different.")
    else:
        break

if(os.path.isfile(fileTo)):
    overwrite = input("The target file already exists. " + 
      "Do you want to overwrite it? Enter (y)es to overwrite.")
    if(overwrite.lower() == "y"):
        ft = open(fileTo, "w")
    else:
        print("Exiting without overwriting")
        ff.close()
        exit(0)
else:
    ft = open(fileTo, "w")

line_number = 1
for line in ff:
    ft.write(f"{line_number:4}> {line}")
    line_number += 1

print("Source file contents successfully copied to target with line numbers.")

ff.close()
ft.close()
