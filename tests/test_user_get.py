import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserGet(BaseCase):
    def test_get_user_details_not_auth(self):
        response = requests.get("https://playground.learnqa.ru/api/user/2")
        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_no_key(response, "firstName")
        Assertions.assert_json_has_no_key(response, "lastName")
        Assertions.assert_json_has_no_key(response, "email")

    def test_get_user_details_auth(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response_auth = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        auth_sid = self.get_cookie(response_auth, 'auth_sid')
        token = self.get_header(response_auth, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response_auth, 'user_id')

        response = requests.get(f'https://playground.learnqa.ru/api/user/{user_id_from_auth_method}',
                                headers={'x-csrf-token': token},
                                cookies={'auth_sid': auth_sid})
        expected_fields = ["username", "firstName", "lastName", "email"]
        Assertions.assert_json_has_keys(response, expected_fields)
