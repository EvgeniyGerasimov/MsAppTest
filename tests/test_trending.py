from data.methods import Methods
from data import body


class TestTrending:

    def test_trending_latest(self):
        response = Methods.post('/trending/latest/', body.TRENDING_LATEST, Methods.headers)
        assert 200 == response.status_code
