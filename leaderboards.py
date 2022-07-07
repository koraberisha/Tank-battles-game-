import csv
import pygame
from pygame.locals import *
import math
import random
import sys
from deDec import de
from heapSort import sortFromTwoArr

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
man = (1000,1000)
screen = pygame.display.set_mode((850, 720))
pygame.font.init()


# This class sets up the other class by declaring procedures in which the programme can interface with a csv file, writing and reading from it at choice.

class csvManipulate():
    
    def __init__(self):
        self.listo = []
        self.dir = "bin/csvs/madting.csv"
        self.ofile = 0
        self.writer = 0

    def loadCSV(self):
        file = open(self.dir,"r")
        fileReader = csv.reader(file,delimiter=",")
        fileList = []
        for row in fileReader:
            fileList.append(row)

        file.close()
        return fileList

    def loadWrite(self):
        self.ofile = ifile  = open(self.dir, "a")
        self.writer = csv.writer(self.ofile, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)

    def closeWrite(self):
        self.ofile.close()

    # This procedure is used to make a single entry into the file.

    def entry(self,inp):
        self.writer.writerow(inp)

    # This procedure is used to make multiple entrys at once into the file as a list.

    def entryMultiple(self,inp):
        for i in range(len(inp)):
            self.writer.writetow(inp[i])


cs = csvManipulate()
leaderListNU= cs.loadCSV()


# This class is used for the Leaderboard in the end of the game, initialising here.

class leaderboardSetup(object):

    def __init__(self):
        self.backImg = pygame.image.load("bin/lead/bacc.jpg")
        self.csv = csvManipulate()
        self.leaderList= leaderListNU
        self.ifo = False
    

    # This function removes all empty spaces in the list to make the sorting more efficient.
    
    def fixList(self,ifs):
        for i in range(len(self.leaderList)):
            try:
                if self.leaderList[i][0] == "" or len(self.leaderList[i]) == 0 or self.leaderList[i][1] < 100:
                    self.leaderList.remove(self.leaderList[i])
            except:
                None

        madting = [e for e in self.leaderList if e]
        self.leaderList = madting
                
        ifs = True
        return ifs
            

    # This function generates a line in the leaderboard, containing a score, name and ordinal value. It handles one line at a time.
    
    def constructLine(self,coord,pos):
        rect = coord
        myfont = pygame.font.SysFont("monospace", 17)

        try:
            curPos = pos
            pygame.draw.rect(screen,WHITE,(rect[0]-3,rect[1]-1,344,20),0)   
            posTxt = myfont.render(str(curPos+1),12,(0,100,60))
            screen.blit(posTxt,(rect[0],rect[1]-4))
            current = self.leaderList[pos][0]
            currentSco = self.leaderList[pos][1]
            name = myfont.render(current,12,(0,100,60))
            sco = myfont.render(de(str(currentSco)),12,(0,100,60))
            screen.blit(name,(rect[0]+(17*3)+5,rect[1]-1))
            screen.blit(sco,(rect[0]+(12*8)+(17*3)+5,rect[1]-1))
            
                
        except IndexError:
            None

    # This procedure runs the "constructLine" function 23 times for each index(player) that reaches the top part of the leaderboard  

    def loadLeader(self):
        screen.blit(self.backImg,(0,0))
        pygame.draw.rect(screen,(120,100,210),(220,70,400,550),0)
        noLines = 23
        if self.ifo == False:
            self.ifo = self.fixList(self.ifo)
            self.leaderList = sortFromTwoArr(self.leaderList)
            self.leaderList.reverse()

        self.constructLine((220+25,70+24),0)
        for i in range(1,noLines):
            xint = 70+24+(i*int((15)*1.5))
            self.constructLine((220+25,xint),i)

            
            
            
            
            

    
            
            
            
            
            
            


