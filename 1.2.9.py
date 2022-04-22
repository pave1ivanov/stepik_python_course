objects = [1, 2, 3, 4, 2, 1]

ans = 0

ids = set()

for obj in objects:
    if id(obj) not in ids:
        ids.add(id(obj))
        ans += 1

print(ans)