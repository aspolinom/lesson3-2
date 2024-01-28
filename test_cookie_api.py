import requests

class TestCookieAPI:
    def test_cookie_API(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        name = "Alex"
        data = {'name':name}
        response = requests.get(url,params=data)
        assert response.status_code == 200, "Wrong response code "


        response_cookie = response.cookies
        assert response_cookie is not None, "There is not field cookie"
        print()
        print("answer=",dict(response.cookies))