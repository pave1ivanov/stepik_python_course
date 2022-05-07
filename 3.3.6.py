import requests
import re

url1 = str(input())
url2 = str(input())

start_page = requests.get(url1)
reg_a = r"\bhttps:.*\.html\b"
urls = re.findall(reg_a, start_page.text)
urls2 = []
for url in urls:
    urls2 = urls2 + re.findall(reg_a, requests.get(url).text)

if url2 in urls2:
    print("Yes")
else:
    print("No")



