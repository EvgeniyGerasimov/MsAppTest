import requests
import os


class Methods:
    server = os.getenv('SERVER', "")
    headers = {'Content-Type': 'application/json', 'location': 'ua'}
    base_url = 'http://api' + server + '-v1.motorsport.com'

    @staticmethod
    def get(url, headers,params=None):
        result = requests.get(Methods.base_url + url,
                              headers=headers,
                              params=params
                              )
        return result

    @staticmethod
    def post(url, body, headers):
        result = requests.post(Methods.base_url + url,
                               json=body,
                               headers=headers,
                               params=None
                               )
        return result


