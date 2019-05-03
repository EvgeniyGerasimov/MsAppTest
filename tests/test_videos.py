from data.methods import Methods
from data import request_body


class TestVideos:

    def test_videos_browse(self):
        response = Methods.post('/videos/browse/', request_body.VIDEOS_BROWSE, Methods.headers)
        assert 200 == response.status_code

    def test_videos_latest(self):
        response = Methods.post('/videos/latest/', request_body.VIDEOS_LATEST, Methods.headers)
        assert 200 == response.status_code

    def test_videos_detail(self):
        response = Methods.post('/videos/detail/', request_body.VIDEOS_DETAIL, Methods.headers)
        assert 200 == response.status_code
