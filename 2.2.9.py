import simplecrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open("passwords.txt") as file:
    lines = [line.replace("\n", "") for line in file]

for line in lines:
    try:
        print(simplecrypt.decrypt(line, encrypted))
    except simplecrypt.DecryptionException:
        pass
