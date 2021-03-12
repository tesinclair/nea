from frontend import Box
import pygame

def setup_login(screen, dim: Tuple):
    # Constant Values

    BOX_SPACING = 10

    # Gets Dimensions

    height = dim[0]
    width = dim[1]

    # Creates Login text



    # Username Box

    username_box_login = Box.EnglishInputBox(
        screen, 
        (height/4, width/6), 
        (30,60), 
        text="Username..."
        )

    # Password Box

    password_box_login = Box.EnglishInputBox(
        screen, 
        (height/4 + username_box_login.get_dim[0] + BOX_SPACING, 100), 
        (30,60), 
        text="Password...",
        type="password"
        )
    
    # Returns the instances

    return username_box_login, password_box_login
    
