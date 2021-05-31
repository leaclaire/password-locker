import unittest
import pyperclip
from user_details import User, Detail

class TestUser(unittest.TestCase):
	'''
	Test class that defines test cases for the user class behaviours.

	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def setUp(self):
		'''
		Function to create a user account before each test
		'''
		self.new_user = User('Bernice','Twili','1234')

	def test__init__(self):
		'''
		Test to if check the initialization/creation of user instances is properly done
		'''
		self.assertEqual(self.new_user.first_name,'Leah')
		self.assertEqual(self.new_user.last_name,'Jepkorir')
		self.assertEqual(self.new_user.password,'1234')

	def test_save_user(self):
		'''
		Test to check if the new users info is saved into the users list
		'''
		self.new_user.save_user()
		self.assertEqual(len(User.users_list),1)

class TestDetails(unittest.TestCase):
	'''
	Test class that defines test cases for the details class behaviours.

	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def test_check_user(self):
		'''
		Function to test whether the login in function check_user works as expected
		'''
		self.new_user = User('Leah','Jepkorir','4874')
		self.new_user.save_user()
		user2 = User('Ken','Alex','5678')
		user2.save_user()

		for user in User.users_list:
			if user.first_name == user2.first_name and user.password == user2.password:
				current_user = user.first_name
		return current_user

		self.assertEqual(current_user,Detail.check_user(user2.password,user2.first_name))

	def setUp(self):
		'''
		Function to create an account's details before each test
		'''
		self.new_detail = Detail('leah','Instagram','leaclaire_ayabei','4874')

	def test__init__(self):
		'''
		Test to if check the initialization/creation of detail instances is properly done
		'''
		self.assertEqual(self.new_detail.user_name,'leah')
		self.assertEqual(self.new_detail.site_name,'instagram')
		self.assertEqual(self.new_detail.account_name,'leaclaire_ayabei')
		self.assertEqual(self.new_detail.password,'4874')

	def test_save_credentials(self):
		'''
		Test to check if the new detail info is saved into the details list
		'''
		self.new_detail.save_details()
		twitter = Detail('Claire','Twitter','leaclaire_ayabei','4874')
		twitter.save_details()
		self.assertEqual(len(Detail.details_list),2)

	# def test_generate_password(self):
	# 	'''
	# 	Test to check if the generate password generates 8 character long alphanumeric numbers
	# 	'''
	# 	self.twitter = Credential('Twitter','leaclaire','')
	# 	self.twitter.password = generate_password()
	# 	self.assertEqual()

	def tearDown(self):
		'''
		Function to clear the details list after every test
		'''
		Detail.details_list = []
		User.users_list = []

	def test_display_details(self):
		'''
		Test to check if the display_details method, displays the correct details.
		'''
		self.new_detail.save_details()
		twitter = Detail('Leaclaire','Twitter','Leaclaire_ayabei','4874')
		twitter.save_details()
		gmail = Detail('Leaclaire','Gmail','leaclaire_ayabei','4874')
		gmail.save_details()
		self.assertEqual(len(Detail.display_details(twitter.user_name)),2)

	def test_find_by_site_name(self):
		'''
		Test to check if the find_by_site_name method returns the correct detail
		'''
		self.new_detail.save_details()
		twitter = Detail('leaclaire','Twitter','leaclaire_ayabei','4874')
		twitter.save_details()
		detail_exists = Detail.find_by_site_name('Twitter')
		self.assertEqual(detail_exists,twitter)

	def test_copy_detail(self):
		'''
		Test to check if the copy a detail method copies the correct detail
		'''
		self.new_detail.save_details()
		twitter = Detail('leaclaire','Twitter','leaclaire_ayabei','4874')
		twitter.save_details()
		find_detail = None
		for detail in Detail.user_details_list:
				find_detail =Detail.find_by_site_name(detail.site_name)
				return pyperclip.copy(find_detail.password)
	Detail.copy_detail(self.new_detail.site_name)
		self.assertEqual('pswd100',pyperclip.paste())
		print(pyperclip.paste())

if __name__ == '__main__':
	unittest.main(verbosity=2)