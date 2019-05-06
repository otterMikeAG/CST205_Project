import requests, json, pprint


# noinspection PyUnreachableCode
class Petfinder():
    def __init__(self, c_key, s_key):
        '''this will initialize the client key and secret key used for APi calls.'''
        self.c_key = c_key
        self.s_key = s_key
        self.auth_key = 'need'
        self.pet_dict = {}

    def print_values(self):
        print(self.c_key)

        print(self.s_key)

        print(self.auth_key)

    # used to get auth key from API
    def get_auth(self):
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.c_key,
            'client_secret': self.s_key
        }
        response = requests.post('https://api.petfinder.com/v2/oauth2/token', data=data)
        if (response):
            returned = response.json()
            self.auth_key = returned['access_token']

    # preforms the api call to get all pets of specific type
    def get_pets(self, type):
        headers = {
            'Authorization': 'Bearer ' + self.auth_key
        }
        params = {
            'type': type
        }

        response = requests.get('https://api.petfinder.com/v2/animals', headers=headers, params=params)
        print(response)
        returned = response.json()
        data_send = returned['animals']
        print(data_send)
        return data_send

    # supposed to show the pet's details when clicked
    def get_photo(self, photo):  # , name):

        headers = {
            'Authorization': 'Bearer ' + self.auth_key
        }
        params = {
            'photos': photo
        }
        # call to api
        response2 = requests.get("https://api.petfinder.com/v2/animals/", headers=headers,
                                 params=params).json()  # , params2=params2).json()
        #for debugging
        print(response2)
        animal_photo = response2['animals'][0]['photos'][0]['medium']
        print('^^^^^^^^^^^^^^^^Animal returned^^^^^^^^^^^^^^^^')
        return animal_photo

    def get_name(self, name):
        headers = {
            'Authorization': 'Bearer ' + self.auth_key
        }
        params = {
            'type': name
        }
        response3 = requests.get("https://api.petfinder.com/v2/animals/", headers=headers, params=params).json()
        print('\n\n^^^^^^^^^^^^^^^^^RESPONSE 3 NAME^^^^^^^^^^^^^^^^')
        #for debugging
        print(response3)
        print('\n\n')
        print('\n\n^^^^^^^^^^^^^^^^^RESPONSE 3 NAME^^^^^^^^^^^^^^^^')
        animal_name = response3['animals'][0]['name']
        print('\n\n')
        print(animal_name)
        return animal_name

    def get_description(self, description):
        headers = {
            'Authorization': 'Bearer ' + self.auth_key
        }
        params = {
            'type': description
        }
        response4 = requests.get("https://api.petfinder.com/v2/animals/", headers=headers, params=params).json()
        print('\n\n^^^^^^^^^^^^^^^^^RESPONSE 3 NAME^^^^^^^^^^^^^^^^')
        print(response4)
        print('\n\n')
        print('\n\n^^^^^^^^^^^^^^^^^RESPONSE 3 NAME^^^^^^^^^^^^^^^^')
        animal_name = response4['animals'][0]['description']
        print('\n\n')
        print(animal_name)
        return animal_name

    def get_contact(self, contact):
        headers = {
            'Authorization': 'Bearer ' + self.auth_key
        }
        params = {
            'type': contact
        }
        response5 = requests.get("https://api.petfinder.com/v2/animals/", headers=headers, params=params).json()
        print('\n\n^^^^^^^^^^^^^^^^^RESPONSE 3 NAME^^^^^^^^^^^^^^^^')
        print(response5)
        print('\n\n')
        print('\n\n^^^^^^^^^^^^^^^^^RESPONSE 3 NAME^^^^^^^^^^^^^^^^')
        animal_contact = response5['animals'][0]['contact']['email']
        print('\n\n')
        print(animal_contact)
        return animal_contact


