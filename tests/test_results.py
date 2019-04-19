from data.methods import Methods
from data import body


class TestResults:

    def test_results_browse(self):
        response = Methods.post('/results/browse/', body.RESULTS_BROWSE, Methods.headers)
        assert 200 == response.status_code

    def test_results_detail(self):
        response = Methods.post('/results/detail/', body.RESULTS_DETAIL, Methods.headers)
        assert 200 == response.status_code
