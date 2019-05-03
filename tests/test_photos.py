from data.methods import Methods
from data import request_body
from jsonschema import validate
from  data.JSON_Shemas import photo_latest_shema,photos_browse_shema,photo_detail_shema, photos_signature_shema


class TestPhotos:

    def test_photos_browse(self):
        response = Methods.post('/photos/browse/', request_body.PHOTOS_BROWSE, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=photos_browse_shema.PHOTOS_BROWSE_SHEMA)

    def test_photos_latest(self):
        response = Methods.post('/photos/latest/', request_body.PHOTOS_LATEST, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=photo_latest_shema.PHOTO_LATEST_SHEMA)

    def test_photos_detail(self):
        response = Methods.post('/photos/detail/', request_body.PHOTOS_DETAIL, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=photo_detail_shema.PHOTO_DETAIL_SHEMA)

    def test_photos_signature(self):
        response = Methods.post('/photos/signature/', request_body.PHOTOS_SIGNATURE, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=photos_signature_shema.PHOTOS_SIGNATURE)

