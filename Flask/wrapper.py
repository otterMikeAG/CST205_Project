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
		print('------------------')
		print(self.s_key)
		print('------------------')
		print(self.auth_key)
		print('------------------')
#used to get auth key from API 
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

	#preforms the api call to get all pets of specific type
	def get_pets(self, type):
		headers = {
			'Authorization': 'Bearer ' + self.auth_key
		}
		params = {
			'type': type
		}
		
		#this is the call to the API that I think is causing the error 
		response = requests.get('https://api.petfinder.com/v2/animals', headers=headers, params=params)
		print(response)
		print('--------------')
		returned = response.json()
		#print(returned)
		print('--------------')
		data_send = returned['animals']
		print(data_send)
		print('--------------')
		return data_send

	#supposed to show the pet's details when clicked
	def get_pet_by_id(self, id): #, name):

		headers = {
			'Authorization': 'Bearer ' + self.auth_key
		}

		params = {
			'photos': id
		}

		# params2 = {
		# 	'name': name
		# }

		#call to api
		response2 = requests.get("https://api.petfinder.com/v2/animals/", headers=headers, params=params).json()#, params2=params2).json()
		print(response2)
		print('^^^^^^^^^^^^^^^^ID response^^^^^^^^^^^^^^^^')
		# retrn = response2.json()
		print('^^^^^^^^^^^^^^^^ID response^^^^^^^^^^^^^^^^')
		animal_photo = response2['animals'][0]['photos'][0]['medium']
		#animal_name = response2['animals'][0]['name']
		print(animal_photo)
		#print(animal_name)
		print('^^^^^^^^^^^^^^^^Animal returned^^^^^^^^^^^^^^^^')
		return animal_photo
		#return animal_name


		# headers

		# headers = {
		# 	'Authorization': 'Bearer ' + self.auth_key
		# }
		# params = {
		# 	'id': id,
		# }
		# # params2 = {
		# # 	'description': description
		# # }
		#
		# # params = {
		# # 	'description': description
		# # }
		#
		# url = "https://api.petfinder.com/v2/animals/"
		# # url.format(44608234)
		#
		# response = requests.get(url, headers=headers, params=params).json()
		# # print('-------------')
		# pprint.pprint(response['animals'])
		#
		# data_send=[response['animals'][0]['photos'][0]['medium'], response['animals'][0]['name']]
		#
		#
		# return data_send


		




