import requests
import time

URL = "https://playground.learnqa.ru/ajax/api/longtime_job"

response = requests.get(URL)
token = response.json()["token"]
execution_time = response.json()["seconds"]

payload = {"token": token}
response1 = requests.get(URL, params=payload)
print(response1.text)
time.sleep(execution_time)
response2 = requests.get(URL, params=payload)
print(response2.text)
