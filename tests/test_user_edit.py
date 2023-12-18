import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        register_data = self.prepare_registration_date()
        response_register = requests.post("https://playground.learnqa.ru/api/user", data=register_data)

        Assertions.assert_status_code(response_register, 200)
        Assertions.assert_json_has_key(response_register, "id")

        email = register_data["email"]
        first_name = register_data["firstName"]
        last_name = register_data["lastName"]
        password = register_data["password"]
        user_id = self.get_json_value(response_register, "id")

        login_data = {
            'email': email,
            'password': password
        }

        response_auth = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        auth_sid = self.get_cookie(response_auth, 'auth_sid')
        token = self.get_header(response_auth, "x-csrf-token")

        new_name = "ChangedName"
        response_edit = requests.put(f"https://playground.learnqa.ru/api/user/{user_id}",
                                     headers={"x-csrf-token": token},
                                     cookies={"auth_sid": auth_sid},
                                     data={"firstName": new_name}
                                     )

        Assertions.assert_status_code(response_edit, 200)

        response_check = requests.get(f"https://playground.learnqa.ru/api/user/{user_id}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
                                      )
        Assertions.assert_json_value_by_name(response_check,
                                             "firstName",
                                             new_name,
                                             "Wrong name of the users after edit")
