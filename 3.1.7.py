s = input()
t = input()

count = start = 0
while True:
    start = s.find(t, start) + 1
    if start > 0:
        count += 1
    else:
        break

print(count)
