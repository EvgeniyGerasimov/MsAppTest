from data.methods import Methods
from data import request_body
from jsonschema import validate
from data.json_shemas import results_browse_shema, result_detail_shema


class TestResults:

    def test_results_browse(self):
        response = Methods.post('/results/browse/', request_body.RESULTS_BROWSE, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=results_browse_shema.RESULT_BROWSE_SHEMA)

    def test_results_detail(self):
        response = Methods.post('/results/detail/', request_body.RESULTS_DETAIL, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=result_detail_shema.RESULT_DETAIL_SHEMA_PROD)
