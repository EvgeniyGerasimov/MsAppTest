from data.methods import Methods
from data import request_body
from jsonschema import validate
from data.json_shemas import sheldue_browse_shema, sheldue_list_shema

class TestSchedule:

    def test_schedule_browse(self):
        response = Methods.post('/schedule/browse/', request_body.SCHEDULE_BROWSE, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=sheldue_browse_shema.SHELDUE_BROWSE_SHEMA)

    def test_schedule_list(self):
        response = Methods.post('/schedule/list/', request_body.SCHEDULE_LIST, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=sheldue_list_shema.SHELDUE_LIST_SHEMA)
        print(response.json())
