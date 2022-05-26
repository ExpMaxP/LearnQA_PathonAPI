import pytest
import requests


class TestAuth:
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup(self):
        data = {
            'email': "vinkotov@example.com",
            'password': "1234"
        }

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        assert "auth_sid" in response1.cookies, "There is no auth cookie in the response"
        assert "x-csrf-token" in response1.headers, "There is no CSRF token headers in the response"
        assert "user_id" in response1.json(), "There is no user_id in the response"

        self.auth_sid = response1.cookies.get("auth_sid")
        self.token = response1.headers.get("x-csrf-token")
        self.user_id_from_authMethod = response1.json()["user_id"]

    def test_auth_user(self):
        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token" : self.token},
            cookies={"auth_sid" : self.auth_sid}
        )
        assert "user_id" in response2.json(), "There is no user in thr second response"
        user_id_from_secondMethod = response2.json()["user_id"]

        assert self.user_id_from_authMethod == user_id_from_secondMethod, "User id from authMethod is not equal to user id from secondMethod"


    @pytest.mark.parametrize('condition',exclude_params)
    def test_negative_auth(self, condition):

        if condition == "no_cookie":
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers={"x-csrf-toren": self.token}
            )
        else:
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                cookies={"auth_sid": self.auth_sid}
            )

        assert "user_id" in self.response2.json(), "There is no user id in the second secondre response"

        user_id_from_checkMethod = response2.json()["user_id"]

        assert user_id_from_checkMethod == 0, f"User is authorized with condition{condition}"





