from data.methods import Methods


class TestAdmin:

    def test_admin_menu(self):
        response = Methods.get('/admin/menu/',Methods.headers)
        assert 200 == response.status_code

    def test_admin_info(self):
        response = Methods.get('/admin/info/',Methods.headers)
        assert 200 == response.status_code

    def test_admin_translation(self):
        response = Methods.get('/admin/translation/',Methods.headers)
        assert 200 == response.status_code
