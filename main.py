from json.decoder import JSONDecodeError
import requests

URL = "https://playground.learnqa.ru/api"
payload = {"login": "secret_login", "password": "secret_pass"}
headers = {"some_header": "123"}

response1 = requests.post(URL + "/get_auth_cookie", data=payload)

cookie_value = response1.cookies.get('auth_cookie')

cookies = {}
if cookie_value is not None:
    cookies.update({'auth_cookie': cookie_value})


response2 = requests.post(URL + "/check_auth_cookie", cookies=cookies)
print(cookie_value)
print(response2.text)


# TODO: https://habr.com/ru/companies/first/articles/497342/