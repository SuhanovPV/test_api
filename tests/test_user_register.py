import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserRegister(BaseCase):

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_date(email=email)
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_status_code(response, 400)
        assert response.content.decode(
            'utf-8') == f"Users with email '{email}' already exists", f"Unexpected content {response.content}"

    def test_create_user_successfully(self):
        data = self.prepare_registration_date()
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, 'id')
