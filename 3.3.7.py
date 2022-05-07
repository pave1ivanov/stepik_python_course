import requests
import re

page_url = str(input())

page = requests.get(page_url)
urls = sorted(list(set(re.findall(r"<a.*?href[= ]*[\"\']?(?:[\w-]*://)?(\w[\w.-]*)", page.text))))
for url in urls:
    print(url)
