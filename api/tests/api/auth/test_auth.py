from tests.base import BaseCase


class TestApiUserAuth(BaseCase):
    def setUp(self):
        self.users = self.importer.load_model('user')

    def tearDown(self):
        self.importer.clear_model('user')

    def test_auth_endpoint(self):
        data = {
            'email': self.users[0]['email'],
            'password': self.users[0]['password']
        }
        response = self.client.post(
            '/api/auth/',
            headers=self.headers,
            json=data
        )
        response_json = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response_json)
        self.assertEqual(response_json['user']['email'], data['email'])
