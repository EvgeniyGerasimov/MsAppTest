from data.methods import Methods


class TestAdmin:

    def test_admin_menu(self):
        response = Methods.get('/admin/menu/')
        assert 200 == response.status_code

    def test_admin_info(self):
        response = Methods.get('/admin/info/')
        assert 200 == response.status_code

    def test_admin_translation(self):
        response = Methods.get('/admin/translation/')
        assert 200 == response.status_code
