import os

fileFrom = input("Enter the file name to open (include .txt extension): ")

if(os.path.isfile(fileFrom)):
    ff = open(fileFrom, "r")
else:
    print("The file does not exist.")
    exit(1)

fileTo = input("Enter the file name to save to (include .txt extension): ")

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

        
fileFromContents = ff.read()
ft.write(fileFromContents)

print("Source file contents successfully copied to target!")

ff.close()
ft.close()
