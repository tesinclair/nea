# External Imports

# Local Imports
# External Imports
import backend


def login_button_backend_handler(username, password):
    # If the username exists
    if backend.DatabaseHandler.get_exists(username):
        return True
    return False