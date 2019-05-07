from data.methods import Methods
from data import request_body
from jsonschema import validate
from data.json_shemas import standings_browse_shema, sheldue_list_shema


class TestStandings:

    def test_standings_browse(self):
        response = Methods.post('/standings/browse/', request_body.STANDINGS_BROWSE, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=standings_browse_shema.STANDINGS_BROWSE_SHEMA)

    def test_standings_detail(self):
        response = Methods.post('/standings/detail/', request_body.STANDINGS_DETAIL, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=sheldue_list_shema.SHELDUE_LIST_SHEMA)
