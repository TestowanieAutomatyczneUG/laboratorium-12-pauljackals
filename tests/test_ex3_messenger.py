import unittest
from src.ex3_messenger.messenger import Messenger
from unittest.mock import MagicMock


class TestMessenger(unittest.TestCase):
    def setUp(self):
        self.messenger = Messenger()

    def test_send(self):
        mail_server = MagicMock()
        mail_server.send.side_effect = lambda target, message: {'target': target, 'message': message}

        template_engine = MagicMock()
        template_engine.send.side_effect = lambda target, message, mail_server: mail_server.send(target, message)

        self.messenger.mail_sever = mail_server
        self.messenger.template_engine = template_engine

        data = {
            'target': 'joe@example.com',
            'message': 'Hello'
        }

        self.assertDictEqual(self.messenger.send(data['target'], data['message']), data)

    def test_send_error(self):
        mail_server = MagicMock()
        mail_server.send.side_effect = ConnectionError

        template_engine = MagicMock()
        template_engine.send.side_effect = lambda target, message, mail_server: mail_server.send(target, message)

        self.messenger.mail_sever = mail_server
        self.messenger.template_engine = template_engine

        with self.assertRaisesRegex(ConnectionError, "^Can't access mail server$"):
            self.messenger.send('joe@example.com', 'Hello')

    def test_receive(self):
        messages = ['Hello', 'Hi']

        mail_server = MagicMock()
        mail_server.receive.return_value = messages

        template_engine = MagicMock()
        template_engine.receive.side_effect = lambda mail_server: mail_server.receive()

        self.messenger.mail_sever = mail_server
        self.messenger.template_engine = template_engine

        self.assertListEqual(self.messenger.receive(), messages)

    def test_receive_error(self):
        mail_server = MagicMock()
        mail_server.receive.side_effect = ConnectionError

        template_engine = MagicMock()
        template_engine.receive.side_effect = lambda mail_server: mail_server.receive()

        self.messenger.mail_sever = mail_server
        self.messenger.template_engine = template_engine

        with self.assertRaisesRegex(ConnectionError, "^Can't access mail server$"):
            self.messenger.receive()

    def tearDown(self):
        self.messenger = None


if __name__ == '__main__':
    unittest.main()
