# External Imports

# Local Imports
import backend


def login_button_backend_handler(username, password):
    # If the username exists
    if backend.DatabaseHandler.get_exists(username):
        if backend.DatabaseHandler.check_password(username, password):
            return True
    return False

def create_account_backend_handler(username, password, f_name, s_name):
    # If the username exists
    if backend.DatabaseHandler.get_exists(username):
        print("Username Already Exists")
        return False
    else:
        backend.DatabaseHandler.create_account(f_name, s_name, password, username)
        return True

def searchfor(text):
    return backend.DatabaseHandler.search(text)