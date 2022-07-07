
from pygame.locals import *
import math
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
man = (1000,1000)
screen = pygame.display.set_mode((850, 720))

# This function returns the lowest y coordinate that is not inside the terrain bitmap given an x coordinate.

def getLowestAir(x,y):
    while True:
        try:
            current = screen.get_at((x,y))
        except IndexError:
            current = (0,434)
        if current == (255,255,255):
            y += 1
        else:
            break
    return y

# This function returns the gradient given two coordinates in a euclidian 2d plane.

def surface_normal_avg(x,y):
    h = 22
    x += 20
    xa,ya = x,y
    x1 = x-h
    x2 = x+h
    y1 = getLowestAir(x1,y)
    y2 = getLowestAir(x2,y)
    grad = (180/math.pi)*(math.atan((y1-y2)/(x1-x2)))
    return grad
