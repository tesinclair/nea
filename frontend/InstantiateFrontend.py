# External Imports
import pygame
import math

# Local Imports
import frontend

# Initialise pygame

pygame.init()

def setup_login(screen, dim: tuple):
    # Constant Values

    BOX_SPACING = 10
    SIZE = 30
    FONT_TEXTBOX = pygame.font.Font("../dependencies/chrysuni.ttf", SIZE)
    LOGIN_TEXT_COLOR = (0,0,55)
    TEXT_BG_COLOR = (255,255,255)


    # Gets Dimensions

    height = dim[0]
    width = dim[1]

    # Username Box

    username_box_login = frontend.BoxDesigns.EnglishInputBox(
        screen, 
        (30,60), 
        (math.floor(height/4), math.floor(width/6)), 
        text="Username..."
        )

    # Password Box

    password_box_login = frontend.BoxDesigns.EnglishInputBox(
        screen, 
        (30,60), 
        (math.floor(height/4) + username_box_login.get_dim()[0] + BOX_SPACING, 100), 
        text="Password...",
        type="password"
        )
    
    # Returns the instances

    return username_box_login, password_box_login