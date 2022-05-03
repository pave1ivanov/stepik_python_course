s = input()
a = input()
b = input()

counter = 0
while counter < 1000:
    if a in s:
        s = s.replace(a, b)
        counter += 1
    else:
        break

print(counter if counter < 1000 else "Impossible")
