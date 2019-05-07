from data.methods import Methods
from data import request_body
from jsonschema import validate
from data.json_shemas import topic_find_shema


class TestsTopic:

    def test_topic_find(self):
        response = Methods.post('/topic/find/', request_body.TOPIC_FIND, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=topic_find_shema.TOPIC_SHEMA)
