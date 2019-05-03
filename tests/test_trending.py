from data.methods import Methods
from data import request_body


class TestTrending:

    def test_trending_latest(self):
        response = Methods.post('/trending/latest/', request_body.TRENDING_LATEST, Methods.headers)
        assert 200 == response.status_code
