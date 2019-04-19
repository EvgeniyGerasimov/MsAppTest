from data.methods import Methods
from data import body


class TestStandings:

    def test_standings_browse(self):
        response = Methods.post('/standings/browse/', body.STANDINGS_BROWSE, Methods.headers)
        assert 200 == response.status_code

    def test_standings_detail(self):
        response = Methods.post('/standings/detail/', body.STANDINGS_DETAIL, Methods.headers)
        assert 200 == response.status_code
