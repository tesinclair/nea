# External Imports
import pygame
import math
import os

# Local Imports

import dependencies
import frontend

# Initialization of settings

dependencies.settings.init()

# Instantiates all the login class variables

def setup_login(screen, dim: tuple):
    # Constant Values

    BOX_SPACING = 10
    SIZE = 30
    FONT_TEXTBOX = pygame.font.Font(os.getenv("FONT_PATH"), SIZE)
    LOGIN_TEXT_COLOR = (0,0,55)
    TEXT_BG_COLOR = (255,255,255)


    # Gets Dimensions

    height = dim[1]
    width = dim[0]

    # Username Box

    username_box_login = frontend.BoxDesigns.EnglishInputBox(
        screen, 
        (math.floor(width/4), math.floor(height/3)), 
        (200,30), 
        text="Username..."
        )

    # Password Box

    password_box_login = frontend.BoxDesigns.EnglishInputBox(
        screen, 
        (math.floor(width/4), math.floor(height/3) + 60), 
        (200,30), 
        text="Password...",
        box_type="password"
        )

    # Login Button

    button_login = frontend.ButtonDesigns.LoginButton(
        screen, 
        (math.floor(width/2) - 40, math.floor(5*height/9) - 20),
        (60,30),
        text="Login"
    )
    
    # Returns the instances

    return username_box_login, password_box_login, button_login