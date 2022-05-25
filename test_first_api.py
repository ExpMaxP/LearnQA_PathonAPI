import pytest
import requests

class TestFirstAPI:
    names = [
            ("Max"),
            ("Sergey"),
            ("")
        ]

    @pytest.mark.parametrize('name',names)
    def test_hello_call(self,name):
        url  = "https://playground.learnqa.ru/api/hello"
        data = {'name': name}

        resonse = requests.get(url,params=data)
        assert resonse.status_code == 200, "Wrong response code"

        response_dict = resonse.json()
        assert 'answer' in response_dict, "There is no field 'answer' in the response"

        if len(name) == 0:
            expected_response = f"Hello, someone"
        else:
            expected_response = f"Hello, {name}"

        acteaul_response_text = response_dict['answer']
        assert acteaul_response_text == expected_response, "Actual text in response is not correct"

