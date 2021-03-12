# External Imports
import pygame
import sys
import math

# Local Imports
import frontend
import backend

# Initializing pygame

pygame.init()

# Global Constants

BG_COLOR = (255,255,255)
LOGIN_DIMENSIONS = (600,800)
CREATE_DIMENSIONS = (600,800)
APP_DIMENSIONS = (1600,800)

# Global Variables

logged_in = False
screen = pygame.display.set_mode(LOGIN_DIMENSIONS) # Initial state of screen for login

# Login Method Container Class
class LoginContainer:

    @classmethod
    def setup_login(cls):

        # Calls a setup function
        cls.username_login_box, cls.password_login_box = frontend.InstantiateFrontend.setup_login(screen, LOGIN_DIMENSIONS)

    @classmethod
    def draw_login(cls):    
        cls.username_login_box.draw()
        cls.password_login_box.draw()

    @classmethod
    def run_login(cls):
        pygame.Surface.fill(screen, BG_COLOR)
        cls.username_login_box.update()
        cls.password_login_box.update()

    @classmethod
    def draw_login_text(cls):
        FONT_TEXTBOX = pygame.font.Font("../dependencies/chrysuni.ttf", 30) # This is fairly ugly, but other solutions I've tried haven't worked

        screen.blit((
            FONT_TEXTBOX.render(
                "Login", 
                True, 
                (0,0,100),
                (255,255,255) 
            )), (math.floor(LOGIN_DIMENSIONS[0]/2) - 35, math.floor(LOGIN_DIMENSIONS[1]/6))
        )

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

        LoginContainer.run_login()
        LoginContainer.draw_login_text()
        pygame.display.flip()


if __name__ == '__main__':
    main()
    pygame.quit()