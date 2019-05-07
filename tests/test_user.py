from data.methods import Methods
from data import request_body
from jsonschema import validate
from data.json_shemas import user_dashboard_shema, user_favorites_shema, user_edition_get_shema, user_edition_post_shema, user_notification_shema


class TestUser:

    def test_user_dashboard(self, authtoken):
        response = Methods.post('/user/dashboard/', request_body.USER_DASHBOARD, authtoken)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=user_dashboard_shema.USER_DASHBOARD_SHEMA)


    def test_user_favorites(self, authtoken):
        response = Methods.get('/user/favorites/', authtoken)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=user_favorites_shema.USER_FAVORITES)

    def test_user_edition_get(self):
        query = {"device_id": "123213"}
        response = Methods.get('/user/edition/', Methods.headers, params=query)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=user_edition_get_shema.USER_EDITION_GET_SHEMA)


    def test_user_edition_post(self):
        response = Methods.post('/user/edition/', request_body.USER_EDITION, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=user_edition_post_shema.USER_EDITION_POST_SHEMA)


    def test_user_notification_settings(self):
        response = Methods.get('/user/notification/settings/', Methods.headers,
                               params=request_body.USER_NOTIFICATION_SETTINGS)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=user_notification_shema.USER_NOTIFICATION_SETTINGS)


    def test_user_notification_registration(self, authtoken):
        token = authtoken['AuthorizationToken']
        body = {"device_id": "12345", "token": token}
        response = Methods.post('/user/notification/registration/', body, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=user_notification_shema.USER_NOTIFICATION_REGISTRATION)
        print(response.json())

    def test_user_notification_series(self):
        response = Methods.post('/user/notification/series/', request_body.USER_NOTIFICATION_SERIES, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=user_notification_shema.USER_NOTIFICATION_SERIES_SHEMA)


    def test_user_notification_refresh(self, tokens):
        old_token = tokens["access_token"]
        new_token = tokens["refresh_token"]
        body = {"device_id": "12345", "new_token": new_token, "old_token": old_token}
        response = Methods.post('/user/notification/refresh/', body, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=user_notification_shema.USER_NOTIFICATION_REFRESH)
        print(response.json())

