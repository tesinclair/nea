#External Package Imports
import pygame

# Global Variables

TEXT_COLOR = (0,0,0)
TEXT_COLOR_FILL = ()


# This class simply draws the box, 
# children will handle their own events

class Box(object):
    def __init__(self, screen, pos: Tuple, dim: Tuple, text=""):
       
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

        self.unactive_color = (0,0,0)
        self.active_color = (100,100,100)
        self.update_text = self.text # This value will be used to change the text
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


    def update(self):
        pass

    def draw(self):
        pass

# Child Input Box, used for User Inputs In Japanese

class JapaneseInputBox(Box):

    '''
    While event handling isn't strictly frontend, 
    this directly effects the frontend in such a 
    way that encorparating it into the frontend was
    the only efficient solution.
    '''

    def handle_event(self, event):
        pass

# Child Input Box, used for User Inputs In English

class EnglishInputBox(Box):
    def handle_event(self, event):
        pass

# Child Draw Box, used for drawing characters

class DrawBox(Box):
    def handle_event(self, event):
        pass
