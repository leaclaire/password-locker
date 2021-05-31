import pyperclip
from user_cdetails import User, Detail

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
	checking_user = Detail.check_user(first_name,password)
	return checking_user

def generate_password():
	'''
	Function to generate a password automatically
	'''
	gen_pass = Detail.generate_password()
	return gen_pass

def create_detail(user_name,site_name,account_name,password):
	'''
	Function to create a new detail
	'''
	new_detail=Detail(user_name,site_name,account_name,password)
	return new_detail

def save_detail(cdetail):
	'''
	Function to save a newly created detail
	'''
	Detail.save_details(detail)

def display_details(user_name):
	'''
	Function to display details saved by a user
	'''
	return Detail.display_details(user_name)
	
def copy_detail(site_name):
	'''
	Function to copy a users details to the clipboard
	'''
	return Detail.copy_detail(site_name)

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
					print('Navigation codes: \n cc-Create a Detail \n dc-Display CDetails \n copy-Copy Password \n ex-Exit')
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
						save_detail(create_detail(user_name,site_name,account_name,password))
						print(' ')
						print(f'Detail Created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}')
						print(' ')
					elif short_code == 'dc':
						print(' ')
						if display_details(user_name):
							print('Here is a list of all your details')
							print(' ')
							for detail in display_details(user_name):
								print(f'Site Name: {detail.site_name} - Account Name: {detail.account_name} - Password: {detail.password}')
							print(' ')	
						else:
							print(' ')
							print("You don't seem to have any details saved yet")
							print(' ')
					elif short_code == 'copy':
						print(' ')
						chosen_site = input('Enter the site name for the detail password to copy: ')
						copy_detail(chosen_site)
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

