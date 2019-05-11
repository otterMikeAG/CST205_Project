import requests, json, pprint



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
        
        returned = response.json()
        data_send = returned['animals']
        
        return data_send

    def get_photo(self, photo):

        '''this method returns photo from the animal that was clicked on'''
        headers = {
            'Authorization': 'Bearer ' + self.auth_key
        }
        params = {
            'photos': photo
        }
        response2 = requests.get("https://api.petfinder.com/v2/animals/", headers=headers,
                                 params=params).json()
        # this call gets the name of the photo from pulled data
        # we have to do it this way because this is how
        # we parse the information we get back
        animal_photo = response2['animals'][0]['photos'][0]['medium']
        return animal_photo

    def get_name(self, name):

        '''this method returns the name from the animal that was clicked on'''
        headers = {
            'Authorization': 'Bearer ' + self.auth_key
        }
        params = {
            'type': name
        }
        response3 = requests.get("https://api.petfinder.com/v2/animals/", headers=headers, params=params).json()
        # this call gets the name of the animal from pulled data
        # we have to do it this way because this is how
        # we parse the information we get back
        animal_name = response3['animals'][0]['name']
        return animal_name

    def get_description(self, description):

        '''this method gets the description from the animal that was clicked on'''
        headers = {
            'Authorization': 'Bearer ' + self.auth_key
        }
        params = {
            'type': description
        }
        response4 = requests.get("https://api.petfinder.com/v2/animals/", headers=headers, params=params).json()
        # this call gets the description of the animal from pulled data
        # we have to do it this way because this is how
        # we parse the information we get back
        description = response4['animals'][0]['description']
        return description

    def get_contact(self, contact):

        '''this method returns contact info from animal that was clicked on'''
        headers = {
            'Authorization': 'Bearer ' + self.auth_key
        }
        params = {
            'type': contact
        }
        response5 = requests.get("https://api.petfinder.com/v2/animals/", headers=headers, params=params).json()
        # this call gets the contact of the animal from the pulled data
        # we have to do it this way because this is how
        # we parse the information we get back
        animal_contact = response5['animals'][0]['contact']['email']
        return animal_contact
