from data.methods import Methods
from data import body


class TestSchedule:

    def test_schedule_browse(self):
        response = Methods.post('/schedule/browse/', body.SCHEDULE_BROWSE, Methods.headers)
        assert 200 == response.status_code

    def test_schedule_list(self):
        response = Methods.post('/schedule/list/', body.SCHEDULE_LIST, Methods.headers)
        assert 200 == response.status_code
