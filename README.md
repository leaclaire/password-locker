# Password-Locker

## Description
Password-Locker is an terminal run application that helps users manage their passwords and even generate new passwords.

## Features the application implements
A user is able to:

* create an account
* store existing login information
* generate a password for a new account
* copy the credentials to the clipboard

## Instructions
| Feature | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **In terminal: $./password-locker.py** | Welcome, choose an option: ca-Create Account, lg-Log In, ex-Exit |
| Display prompt for creating an account | **Enter: ca** | Enter your first name, last name and password |
| Display prompt for login in | **Enter: li** | Enter your account name and password |
| Display codes for navigation | **Successful login** | Choose an option: cc - Create Credential, dc - Display Credentials, copy - Copy Credential, ex - exit |
| Display prompt for creating a credential | **Enter: cc** | Enter the site name, your username and password |
| Display a list of credentials | **Enter: dc** | Prints a list of saved credentials |
| Display prompt for which credential to copy | **Enter: copy** | Enter the site name of the credential you wish to copy. |
| Exit application | **Enter: ex** | Exit the current navigation stage |

## Installation Requirements
### Prerequisites
* python3.6
* pip
* pyperclip
* xclip
### Cloning
* In your terminal:
        
        $ git clone https://github.com/leaclaire/password-locker.git/
        $ cd Password-Locker
        
## Running the Application
* To run the application, in your terminal:

        $ chmod +x password-locker.py
        $ ./password-locker.py
        
## Testing the Application
* To run the tests for the class file:

        $ python3.8 user_credentials_test.py
        
## Technologies Used
* Python3.8

## License & copyright
© Leah jepkorir,Moringa School

Licensed under the [MIT License](LICENSE).