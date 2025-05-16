from requests.models import Response


def response(response:Response):
    json = response.json()
    assert json == "hello"