import requests


class Methods:

    headers = {'Content-Type': 'application/json'}
    base_url = 'http://api-s-v1.motorsport.com'
    @staticmethod
    def get(url):
        result = requests.get(Methods.base_url + url,
                              headers=Methods.headers,
                              params=None)
        return result
    @staticmethod
    def post(url, body):
        result = requests.post(Methods.base_url + url,
                               json=body,
                               headers=Methods.headers,
                               )
        return result


