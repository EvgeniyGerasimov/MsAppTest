from data.methods import Methods
from data import request_body
from jsonschema import validate
from data.json_shemas import trending_latest_shema


class TestTrending:

    def test_trending_latest(self):
        response = Methods.post('/trending/latest/', request_body.TRENDING_LATEST, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=trending_latest_shema.TRENDING_LATEST_SHEMA)
