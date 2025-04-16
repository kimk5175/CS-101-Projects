print("Opening encrypt.txt")

distance = int(input("Enter the distance value: "))
decryptedText = ""

f = open("encrypt.txt", 'r')
plainText = f.read()

for ch in plainText:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distance
    if cipherValue < ord('a'):
        cipherValue = ord('z') - (distance - (ord('a') - ordvalue - 1))
    decryptedText += chr(cipherValue)

f = open("decrypt.txt", 'w')
f.write(decryptedText)
f.close()
print("Cipher saved to decrypt.txt")
