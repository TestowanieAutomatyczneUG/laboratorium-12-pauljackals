import unittest
from src.ex2_subscriber.subscriber import Subscriber
from unittest.mock import MagicMock


class TestSubscriber(unittest.TestCase):
    def setUp(self):
        clients = MagicMock()
        clients.append.side_effect = lambda x: x

        clients_list = ['Joe', 'Mark']

        def clients_remove(x):
            if x in clients_list:
                return x
            else:
                raise ValueError
        clients.remove.side_effect = clients_remove

        send = MagicMock()

        def send_function(x, y):
            if x in clients_list:
                return {
                    'client': x,
                    'message': y
                }
            else:
                raise ValueError

        send.side_effect = send_function

        self.subscriber = Subscriber(clients, send)

    def test_add_client(self):
        client = 'John'
        self.assertEqual(self.subscriber.add_client(client), client)

    def test_add_client_wrong_type(self):
        with self.assertRaisesRegex(TypeError, '^Client must be a string$'):
            self.subscriber.add_client(545)

    def test_remove_client(self):
        client = 'Joe'
        self.assertEqual(self.subscriber.remove_client(client), client)

    def test_remove_client_wrong_type(self):
        with self.assertRaisesRegex(TypeError, '^Client must be a string$'):
            self.subscriber.remove_client(545)

    def test_remove_client_no_client(self):
        with self.assertRaisesRegex(ValueError, '^No such client$'):
            self.subscriber.remove_client('John')

    def test_send_message(self):
        data = {
            'client': 'Joe',
            'message': 'Hi'
        }
        self.assertDictEqual(self.subscriber.send_message(data['client'], data['message']), data)

    def test_send_message_wrong_type(self):
        with self.assertRaisesRegex(TypeError, '^Both client and message must be strings$'):
            self.subscriber.send_message('Joe', 5435)

    def test_send_message_no_client(self):
        with self.assertRaisesRegex(ValueError, '^No such client$'):
            self.subscriber.send_message('John', 'Hi')

    def tearDown(self):
        self.subscriber = None


if __name__ == '__main__':
    unittest.main()
