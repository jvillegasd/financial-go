from tests.base import BaseCase
from src.errors.user import UserBadCredentials, UserNotFoundError


class TestApiUserAuth(BaseCase):
    def setUp(self):
        self.users = self.importer.load_model('user')

    def tearDown(self):
        self.importer.clear_model('user')

    def test_auth_bad_creds(self):
        data = {
            'email': self.users[0]['email'],
            'password': 'bad cred'
        }
        response = self.client.post(
            '/api/auth/',
            headers=self.headers,
            json=data
        )
        response_json = response.get_json()
        expected_value: dict = {
            'code': 400,
            'name': 'Bad Request',
            'description': 'Email or password is wrong'
        }
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_json, expected_value)

    def test_auth_user_not_found(self):
        data = {
            'email': 'bad-email@email.com',
            'password': 'bad cred'
        }
        response = self.client.post(
            '/api/auth/',
            headers=self.headers,
            json=data
        )
        response_json = response.get_json()
        expected_value: dict = {
            'code': 404,
            'name': 'Not Found',
            'description': 'User not found'
        }
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_json, expected_value)
