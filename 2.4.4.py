with open("dataset_24465_4.txt", "r") as first, open("second.txt", "w")as second:
    lines = first.read().splitlines()
    lines.reverse()
    for line in lines:
        second.write(line + "\n")

