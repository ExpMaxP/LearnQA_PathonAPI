from json.decoder import JSONDecodeError
import requests

# peyload = {"name":"User"}
response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)

try:
    parserd_response_text = response.json()
    print(parserd_response_text)
except JSONDecodeError:
    print("Response is not a JSON format")
