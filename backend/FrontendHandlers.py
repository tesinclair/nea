# External Imports
from mss import mss
import os

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
  
  
# def enter_button_backend_handler():
#     with mss.mss() as sct:
#         monitor_dim = {"top": 485, "left": 375, "width": 150, "height": 150} 
#         c_out = "sct-{top}x{left}_{width}x{height}.png".format(**monitor_dim)
#         sct_img = sct.grab(monitor_dim)
#         mss.tools.to_png(sct_img.rgb, sct_img.size, output=c_out)
#         character = backend.OCR.image_to_text(c_out)
#         os.remove(c_out)
#         return character

def send_message(message, user, contact):
    backend.DatabaseHandler.add_message(message, user, contact)
