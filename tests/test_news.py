from data.methods import Methods
from data import request_body
from jsonschema import validate
from data.json_shemas import news_browse_shema, news_latest_shema, news_detail_shema


class TestNews:
    def test_news_browse(self):
        response = Methods.post('/news/browse/', request_body.NEWS_BROWSE, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=news_browse_shema.NEWS_BROWSE_SHEMA)

    def test_news_latest(self):
        response = Methods.post('/news/latest/', request_body.NEWS_LATEST, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=news_latest_shema.NEWS_LATEST_SHEMA)

    def test_news_detail(self):
        response = Methods.post('/news/detail/', request_body.NEWS_DETAIL, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=news_detail_shema.NEWS_DETAIL_SHEMA)
