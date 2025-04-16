print("Opening myfile.txt")

distance = int(input("Enter the distance value: "))
code = ""

f = open("myfile.txt", 'r')
plainText = f.read()

for ch in plainText:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    if cipherValue > ord('z'):
        cipherValue = ord('a') + distance - (ord('z') - ordvalue + 1)
    code += chr(cipherValue)

f = open("encrypt.txt", 'w')
f.write(code)
f.close()
print("Cipher saved to encrypt.txt")
