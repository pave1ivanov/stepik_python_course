import re
import sys

for line in sys.stdin:
    line = line.strip()
    print(re.sub(r"\ba[aA]*\b", "argh", line, 1, re.IGNORECASE))
