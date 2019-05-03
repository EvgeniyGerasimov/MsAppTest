from data.methods import Methods
from data import request_body


class TestResults:

    def test_results_browse(self):
        response = Methods.post('/results/browse/', request_body.RESULTS_BROWSE, Methods.headers)
        assert 200 == response.status_code

    def test_results_detail(self):
        response = Methods.post('/results/detail/', request_body.RESULTS_DETAIL, Methods.headers)
        assert 200 == response.status_code
