from tests.base import BaseCase


class TestTransactionCRUD(BaseCase):
    def setUp(self):
        self.users = self.importer.load_model('user')
        self.cards = self.importer.load_model('card')
        self.transactions = self.importer.load_model('transaction')
        self.auth_user = self.authentication(
            user_creds={
                'email': self.users[0]['email'],
                'password': self.users[0]['password']
            }
        )

    def tearDown(self) -> None:
        self.importer.clear_model('transaction')
        self.importer.clear_model('card')
        self.importer.clear_model('user')

    def test_create_transaction(self):
        data = {
            'title': 'A new transaction',
            'type': 'Unique',
            'amount': 12.3,
            'category': 'Shopping'
        }
        response = self.client.post(
            f'/api/card/{self.cards[0]["doc_id"]}/transaction',
            headers=self.headers,
            json=data
        )
        response_json = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_json['title'], data['title'])
        self.assertEqual(response_json['type'], data['type'])
        self.assertEqual(response_json['amount'], data['amount'])
        self.assertEqual(response_json['category'], data['category'])

    def test_update_transaction(self):
        data = {
            'title': 'An updated transaction',
            'type': 'Unique',
            'amount': 12.3,
            'category': 'Shopping'
        }
        response = self.client.patch(
            (
                f'/api/card/{self.cards[0]["doc_id"]}/'
                f'transaction/{self.transactions[0]["doc_id"]}'
            ),
            headers=self.headers,
            json=data
        )
        response_json = response.get_json()
        self.assertEqual(response_json['title'], data['title'])
        self.assertEqual(response_json['type'], data['type'])
        self.assertEqual(response_json['amount'], data['amount'])
        self.assertEqual(response_json['category'], data['category'])

    def test_read_transaction(self):
        response = self.client.get(
            (
                f'/api/card/{self.cards[0]["doc_id"]}/'
                f'transaction/{self.transactions[0]["doc_id"]}'
            ),
            headers=self.headers
        )
        response_json = response.get_json()
        self.assertEqual(
            response_json['doc_id'],
            self.transactions[0]['doc_id']
        )
        self.assertEqual(
            response_json['title'],
            self.transactions[0]['title']
        )
        self.assertEqual(
            response_json['amount'],
            float(self.transactions[0]['amount'])
        )

    def test_delete_transaction(self):
        response = self.client.delete(
            (
                f'/api/card/{self.cards[0]["doc_id"]}/'
                f'transaction/{self.transactions[0]["doc_id"]}'
            ),
            headers=self.headers
        )
        response_json = response.get_json()
        expected_value: dict = {
            'message': 'Transaction deleted successfully.'
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_json, expected_value)
