# External Package Imports
import pygame

# Initialise pygame

pygame.init()

# Global Constants

TEXT_COLOR = (0,0,0)
TEXT_COLOR_FILL = (255,255,255)


# This class simply draws the box, 
# children will handle their own events

class Box(object):

    # Local Box Variables

    TEXT_SIZE = 20 # Denotes the text size

    # This creates a font which can be used to blit text to the screen
    BOX_FONT_TEXTBOX = pygame.font.Font("../dependencies/chrysuni.ttf", TEXT_SIZE)

    def __init__(self, screen, pos: tuple, dim: tuple, text=""):
       
        # Initializing Cusomizable values

        self.text = text
        self.screen = screen
       
    # Getting the position of the Box

        self.x = pos[0]
        self.y = pos[1]

        # Getting the dimentions (dim) of the box

        self.height = dim[0]
        self.width = dim[1]

        #Initializing values

            # Constants

        self.UNACTIVE_COLOR = (0,0,0)
        self.ACTIVE_COLOR = (100,100,100)
        self.TEXT_SPACING = (9,7)

            # Variables

        self.color = (0,0,0)
        self.update_text = text # This value will be used to change the text
        self.rect = pygame.Rect(pos[0], pos[1], dim[0], dim[1])

    # To be called once per frame.

    def update(self):
        text_position = (
            self.x + self.TEXT_SPACING[0], 
            self.y + self.TEXT_SPACING[1]
            )

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, self.color, self.rect, 1)

        self.screen.blit((
            self.BOX_FONT_TEXTBOX.render(
                self.text, True, TEXT_COLOR, TEXT_COLOR_FILL
            )), text_position
        )

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

# Child Input Box, 
# used for User Inputs In Japanese

class JapaneseInputBox(Box):

    '''
    While event handling isn't strictly frontend, 
    this directly effects the frontend in such a 
    way that encorparating it into the frontend was
    the only efficient solution.
    '''

    def handle_event(self, event):
        pass

# Child Input Box, 
# used for User Inputs In English

class EnglishInputBox(Box):
    def __init__(self, screen, pos: tuple, dim: tuple, text="", type = "text"):
        super().__init__(screen, pos, dim, text="")
        self.type = type

    def handle_event(self, event):
        pass

# Child Draw Box, 
# used for drawing characters

class DrawBox(Box):
    def handle_event(self, event):
        pass
