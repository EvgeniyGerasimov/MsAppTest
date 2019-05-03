from data.methods import Methods
from data import request_body


class TestsTopic:

    def test_topic_find(self):
        response = Methods.post('/topic/find/', request_body.TOPIC_FIND, Methods.headers)
        assert 200 == response.status_code
