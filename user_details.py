import pyperclip
import random
import string

# Global Variables
global users_list 
class User:
	'''
	Class to create user accounts and save their information
	'''
	# Class Variables
	# global users_list
	users_list = []
	def __init__(self,first_name,last_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.first_name = first_name
		self.last_name = last_name
		self.password = password

	def save_user(self):
		'''
		Function to save a newly created user instance
		'''
		User.users_list.append(self)
		
class Detail:
	'''
	Class to create  account details, generate passwords and save their information
	'''
	# Class Variables
	details_list =[]
	user_details_list = []
	@classmethod
	def check_user(cls,first_name,password):
		'''
		Method that checks if the name and password entered match entries in the users_list
		'''
		current_user = ''
		for user in User.users_list:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user

	def __init__(self,user_name,site_name,account_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.user_name = user_name
		self.site_name = site_name
		self.account_name = account_name
		self.password = password

	def save_details(self):
		'''
		Function to save a newly created user instance
		'''
		# global users_list
		Detail.details_list.append(self)
	
	def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
		'''
		Function to generate an 8 character password for a detail
		'''
		gen_pass=''.join(random.choice(char) for _ in range(size))
		return gen_pass

	@classmethod
	def display_deatails(cls,user_name):
		'''
		Class method to display the list of details saved
		'''
		user_details_list = []
		for detail in cls.details_list:
			if detail.user_name == user_name:
				user_details_list.append(detail)
		return user_details_list
				

	
	@classmethod
	def find_by_site_name(cls, site_name):
		'''
		Method that takes in a site_name and returns a detail that matches that site_name.
		'''
		for detail in cls.details_list:
			if detail.site_name == site_name:
				return detail

	@classmethod
	def copy_detail(cls,site_name):
		'''
		Class method that copies a details info after the details site name is entered
		'''
		find_detail = Detail.find_by_site_name(site_name)
		return pyperclip.copy(find_detail.password)

