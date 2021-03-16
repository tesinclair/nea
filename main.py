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
APP_DIMENSIONS = (1200,800)

# Global Variables

login_form = False
create_account_form = False
app_form = True
screen = pygame.display.set_mode(LOGIN_DIMENSIONS) # Initial state of screen for login
user = frontend.UserData.User("username_test", "1", "f_name", "s_name")
contact = frontend.UserData.User("username_test_2")

# Login Method Container Class
class LoginContainer:

    # Fetches the class objects for the login boxes
    @classmethod
    def setup_login(cls):

        # Calls a setup function
        cls.username_login_box, cls.password_login_box, cls.button_login, cls.button_create_account_form = frontend.InstantiateFrontend.setup_login(screen, LOGIN_DIMENSIONS)
        cls.draw_login()
        pygame.display.flip()

    @classmethod
    def draw_login_text(cls):
        # Creates a font
        FONT_TEXTBOX = pygame.font.Font("dependencies/chrysuni.ttf", 30)

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
        cls.button_create_account_form.draw()

    @classmethod
    def run_login(cls):
        # Changes background color back to white (essentially clearing it)
        pygame.Surface.fill(screen, BG_COLOR)
        cls.username_login_box.update()
        cls.password_login_box.update()
        cls.button_login.update()
        cls.button_create_account_form.update()

    # I'd have liked to put this inside InstantiateFrontend, 
    # but it wouuld be bad to call an instantiation function as an update function...


    @classmethod
    def run_event_handler(cls, event):

         # Sends the event handler the event
        cls.password_login_box.handle_event(event)
        cls.username_login_box.handle_event(event)
        if cls.button_create_account_form.handle_event(event):
            login_form = False
            create_account_form = True
            CreateAccountContainer.setup_create_account()

        if cls.button_login.handle_event(
            event, 
            cls.username_login_box.get_text(), 
            cls.password_login_box.get_text()
        ):

            user = cls.button_login.handle_event(
            event, 
            cls.username_login_box.get_text(), 
            cls.password_login_box.get_text()
            )
            login_form = False
            app_form = True
            AppContainer.setup_app()


class CreateAccountContainer:
    @classmethod
    def setup_create_account(cls):

        # Calls a setup function
        cls.username_box, cls.password_box, cls.first_name_box, cls.last_name_box, cls.button_create_account = frontend.InstantiateFrontend.setup_create_account(screen, CREATE_DIMENSIONS)
        cls.draw_create()
        pygame.display.flip()

    @classmethod
    def draw_create_text(cls):
        # Creates a font
        FONT_TEXTBOX = pygame.font.Font(os.getenv("FONT_PATH"), 30)

        # Adds text to screen
        screen.blit((
            FONT_TEXTBOX.render(
                "Create Account", 
                True, 
                (0,0,100),
                (255,255,255) 
            )), (math.floor(LOGIN_DIMENSIONS[0]/2) + 20, math.floor(LOGIN_DIMENSIONS[1]/6))
        )
    
    @classmethod
    def draw_create(cls):    
        cls.username_box.draw()
        cls.password_box.draw()
        cls.first_name_box.draw()
        cls.last_name_box.draw()
        cls.button_create_account.draw()

    @classmethod
    def run_create(cls):
        # Changes background color back to white (essentially clearing it)
        pygame.Surface.fill(screen, BG_COLOR)
        cls.username_box.update()
        cls.password_box.update()
        cls.first_name_box.update()
        cls.last_name_box.update()
        cls.button_create_account.update()
    
    @classmethod
    def run_event_handler(cls, event):

         # Sends the event handler the event
        cls.username_box.handle_event(event)
        cls.password_box.handle_event(event)
        cls.first_name_box.handle_event(event)
        cls.last_name_box.handle_event(event)
        # Somehow returns a value even if not true. Check references
        if cls.button_create_account.handle_event(
            event, 
            cls.username_box.get_text(),
            cls.password_box.get_text(),
            cls.first_name_box.get_text(),
            cls.last_name_box.get_text()
        ):

            user = cls.button_create_account.handle_event(
            event, 
            cls.username_box.get_text(),
            cls.password_box.get_text(),
            cls.first_name_box.get_text(),
            cls.last_name_box.get_text()
            )
            create_account_form = False
            app_form = True
            AppContainer.setup_app()
        

class AppContainer:
    @classmethod
    def setup_app(cls):
        # Variable Setup
        cls.search_results = []

        # Calls a setup function
        cls.message_display_box, cls.search_box, cls.message_send_box, cls.draw_box, cls.draw_box_enter_button, cls.search_result_box = frontend.InstantiateFrontend.setup_app(screen, APP_DIMENSIONS)
        cls.draw_app()
        pygame.display.flip()

    @classmethod
    def draw_app_text(cls):
        # Creates a font
        FONT_TEXTBOX = pygame.font.Font(os.getenv("FONT_PATH"), 30)

        # Adds text to screen
        screen.blit((
            FONT_TEXTBOX.render(
                contact.get_username(), 
                True, 
                (0,0,100),
                (255,255,255) 
            )), (math.floor(APP_DIMENSIONS[0]/3) + 10, 20)
        )
        screen.blit((
            FONT_TEXTBOX.render(
                user.get_username(), 
                True, 
                (0,0,100),
                (255,255,255) 
            )), (math.floor(5*APP_DIMENSIONS[0]/6) + 20, 70)
        )
    
    @classmethod
    def draw_app(cls):    
        cls.message_display_box.draw()
        cls.search_box.draw()
        cls.message_send_box.draw()
        cls.draw_box.draw()
        cls.draw_box_enter_button.draw()
        cls.search_result_box.draw()

    @classmethod
    def run_app(cls):

        # Changes background color back to white (essentially clearing it)
        pygame.Surface.fill(screen, BG_COLOR)

        cls.message_display_box.update()
        cls.search_box.update()
        cls.message_send_box.update()
        cls.draw_box.update()
        cls.draw_box_enter_button.update()
        cls.search_result_box.update()

        for result in cls.search_results:
            print(result)
            result.update()
    
    @classmethod
    def run_event_handler(cls, event):

        # Sends the event handler the event
        cls.search_results = []
        results = [result for result in cls.search_box.handle_event(event)]
        if len(results) > 0:
            for result in results:
                cls.search_results.append(result)

        cls.message_send_box.handle_event(event, user, contact)
        cls.draw_box.handle_event(event)
        cls.draw_box_enter_button.handle_event(event)
        cls.message_display_box.handle_event(event)

        for result in cls.search_results:
            result.handle_event(event)


# Main Script

def main():
    if login_form:
        LoginContainer.setup_login()
    
    elif create_account_form:
        CreateAccountContainer.setup_create_account()

    elif app_form:
        AppContainer.setup_app()

    while True:

        # If the user is on the login form (True by default)
        if login_form:

            # Loops through a list of events
            for event in pygame.event.get():
                # If the page is closed
                if event.type == pygame.QUIT:
                    sys.exit()
                else:
                    LoginContainer.run_event_handler(event)

            LoginContainer.run_login()
            LoginContainer.draw_login_text()
            pygame.display.flip()

        # If the user is on the create account form
        elif create_account_form:
            screen = pygame.display.set_mode(CREATE_DIMENSIONS)

            # Loops through a list of events
            for event in pygame.event.get():
                # If the page is closed
                if event.type == pygame.QUIT:
                    sys.exit()
                else:
                    CreateAccountContainer.run_event_handler(event)

            CreateAccountContainer.run_create()
            CreateAccountContainer.draw_create_text()
            pygame.display.flip()

        # If the user is on the main app form
        elif app_form:
            screen = pygame.display.set_mode(APP_DIMENSIONS)

            # Loops through a list of events
            for event in pygame.event.get():
                # If the page is closed
                if event.type == pygame.QUIT:
                    sys.exit()
                else:
                    AppContainer.run_event_handler(event)

            AppContainer.run_app()
            AppContainer.draw_app_text()
            pygame.display.flip()
        


if __name__ == '__main__':
    main()
    pygame.quit()
