from tests.base import BaseCase


class TestCardCRUD(BaseCase):
    def setUp(self):
        self.users = self.importer.load_model('user')
        self.cards = self.importer.load_model('card')
        self.auth_user = self.authentication(
            user_creds={
                'email': self.users[0]['email'],
                'password': self.users[0]['password']
            }
        )

    def tearDown(self):
        self.importer.clear_model('card')
        self.importer.clear_model('user')

    def test_create_new_card(self):
        data = {
            'title': 'a new card',
            'initial_amount': 100
        }
        response = self.client.post(
            '/api/card/',
            headers=self.headers,
            json=data
        )
        response_json = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_json['title'], data['title'])
        self.assertEqual(response_json['initial_amount'], data['initial_amount'])
