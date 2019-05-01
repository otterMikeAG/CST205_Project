import requests, json


class Petfinder():
	def __init__(self, c_key, s_key):
		'''this will initialize the client key and secret key.'''
		self.c_key = c_key
		self.s_key = s_key
		self.auth_key = 'need'


	def get_auth(self):
		data = {
			'grant_type': 'client_credentials',
			'client_id': self.c_key,
			'client_secret': self.s_key
		}
		response = requests.post('https://api.petfinder.com/v2/oauth2/token', data=data)
		if(response):
			returned = response.json()
			self.auth_key = returned['access_token']


	def get_pets(self, type):
		headers = {
			'Authorization': 'Bearer ' + self.auth_key
		}
		params = (
				('type', type)
			)
		response = requests.get('https://api.petfinder.com/v2/animals', headers=headers, params=params)
		if(response):
			returned = response.json()
			return returned
		




		