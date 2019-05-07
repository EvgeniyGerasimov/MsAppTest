from data.methods import Methods
from jsonschema import validate
from data.json_shemas import admin_shemas, admin_menu_shema, admin_translation_shema


class TestAdmin:

    def test_admin_menu(self):
        response = Methods.get('/admin/menu/', Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=admin_menu_shema.ADMIN_MENU)

    def test_admin_info(self):
        response = Methods.get('/admin/info/', Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=admin_shemas.ADMIN_INFO)

    def test_admin_translation(self):
        response = Methods.get('/admin/translation/', Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=admin_translation_shema.ADMIN_TRANSLATION)
