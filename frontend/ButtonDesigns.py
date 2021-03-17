# External Package Imports
import pygame
import os

# Local Package Imports
import dependencies
import backend
import frontend

# Initialization of settings

dependencies.settings.init()

# Global Constants

TEXT_COLOR_FILL = (255,255,255)


# This class simply draws the button, 
# children will handle their own events

'''
Code is very similar to the Box class in box designs
Since, on a soley frontend level, a Button is effectively 
a less versitile box. As such this class is mostly the
Box skeleton, but with fewer variables 
'''
class Button(object):
    
    # Local Box Variables

    TEXT_SIZE = 15 # Denotes the text size

    # This creates a font which can be used to blit text to the screen
    BOX_FONT_TEXTBOX = pygame.font.Font("dependencies/chrysuni.ttf", TEXT_SIZE)

    def __init__(self, screen, pos: tuple, dim: tuple, text=""):
       
        # Initializing Cusomizable values

        self.text = text
        self.screen = screen
       
    # Getting the position of the Box

        self.x = pos[0]
        self.y = pos[1]

        # Getting the dimentions (dim) of the box

        self.height = dim[1]
        self.width = dim[0]

        #Initializing values

            # Constants

        self.UNACTIVE_COLOR = (0,0,0) # Colour when there is no box event
        self.ACTIVE_COLOR = (100,100,100) # Colour when there is a box event
        self.TEXT_SPACING = (9,7) # Spacing between text and walls of rect

            # Variables

        self.color = (0,0,0) # The color that is referenced in renders, changes on event to constants above 
        self.rect = pygame.Rect(pos[0], pos[1], dim[1], dim[0]) # Creates a pygame shell of a rectangle 

    # To be called once per frame.

    def update(self):
        text_position = (
            self.x + self.TEXT_SPACING[0], 
            self.y + self.TEXT_SPACING[1]
            ) # Defining the text position to keep it withing the rectandgle

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height) # Redefines the rect for new x, y, width, and height. As they may change
        pygame.draw.rect(self.screen, self.color, self.rect, 1) # Draws the rectangle to the screen
        self.screen.blit((
            self.BOX_FONT_TEXTBOX.render(
                self.text, True, self.color, TEXT_COLOR_FILL
            )), text_position
        ) # Adds text to the screen

    # To be called once. 
    # Simply performs any tasks intended to be done once

    def draw(self):
        # Draws the first box, 
        # This is done here to stop the screen from loading blank
        text_position = (
            self.rect.x + self.TEXT_SPACING[0], 
            self.rect.y + self.TEXT_SPACING[1]
            )

        pygame.draw.rect(self.screen, self.color, self.rect, 1)
        self.screen.blit((
            self.BOX_FONT_TEXTBOX.render(
                self.text, True, self.color, TEXT_COLOR_FILL
            )), text_position
        )
    
    def onHoverCheck(self, event):
        if event.type == pygame.MOUSEMOTION:
    
            # If the user is hovering over the button
            if self.rect.collidepoint(event.pos):
                self.color = self.ACTIVE_COLOR
            else:
                self.color = self.UNACTIVE_COLOR

class LoginButton(Button):
    def handle_event(self, event, username, password):
        self.onHoverCheck(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.color == self.ACTIVE_COLOR:
                # Runs a backend script which handles the database work
                if backend.FrontendHandlers.login_button_backend_handler(username, password):
                    user_id = backend.DatabaseHandler.get_id(username)[0][0]
                    f_name, s_name = backend.DatabaseHandler.get_name(username)
                    user = frontend.UserData.User(username, user_id, f_name[0][0], s_name[0][0])
                    return user
                
class CreateAccountFormButton(Button):
    def handle_event(self, event):
        self.onHoverCheck(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.color == self.ACTIVE_COLOR:
                # Change to create account form
                return True

class CreateAccountButton(Button):
    def handle_event(self, event, username, password, f_name, s_name):
        self.onHoverCheck(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.color == self.ACTIVE_COLOR:
                if backend.FrontendHandlers.create_account_backend_handler(username, password, f_name, s_name):
                    user_id = backend.DatabaseHandler.get_id(username)[0][0]
                    f_name, s_name = backend.DatabaseHandler.get_name(username)
                    user = frontend.UserData.User(username, user_id, f_name[0][0], s_name[0][0])
                    return user
                else:
                    pass

class EnterButton(Button):
    def handle_event(self, event, enter_button_instance):
        self.onHoverCheck(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                # character = backend.FrontendHandlers.enter_button_backend_handler()
                enter_button_instance.reset()
                # return character

class UserButton(Button):
    def handle_event(self, event):
        self.onHoverCheck(event)
        return None