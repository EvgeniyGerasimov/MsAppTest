from data.methods import Methods
from data import request_body
from jsonschema import validate
from data.JSON_Shemas import event_detail_shema, event_strip_shema, event_browse_shema, event_latest_shema, event_best_shema


class TestEvent:

    def test_event_detail(self):
        response = Methods.post('/event/detail/', request_body.EVENT_DETAIL, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=event_detail_shema.EVENT_DETAIL_SHEMA)

    def test_event_strip(self):
        response = Methods.post('/event/strip/', request_body.EVENT_STRIP, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=event_strip_shema.EVENT_STRIP_SHEMA)

    def test_event_browse(self):
        response = Methods.post('/event/browse/', request_body.EVENT_BROWSE, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(),schema=event_browse_shema.EVENT_BROWSE_SHEMA)

    def test_event_best(self):
        response = Methods.post('/event/best/', request_body.EVENT_BEST, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=event_best_shema.EVENT_BEST_SHEMA)

    def test_event_latest(self):
        response = Methods.post('/event/latest/', request_body.EVENT_LATEST, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(),schema=event_latest_shema.EVENT_LATEST_SHEMA)
