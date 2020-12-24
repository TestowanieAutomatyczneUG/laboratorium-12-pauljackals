class Subscriber:
    def __init__(self, clients, send_function):
        self.clients = clients
        self.send_function = send_function

    def add_client(self, client):
        if type(client) != str:
            raise TypeError("Client must be a string")

        return self.clients.append(client)

    def remove_client(self, client):
        if type(client) != str:
            raise TypeError("Client must be a string")

        try:
            return self.clients.remove(client)
        except ValueError:
            raise ValueError("No such client")

    def send_message(self, client, message):
        if type(client) != str or type(message) != str:
            raise TypeError("Both client and message must be strings")

        try:
            return self.send_function(client, message)
        except ValueError:
            raise ValueError("No such client")
