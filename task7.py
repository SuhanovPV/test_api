import requests

methods = ["GET", "POST", "PUT", "DELETE"]
requests_methods = {"get": requests.get, "post": requests.post, "put": requests.put, "delete": requests.delete}
URL = "https://playground.learnqa.ru/ajax/api/compare_query_type"

for requests_method in requests_methods:
    for method in methods:
        payload = {"method": method}
        if requests_method == "get":
            response = requests_methods[requests_method](URL, params=payload)
        else:
            response = requests_methods[requests_method](URL, data=payload)
        print(f"{requests_method}:\t{method} -> {response.text}")
    print()
