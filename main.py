import requests

response = requests.get("https://playground.learnqa.ru/api/check_type")
print(response.status_code)






# try:
#     parserd_response_text = response.json()
#     print(parserd_response_text)
# except JSONDecodeError:
#     print("Response is not a JSON format")
