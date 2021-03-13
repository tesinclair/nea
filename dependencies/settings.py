# sETTINGS.PY this runs all the necessary code for initializations used across files

from dotenv import load_dotenv
import pygame

# Initialzises all dependencies used

def init():
    pygame.init()
    load_dotenv(dotenv_path="../.env")