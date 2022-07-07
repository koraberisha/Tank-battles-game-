import pygame
from pygame.locals import *



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
man = (1000,1000)
screen = pygame.display.set_mode((850, 720))

#this function is an algorithm that uses the screen.get_at function. to calculate the distance from one pixel at
#a set height. this gave a distance from this number to the closest pixel that is on the ground. this allows the
#programme to subtract this number from the x coordinate of the tank. this gives the illusion of the tank
#image traversing the ground image.

def pixl_chec(m):
    dist_list = []
    print("reading map")
    for i in range(0,850):
        n_temp = 0
        dist_list.append([n_temp,i])
        for y in range(400,620):
            current = screen.get_at((i,y))
            if current == (255,255,255,255):
                n_temp += 1  
            dist_list[i][0] = n_temp
    m = True
    return dist_list,m



# This function works as a workaround for pixel-perfect collision detectiion, making a distinction between terrain and non terrain pixels returning a
# boolean variable for collided or not.

def newPixCol(tup,mapix):
    currentx = tup[0]
    try:
        if tup[1] >= mapix[currentx]:
            pixCol = True
        else:
            pixCol = False
    except IndexError:
        pixCol = False

    pixpos = tup

    return pixCol,pixpos
        

