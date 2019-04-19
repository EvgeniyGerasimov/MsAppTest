from data.methods import Methods
from data import body

class TestEvent:

    def test_event_detail(self):
        response = Methods.post('/event/detail/', body.EVENT_DETAIL,Methods.headers)
        assert 200 == response.status_code

    def test_event_strip(self):
        response = Methods.post('/event/strip/', body.EVENT_STRIP,Methods.headers)
        assert 200 == response.status_code

    def test_event_browse(self):
        response = Methods.post('/event/browse/', body.EVENT_BROWSE,Methods.headers)
        assert 200 == response.status_code

    def test_event_best(self):
        response = Methods.post('/event/best/', body.EVENT_BEST,Methods.headers)
        assert 200 == response.status_code

    def test_event_latest(self):
        response = Methods.post('/event/latest/', body.EVENT_LATEST,Methods.headers)
        assert 200 == response.status_code
