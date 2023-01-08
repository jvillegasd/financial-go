from tests.base import BaseCase


class TestUserCRUD(BaseCase):
    def setUp(self):
        self.users = self.importer.load_model('user')

    def tearDown(self):
        self.importer.clear_model('user')

    def test_create_new_user(self):
        data = {
            'first_name': 'test',
            'last_name': 'name',
            'email': 'test@test.com',
            'password': 'password'
        }
        response = self.client.post(
            '/api/user/',
            headers=self.headers,
            json=data
        )
        response_json = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_json['first_name'], data['first_name'])
        self.assertEqual(response_json['last_name'], data['last_name'])
        self.assertEqual(response_json['email'], data['email'])
        self.assertNotIn('password', response_json)
