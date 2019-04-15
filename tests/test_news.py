from data.methods import Methods
from data import body


class TestNews:
    def test_news_browse(self):
        response = Methods.post('/news/browse/',body.NEWS_BROWSE)
        assert 200 == response.status_code

    def test_news_latest(self):
        response = Methods.post('/news/latest/', body.NEWS_LATEST)
        assert 200 == response.status_code
