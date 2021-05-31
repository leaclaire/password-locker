import pyperclip
from user_details import User, Details

def create_user(fname,lname,password):
	'''
	Function to create a new user account
	'''
	new_user = User(fname,lname,password)
	return new_user

def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)


def verify_user(first_name,password):
	'''
	Function that verifies the existance of the user before creating details
	'''
	checking_user = Details.check_user(first_name,password)
	return checking_user

def generate_password():
	'''
	Function to generate a password automatically
	'''
	gen_pass = Details.generate_password()
	return gen_pass

def create_details(user_name,site_name,account_name,password):
	'''
	Function to create a new details
	'''
	new_details=details(user_name,site_name,account_name,password)
	return new_details

def save_details(details):
	'''
	Function to save a newly created details
	'''
	Details.save_details(details)

def display_details(user_name):
	'''
	Function to display details saved by a user
	'''
	return Details.display_details(user_name)
	
def copy_details(site_name):
	'''
	Function to copy a user details to the clipboard
	'''
	return Details.copy_details(site_name)

def main():
	print(' ')
	print('Welcome to Password Locker.')
	while True:
		print(' ')
		print("-"*60)
		print('Use these codes to navigate: \n ca-Create an Account \n lg-Log In \n ex-Exit')
		short_code = input('Enter a choice: ').lower().strip()
		if short_code == 'ex':
			break

		elif short_code == 'ca':
			print("-"*60)
			print(' ')
			print('To create a new account:')
			first_name = input('Enter your first name - ').strip()
			last_name = input('Enter your last name - ').strip()
			password = input('Enter your password - ').strip()
			save_user(create_user(first_name,last_name,password))
			print(" ")
			print(f'New Account Created for: {first_name} {last_name} using password: {password}')
		elif short_code == 'lg':
			print("-"*60)
			print(' ')
			print('To login, enter your account details:')
			user_name = input('Enter your first name - ').strip()
			password = str(input('Enter your password - '))
			user_exists = verify_user(user_name,password)
			if user_exists == user_name:
				print(" ")
				print(f'Welcome {user_name}. Please choose an option to continue.')
				print(' ')
				while True:
					print("-"*60)
					print('Navigation codes: \n cc-Create a detail \n dc-Display Details \n copy-Copy Password \n ex-Exit')
					short_code = input('Enter a choice: ').lower().strip()
					print("-"*60)
					if short_code == 'ex':
						print(" ")
						print(f'Goodbye {user_name}')
						break
					elif short_code == 'cc':
						print(' ')
						print('Enter your user details:')
						site_name = input('Enter the site\'s name- ').strip()
						account_name = input('Enter your account\'s name - ').strip()
						while True:
							print(' ')
							print("-"*60)
							print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
							psw_choice = input('Enter an option: ').lower().strip()
							print("-"*60)
							if psw_choice == 'ep':
								print(" ")
								password = input('Enter your password: ').strip()
								break
							elif psw_choice == 'gp':
								password = generate_password()
								break
							elif psw_choice == 'ex':
								break
							else:
								print('Wrong option entered.Please try again.')
						save_details(create_details(user_name,site_name,account_name,password))
						print(' ')
						print(f'Details Created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}')
						print(' ')
					elif short_code == 'dc':
						print(' ')
						if display_details(user_name):
							print('Here is a list of all your credentials')
							print(' ')
							for details in display_details(user_name):
								print(f'Site Name: {detail.site_name} - Account Name: {details.account_name} - Password: {details.password}')
							print(' ')	
						else:
							print(' ')
							print("You don't seem to have any details saved yet")
							print(' ')
					elif short_code == 'copy':
						print(' ')
						chosen_site = input('Enter the site name for the details password to copy: ')
						copy_details(chosen_site)
						print('')
					else:
						print('Wrong option entered.Please try again.')

			else: 
				print(' ')
				print('Wrong details entered. Try again or Create an Account.')		
		
		else:
			print("-"*60)
			print(' ')
			print('Wrong option entered.Please try again.')
				






if __name__ == '__main__':
	main()



