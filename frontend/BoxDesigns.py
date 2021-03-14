# External Package Imports
import pygame
import os

# Local Package Imports
import dependencies
import backend

# Initialization of settings

dependencies.settings.init()

# Global Constants

TEXT_COLOR = (0,0,0)
TEXT_COLOR_FILL = (255,255,255)


# This class simply draws the box, 
# children will handle their own events

class Box(object):

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
        self.ORIGINAL_TEXT = self.text # Used so that any box text canbe removed and replaces

            # Variables

        self.color = (0,0,0) # The color that is referenced in renders, changes on event to constants above 
        self.update_text = text # This value will be used to change the text
        self.rect = pygame.Rect(pos[0], pos[1], dim[1], dim[0]) # Creates a pygame shell of a rectangle 
        self.box_contents = "" # Used for returning the password and username 

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
                self.text, True, TEXT_COLOR, TEXT_COLOR_FILL
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
                self.text, True, TEXT_COLOR, TEXT_COLOR_FILL
            )), text_position
        )

    def get_dim(self): return (self.y, self.x)

    def get_text(self): return self.box_contents

# Child Input Box, 
# used for User Inputs In Japanese

class JapaneseInputBox(Box):
    def __init__(self, screen, pos: tuple, dim: tuple, text=""):
        super().__init__(screen, pos, dim, text=text)
        self.to_transliterate = "" # Should hole a maximum of 3 characters to transliterate
         
    
    '''

    While event handling isn't strictly frontend, 
    this directly effects the frontend in such a 
    way that encorparating it into the frontend was
    the only efficient solution.
    '''

    def handle_event(self, event, user, contact):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.text == self.ORIGINAL_TEXT: self.text = ""  # If the text is original
                self.color = self.ACTIVE_COLOR
            else:
                if self.text == "": self.text = self.ORIGINAL_TEXT # If the text is empty
                self.color = self.UNACTIVE_COLOR

        if event.type == pygame.KEYDOWN:

            if self.color == self.ACTIVE_COLOR:

                if event.key == pygame.K_RETURN:
                    try:
                        backend.SendMessageHandler.send_message(self.box_contents, user.get_username(), contact)
                    except TypeError as e: # If there is no instance of user this will throw a type error
                        print(e)

                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1] # Removes that last index
                    self.box_contents = self.box_contents[:-1]

                else:

                    '''
                    Here we need to check whether the typed character can be transliterated
                    If it can we should transliterate it, then remove characters from the list
                    '''
                    self.to_transliterate += event.unicode # Add letter to to_transliterate

                    transliterated = backend.HiraganaConversion.transliterate(self.to_transliterate) # returned value (text or None)
                    if transliterated: # if not none
                        self.text = self.text[:-len(self.to_transliterate)] # Remove the characters from to_transliterate
                        self.box_contents = self.box_contents[:-len(self.to_transliterate)]
                        self.to_transliterate = self.to_transliterate[:-len(self.to_transliterate)] # resets teh to transliterate

                        self.text += transliterated # Add transliterated character
                        self.box_contents += transliterated
                    else: # If the character couldn't be transliterateted
                        self.text += event.unicode # Just show the roman letter
                        self.box_contents += event.unicode



# Child Input Box, 
# used for User Inputs In English

class EnglishInputBox(Box):
    def __init__(self, screen, pos: tuple, dim: tuple, text="", box_type = "text"):
        super().__init__(screen, pos, dim, text=text)
        self.type = box_type

    def handle_event(self, event):
        # This will change whether the box is active or not
        if event.type == pygame.MOUSEBUTTONDOWN:

            # If collision is inside the rectangle
            if self.rect.collidepoint(event.pos):
                if self.text == self.ORIGINAL_TEXT: self.text = ""  # If the text is original
                self.color = self.ACTIVE_COLOR

            # If User clicked outside the rect
            else:
                if self.text == "": self.text = self.ORIGINAL_TEXT # If the text is empty
                self.color = self.UNACTIVE_COLOR
        
        # This will alter the contents of the box
        if event.type == pygame.KEYDOWN:
            # This checks if the box is active
            if self.color == self.ACTIVE_COLOR:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1] # Removes that last index
                    self.box_contents = self.box_contents[:-1]

                elif event.key == pygame.K_RETURN:
                    # If the user pressed return, we don't want anything to happen, 
                    # since this is a login form
                    pass 

                # If anything else is pressed
                else:
                    # Checks if the box type is password
                    if self.type == "password":
                        self.text += "*" # Adds an astrisk, so password cannot be seen
                        self.box_contents += event.unicode
                    else:
                        self.text += event.unicode
                        self.box_contents += event.unicode
        

# Child Draw Box, 
# used for drawing characters

class DrawBox(Box):
    def handle_event(self, event):
        pass

class MessageBox(Box):
    def handle_event(self, event):
        pass
