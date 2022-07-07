import pygame
from pygame.locals import *

# initialisation of slider class. This class represents the abstract coordinate based slider, initialisation includes a maximum height and minimum;
# on top of this a current position is needed. From here the class can generate calculate if a user is dragging the slider

class Slider():


    def __init__(self):
        self.x = 178
        self.y = 24
        self.current = 24
        self.width = 18
        self.height = 5
        self.rect = (self.x,self.current,self.width,self.height)
        self.pressed_inside = False

    # This function has one main focus, this being allowing the user to drag the slider wherever they desire within the confines of the slider itself.

    def slide(self):
        
        pos = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        self.rect = (self.x,self.current,self.width,self.height)
        rect1 = list(self.rect)
        
        if pressed[0] == 1:
            if pos[0] > rect1[0] and pos[0] < rect1[0]+18 and pos[1] > rect1[1]-8 and pos[1] < rect1[1]+8 or self.pressed_inside == True:
                self.pressed_inside = True
                if rect1[1] <= 74 and rect1[1] >= 24:
                    if pos[1] <= 74 and pos[1] >= 24:
                        if pos[0] > rect1[0] and pos[0] < rect1[0]+18:
                            self.current = rect1[1] = pos[1]
            if pressed[0] == 0:
                self.pressed_inside = False

    # This function simply returns the current position of the slider.
    
    def return_pos(self):
        x = self.current
        return x
