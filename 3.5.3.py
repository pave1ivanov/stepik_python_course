import requests

while True:
    number = str(input("Number? ")).strip()
    url = f"http://numbersapi.com/{number}/math"
    params = {
        "default": "Boring"
    }
    response = requests.get(url, params)
    if response.text == "Boring":
        print(response.text)
    else:
        print("Interesting")
