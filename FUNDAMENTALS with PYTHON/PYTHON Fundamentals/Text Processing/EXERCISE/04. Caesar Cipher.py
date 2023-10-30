text = input()
encrypter_version = ""

for symbol in text:
    encrypter_version += chr(ord(symbol) + 3)

print(encrypter_version)