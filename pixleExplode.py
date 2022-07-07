import pygame
from pygame.locals import *
import math
import random
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
man = (1000,1000)
screen = pygame.display.set_mode((850, 720))

# This function takes a radius, and an x,y coordinate as arguements, From here
# it will give you a list of pixels that lie inside the radius of the circle
# at coordinates x,y for radius r.

def calc_rad_pix(x1,y1,r,complete):
    p1 = r-(r*2)-r
    p2 = r+2
    inside_pix = []
    for x3 in range(p1,p2):
        for y3 in range(p1,p2):
            x2 = x1+x3
            y2 = y1+y3
            try:
                d = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
                if d < r and screen.get_at((x2,y2)) != (255,255,255):
                    inside_pix.append([(x2,y2),0])
            except IndexError:
                None
                

    complete = True
    return inside_pix,complete


# This function simply moves a pixel from one place to another.

def move_pix(xy0,xy1):
    colour = screen.get_at(xy0)
    screen.set_at(xy0,(255,255,255))
    screen.set_at(xy1,(colour))
    return colour


# This function generates a trajectory for a pixel to take to end up at a
# specified coordinate

def line(x0, y0, x1, y1):
    LINE_LIST = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x, y = x0, y0
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1
    if dx > dy:
        err = dx / 2.0
        while x != x1:
            LINE_LIST.append((x,y))
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y1:
            LINE_LIST.append((x,y))
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy        
    LINE_LIST.append((x,y))
    return LINE_LIST


# this function generates trajectorys for all the pixels in the given array, from here it adds the trajectroy list to another list containing all the
# pixels, the index that it is places in corresponds with 

def animate_pix(pix_list):
    for i in range(0,len(pix_list)-1):
        current_xy = pix_list[i][0]
        current_xy = list(current_xy)
        cast_traj = line(current_xy[0],current_xy[1],random.randint(0,850),0)
        pix_list[i][1] = cast_traj
    
    return pix_list

# This function moves all pixels in the explosion list one index up their trajectory lists every frame until all of them have reached their final index.

def construct_exp(pix_list,count):
    for i in range(0,len(pix_list)):
        try:
            move_pix(pix_list[i][0],pix_list[i][1][count])
        except:
            None
    return pix_list
