import requests
import pytest


@pytest.fixture(scope="function")
def authtoken():
    url = "https://accounts.motorsportnetwork.com/oauth/access_token"

    payload = "grant_type=password&client_id=72&client_secret=KsuA38vVCyTYrEryumfU9P2vhwGgzwTr&username=test%40mail.com&password=Prodigy1986"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
    }

    response = requests.post(url, data=payload, headers=headers)
    token = response.json()
    authorization_token = token['access_token']
    headers_aus = {'Content-Type': 'application/json', 'location': 'ua', 'AuthorizationToken': authorization_token}
    return headers_aus


@pytest.fixture(scope="function")
def tokens():
    url = "https://accounts.motorsportnetwork.com/oauth/access_token"

    payload = "grant_type=password&client_id=72&client_secret=KsuA38vVCyTYrEryumfU9P2vhwGgzwTr&username=test%40mail.com&password=Prodigy1986"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
    }

    response = requests.post(url, data=payload, headers=headers)
    tokens = response.json()
    return tokens
