from data.methods import Methods
from data import body


class TestVideos:

    def test_videos_browse(self):
        response = Methods.post('/videos/browse/', body.VIDEOS_BROWSE, Methods.headers)
        assert 200 == response.status_code

    def test_videos_latest(self):
        response = Methods.post('/videos/latest/', body.VIDEOS_LATEST, Methods.headers)
        assert 200 == response.status_code

    def test_videos_detail(self):
        response = Methods.post('/videos/detail/', body.VIDEOS_DETAIL, Methods.headers)
        assert 200 == response.status_code
