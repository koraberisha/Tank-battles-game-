import pygame
import random
import os
import math
import sys
from pygame.locals import *
from proj_motion import *
import random
from math import *
import time
from stack import Stack

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
man = (1000,1000)
screen = pygame.display.set_mode((850, 720))

# Initialising tank class


class Tank():
    
    def __init__(self):
        self.Tank_main = pygame.image.load('bin/recources/Tank_Main.png').convert_alpha()
        self.tank_height = 17
        self.tank_width = 42
        self.tank_health = 115
        self.t_angle = 0
        self.image = pygame.Surface([self.tank_width, self.tank_height])
        self.rect = self.image.get_rect()
        self.image.fill(WHITE)
        self.Tank_gun = pygame.image.load("bin/recources/Tank_Gun.png").convert_alpha()
        self.grect = self.Tank_gun.get_rect()
        self.rand_pos = random.randint(0,750)
        self.Tank_x = self.rand_pos
        self.Tank_y = 400
        self.angle = 0
        self.shell_angle = 0
        self.u = 0
        self.gunx_offset = 33
        self.guny_offset = 5
        self.v = 80
        self.accuracyList = []
        

    #function to allow movement of the x position of the tank image depending o the user input
        
    def move(self,direction,x_checked):
        n = 0
        if direction == 0:
            n += -0.7
        else:
            n += 0.7
        self.Tank_x += n
        self.tank_collision()
        screen.blit(self.Tank_main, (self.Tank_x,self.Tank_y-(self.tank_height/2)))
        x_checked = False
        return x_checked

    # this procedure is involved in the calculation of game score, includng average accuracy of shots calculations.

    def calcAccuracy(self,poi,oppx):
        dist = poi[0]-oppx
        dist = abs(dist)
        if dist <= 100:
            self.accuracyList.append(dist)
        else:
            self.accuracyList.append(100)
        
    
    #function to handle the changing of the gun angle depending on the users input

    def gun_angle(self):
        if self.u == 0:
            self.angle += 1.2
        elif self.u == 1:
            self.angle -= 1.2
        else:
            self.angle = 0
        return self.angle


    #this handles the changing of the angle of the shell angle required for the equation for the projectile motion porabola

    def gun_angle_2(self):
        if self.u == 0:
            self.shell_angle -= 1.2 
        elif self.u == 1:
            self.shell_angle += 1.2
        else:
            self.angle = 0
        return self.shell_angle

    # This function renders the tanks gun wherever it needs to be, this is a necessary seperate procedure due to the way the user controlls
    # the tanks gun angle.
  
    def gun_blit(self,tank_gun,x,y):
        rect = tank_gun.get_rect(center=(self.Tank_x+self.gunx_offset-4,self.Tank_y+6))
        screen.blit(tank_gun, rect)
        return rect

    # This procudure handles the collision between the tank class and the edges of the map itself (the walls).
    
    def tank_collision(self):
        if self.Tank_x+(self.tank_width) >= 849:
            self.Tank_x -= 1
        if self.Tank_x <= 1:
            self.Tank_x += 1
