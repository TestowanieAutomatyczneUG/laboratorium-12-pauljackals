import unittest
from src.ex1_random_user_api.random_user_api import RandomUserAPI
from unittest.mock import MagicMock


class TestRandomUserApiMock(unittest.TestCase):
    def setUp(self):
        self.api = RandomUserAPI()
        self.get_response_object = lambda results: type("Object", (), {"json": lambda: {"results": results}})

    def test_get_random_user(self):
        mock = MagicMock()
        mock.get.return_value = self.get_response_object([{}])
        self.api.requests = mock

        user = self.api.get_random_user()
        self.assertIsInstance(user, dict)

    def test_get_random_users(self):
        mock = MagicMock()
        mock.get.side_effect = lambda x: self.get_response_object([{}] * int(x.split('?results=')[-1]))
        self.api.requests = mock

        number = 4
        users = self.api.get_random_users(number)
        self.assertEqual(len(users), number)

    def test_get_random_users_wrong_type(self):
        with self.assertRaisesRegex(TypeError, '^Number must be an integer$'):
            self.api.get_random_users('t')

    def test_get_random_user_with_nationality(self):
        mock = MagicMock()
        mock.get.side_effect = lambda x: self.get_response_object([{"nat": x.split('?nat=')[-1]}])
        self.api.requests = mock

        nationality = 'US'
        user = self.api.get_random_user_with_nationality(nationality)
        self.assertEqual(user['nat'], nationality)

    def test_get_random_user_with_nationality_wrong_type(self):
        with self.assertRaisesRegex(TypeError, '^Nationality must be a string$'):
            self.api.get_random_user_with_nationality(45)

    def test_get_random_user_with_nationality_empty(self):
        with self.assertRaisesRegex(ValueError, '^Nationality must not be empty$'):
            self.api.get_random_user_with_nationality('')

    def test_get_random_user_with_gender(self):
        mock = MagicMock()
        mock.get.side_effect = lambda x: self.get_response_object([{"gender": x.split('?gender=')[-1]}])
        self.api.requests = mock

        gender = 'female'
        user = self.api.get_random_user_with_gender(gender)
        self.assertEqual(user['gender'], gender)

    def test_get_random_user_with_gender_wrong_type(self):
        with self.assertRaisesRegex(TypeError, '^Gender must be a string$'):
            self.api.get_random_user_with_gender(45)

    def test_get_random_user_with_gender_empty(self):
        with self.assertRaisesRegex(ValueError, '^Gender must not be empty$'):
            self.api.get_random_user_with_gender('')

    def test_get_random_user_without_field(self):
        mock = MagicMock()
        results = {"gender": "", "name": "", "location": "", "email": "", "login": "", "dob": "", "registered": "", "phone": "", "cell": "", "id": "", "picture": "", "nat": ""}
        mock.get.side_effect = lambda x: self.get_response_object([[results, results.pop(x.split('?exc=')[-1])][0]])
        self.api.requests = mock

        field = 'login'
        user = self.api.get_random_user_without_field(field)
        self.assertTrue(field not in user)

    def test_get_random_user_without_field_wrong_type(self):
        with self.assertRaisesRegex(TypeError, '^Field must be a string$'):
            self.api.get_random_user_without_field(45)

    def test_get_random_user_without_field_empty(self):
        with self.assertRaisesRegex(ValueError, '^Field must not be empty$'):
            self.api.get_random_user_without_field('')

    def test_get_user_from_seed(self):
        mock = MagicMock()
        mock.get.side_effect = lambda x: x.split('?seed=')[-1] == 'foobar' and self.get_response_object([{"name": {"first": "Britney", "last": "Sims"}}])
        self.api.requests = mock

        user = self.api.get_user_from_seed('foobar')
        self.assertEqual(user['name']['first'] + ' ' + user['name']['last'], 'Britney Sims')

    def test_get_user_from_seed_wrong_type(self):
        with self.assertRaisesRegex(TypeError, '^Seed must be a string$'):
            self.api.get_user_from_seed(45)

    def test_get_user_from_seed_empty(self):
        with self.assertRaisesRegex(ValueError, '^Seed must not be empty$'):
            self.api.get_user_from_seed('')

    def tearDown(self):
        self.api = None


if __name__ == '__main__':
    unittest.main()
