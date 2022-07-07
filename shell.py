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


class Shell():
    
    def __init__(self):
        self.map = 0

    # This function runs through the trajectory list and moves the shell through each index(tuple coordinate) until it reaches the final one or a collision
    # occurs.
     
    def fireShell(self,tList,count,count_goal,fired):
        man = (1000,1000)
        if count <= count_goal:
            try:
                n = list(tList[count])
                pygame.draw.circle(screen, BLACK, (int(n[0]),int(n[1]))  , 2, 0)
                count = count 
                man = (int(n[0]),int(n[1]))   
            except:
                None
            if count == (count_goal-1):
                fired = False
                count = 0
        return count,fired,man

    
    # This function runs through the trajectory list and moves the shell through each index(tuple coordinate) until it reaches the final one or a collision
    # occurs, however this shell is invisible and is simply semantic. It is used for cslculations and collisions.

    def fireShell_i(self,tList,count,count_goal,fired):
        man = (1000,1000)
        if count <= count_goal:
            try:
                n = list(tList[count])
                count = count + 1
                man = (int(n[0]),int(n[1]))   
            except:
                None
            if count == (count_goal-1):
                fired = False
                count = 0
        return count,fired,man

    ################## ▼▼RESEARCH & TESTING▼▼ ###################
               
    def vel_increase(self,health,turn):
        pos = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        x3 = pygame.draw.rect(screen, (0,0,255), (700,120,20,10), 0)
        x4 = pygame.draw.rect(screen, (0,255,0), (700,150,20,10), 0)
        
        if pos[0] >700 and pos[0] < 720 and pos[1] > 120 and pos[1] < 130:
            x3 = pygame.draw.rect(screen, (0,0,175), (700,120,20,10), 0)
            if press[0] == True:
                health -= 1

        if pos[0] >700 and pos[0] < 720 and pos[1] > 150 and pos[1] < 160:
            x4 = pygame.draw.rect(screen, (0,175,0), (700,150,20,10), 0)
            if press[0] == True:
                if turn == 0:
                    turn = 1
                else:
                    turn = 0
                time.sleep(0.2)
                
        return health,turn

    ################## ▲▲RESEARCH & TESTING▲▲ ###################

