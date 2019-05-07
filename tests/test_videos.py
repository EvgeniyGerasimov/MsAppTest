from data.methods import Methods
from data import request_body
from jsonschema import validate
from data.json_shemas import video_browse_shema, video_ditale_shema, video_latest_shema


class TestVideos:

    def test_videos_browse(self):
        response = Methods.post('/videos/browse/', request_body.VIDEOS_BROWSE, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=video_browse_shema.VIDEO_BROWSE_SHEMA)

    def test_videos_latest(self):
        response = Methods.post('/videos/latest/', request_body.VIDEOS_LATEST, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=video_latest_shema.VIDEO_LATEST_SHEMA)

    def test_videos_detail(self):
        response = Methods.post('/videos/detail/', request_body.VIDEOS_DETAIL, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=video_ditale_shema.VIDEO_DETAIL_SHEMA)
