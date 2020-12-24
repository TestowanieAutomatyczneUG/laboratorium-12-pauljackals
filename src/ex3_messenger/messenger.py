from .template_engine import TemplateEngine
from .mail_server import MailServer


class Messenger:
    def __init__(self):
        self.mail_sever = MailServer()
        self.template_engine = TemplateEngine()

    def send(self, target, message):
        try:
            return self.template_engine.send(target, message, self.mail_sever)
        except ConnectionError:
            raise ConnectionError("Can't access mail server")

    def receive(self):
        try:
            return self.template_engine.receive(self.mail_sever)
        except ConnectionError:
            raise ConnectionError("Can't access mail server")
