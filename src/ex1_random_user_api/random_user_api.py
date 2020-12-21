import requests


class RandomUserAPI:
    def __init__(self):
        self.api_url = 'https://randomuser.me/api/'
        self.requests = requests

    def get_random_user(self):
        response = self.requests.get(self.api_url)
        return response.json()['results'][0]

    def get_random_users(self, number):
        if type(number) != int:
            raise TypeError('Number must be an integer')

        response = self.requests.get(self.api_url+'?results='+str(number))
        return response.json()['results']

    def get_random_user_with_nationality(self, nationality):
        if type(nationality) != str:
            raise TypeError('Nationality must be a string')
        elif nationality == '':
            raise ValueError('Nationality must not be empty')

        response = self.requests.get(self.api_url+'?nat='+nationality)
        return response.json()['results'][0]

    def get_random_user_with_gender(self, gender):
        if type(gender) != str:
            raise TypeError('Gender must be a string')
        elif gender == '':
            raise ValueError('Gender must not be empty')

        response = self.requests.get(self.api_url+'?gender='+gender)
        return response.json()['results'][0]

    def get_random_user_without_field(self, field):
        if type(field) != str:
            raise TypeError('Field must be a string')
        elif field == '':
            raise ValueError('Field must not be empty')

        response = self.requests.get(self.api_url+'?exc='+field)
        return response.json()['results'][0]

    def get_user_from_seed(self, seed):
        if type(seed) != str:
            raise TypeError('Seed must be a string')
        elif seed == '':
            raise ValueError('Seed must not be empty')

        response = self.requests.get(self.api_url+'?seed='+seed)
        return response.json()['results'][0]
