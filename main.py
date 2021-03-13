# External Imports
import pygame
import sys
import os
import math

# Local Imports
import frontend
import backend
import dependencies

# Initializing settings

dependencies.settings.init()

# Global Constants

BG_COLOR = (255,255,255)
LOGIN_DIMENSIONS = (400,600)
CREATE_DIMENSIONS = (600,800)
APP_DIMENSIONS = (1600,800)

# Global Variables

logged_in = False
screen = pygame.display.set_mode(LOGIN_DIMENSIONS) # Initial state of screen for login

# Login Method Container Class
class LoginContainer:

    # Fetches the class objects for the login boxes
    @classmethod
    def setup_login(cls):

        # Calls a setup function
        cls.username_login_box, cls.password_login_box, cls.button_login = frontend.InstantiateFrontend.setup_login(screen, LOGIN_DIMENSIONS)

    @classmethod
    def draw_login_text(cls):
        # Creates a font
        FONT_TEXTBOX = pygame.font.Font(os.getenv("FONT_PATH"), 30)

        # Adds text to screen
        screen.blit((
            FONT_TEXTBOX.render(
                "Login", 
                True, 
                (0,0,100),
                (255,255,255) 
            )), (math.floor(LOGIN_DIMENSIONS[0]/2) - 40, math.floor(LOGIN_DIMENSIONS[1]/6))
        )

    @classmethod
    def draw_login(cls):    
        cls.username_login_box.draw()
        cls.password_login_box.draw()
        cls.button_login.draw()

    @classmethod
    def run_login(cls):
        # Changes background color back to white (essentially clearing it)
        pygame.Surface.fill(screen, BG_COLOR)
        cls.username_login_box.update()
        cls.password_login_box.update()
        cls.button_login.update()

    # I'd have liked to put this inside InstantiateFrontend, 
    # but it wouuld be bad to call an instantiation function as an update function...


    @classmethod
    def run_event_handler(cls, event):
         # Sends the event handler the event
        cls.password_login_box.handle_event(event)
        cls.username_login_box.handle_event(event)
        cls.button_login.handle_event(event)

# Main Script

def main():
    if not logged_in:
        LoginContainer.setup_login()
        LoginContainer.draw_login()
        pygame.display.flip()

    while not logged_in:
        # Loops through a list of events
        for event in pygame.event.get():
            # If the page is closed
            if event.type == pygame.QUIT:
                sys.exit()
            if not logged_in:
                LoginContainer.run_event_handler(event)

        LoginContainer.run_login()
        LoginContainer.draw_login_text()
        pygame.display.flip()


if __name__ == '__main__':
    main()
    pygame.quit()