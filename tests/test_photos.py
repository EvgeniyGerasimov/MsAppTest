from data.methods import Methods
from data import body


class TestPhotos:

    def test_photos_browse(self):
        response = Methods.post('/photos/browse/', body.PHOTOS_BROWSE, Methods.headers)
        assert 200 == response.status_code

    def test_photos_latest(self):
        response = Methods.post('/photos/latest/', body.PHOTOS_LATEST, Methods.headers)
        assert 200 == response.status_code

    def test_photos_detail(self):
        response = Methods.post('/photos/detail/', body.PHOTOS_DETAIL, Methods.headers)
        assert 200 == response.status_code

    def test_photos_signature(self):
        response = Methods.post('/photos/signature/', body.PHOTOS_SIGNATURE, Methods.headers)
        assert 200 == response.status_code
