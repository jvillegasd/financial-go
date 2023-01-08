from tests.base import BaseCase


class TestUserCRUD(BaseCase):
    def setUp(self):
        self.users = self.importer.load_model('users')

    def tearDown(self):
        self.importer.clear_model('users')

    def test_create_new_user(self):
        data = self.users[0]
        response = self.client.post(
            '/api/user/',
            headers=self.headers,
            json=data
        )
        response_json = response.get_json()
        self.assertEqual(response.status_code,)