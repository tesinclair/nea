# External Package Imports
import pygame
import os

# Local Package Imports
import dependencies

# Initialization of settings

dependencies.settings.init()

# Global Constants

TEXT_COLOR = (0,0,0)
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

    TEXT_SIZE = 25 # Denotes the text size

    # This creates a font which can be used to blit text to the screen
    BOX_FONT_TEXTBOX = pygame.font.Font(os.getenv("FONT_PATH"), TEXT_SIZE)

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

class LoginButton(Button):
    def handle_event(self, event):
        
