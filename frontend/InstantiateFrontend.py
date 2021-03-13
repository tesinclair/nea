# External Imports
import pygame
import math
import os

# Local Imports

import dependencies
import frontend

# Initialization of settings

dependencies.settings.init()

# Constant Global Values

BOX_SPACING = 10
SIZE = 30
FONT_TEXTBOX = pygame.font.Font(os.getenv("FONT_PATH"), SIZE)
LOGIN_TEXT_COLOR = (0,0,55)
TEXT_BG_COLOR = (255,255,255)

# Instantiates all the login class variables

def setup_login(screen, dim: tuple):


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

    # Create Account Button

    button_create_account_form = frontend.ButtonDesigns.CreateAccountFormButton(
        screen, 
        (math.floor(1*width/3) - 10, math.floor(5*height/6)),
        (145,30),
        text="Create Account"
    )
    
    # Returns the instances

    return username_box_login, password_box_login, button_login, button_create_account_form

# Instantiate All the Create account class variables

def setup_create_account(screen, dim: tuple):

    # Gets Dimensions

    height = dim[1]
    width = dim[0]

    # Username Box

    username_box = frontend.BoxDesigns.EnglishInputBox(
        screen, 
        (math.floor(width/2), math.floor(height/3) + 120), 
        (200,30), 
        text="Username..."
        )

    # Password Box

    password_box = frontend.BoxDesigns.EnglishInputBox(
        screen, 
        (math.floor(width/2), math.floor(height/3) + 180), 
        (200,30), 
        text="Password...",
        box_type="password"
        )
    
    # First Name Box

    first_name_box = frontend.BoxDesigns.EnglishInputBox(
        screen, 
        (math.floor(width/2), math.floor(height/3)), 
        (200,30), 
        text="First Name..."
        )
    
    # Last Name Box

    last_name_box = frontend.BoxDesigns.EnglishInputBox(
        screen, 
        (math.floor(width/2), math.floor(height/3) + 60), 
        (200,30), 
        text="Last Name"
        )


    # Create Account Button

    button_create_account = frontend.ButtonDesigns.CreateAccountButton(
        screen, 
        (math.floor(width/2) + 20, math.floor(5*height/6)),
        (145,30),
        text="Create Account"
    )
    
    # Returns the instances

    return username_box, password_box, first_name_box, last_name_box, button_create_account