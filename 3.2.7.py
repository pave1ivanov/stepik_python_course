import re
import sys

for line in sys.stdin:
    line = line.strip()
    if len(re.findall(r"cat", line)) >= 2:
        print(line)