from data.methods import Methods
from data import request_body


class TestStandings:

    def test_standings_browse(self):
        response = Methods.post('/standings/browse/', request_body.STANDINGS_BROWSE, Methods.headers)
        assert 200 == response.status_code

    def test_standings_detail(self):
        response = Methods.post('/standings/detail/', request_body.STANDINGS_DETAIL, Methods.headers)
        assert 200 == response.status_code
