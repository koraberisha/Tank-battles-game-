from pygame.locals import *
import pygame
import random



class artificialIntelligence():

    def __init__(self,opp_x,opp_y,x,y,health):
        self.opp_x = opp_x
        self.opp_y = opp_y
        self.timeCheck = False
        self.tim0 = 0
        self.tim1 = 1
        self.x = x
        self.y = y
        self.skillChoice = 0
        self.skillList = [[1,False],[2,False],[3,False],[4,False]] #index = (skill level, If it has been initialised)
        self.health = health
        self.gVelocity = 80
        self.gAngle = 0
        self.POI = (None,None)
        self.tankDistanceFromTank = 1000
        self.POIdistanceFromTank = 1000 #POI = Point of Impact
        self.aRight = False
        self.aLeft = False
        self.aUp = False
        self.aDown = False
        self.aFireShell = False
        self.finalX = 1000
        self.skillTwoAdaptation = 1
        self.ranOne = random.randint(10,35)
        self.ranTwo = random.randint(10,20)
        self.ranThree =  random.randint(7,12)
        self.gunSet = False
        self.behindS = None
        self.behindT = False             #used so that the ai knows if the opposition tank is in front of or behind its own tank. If its behind it is true
                                         #if not, then it is false indicating it is in front. saves using more than one variable


    # This function resets all movement boolean variables.

    def setAllFalse(self):
        self.aRight = False
        self.aLeft = False
        self.aUp = False
        self.aDown = False
        self.aFireShell = False

    # This function returns a boolean value representing if the opposition tank is behind or in front of the AI itself.

    def calcDirectionTank(self):
        distance = self.x - self.opp_x+20
        if distance < 0:
            self.behindT = False
        else:
            self.behindT = True
        return distance

    # This function returns a boolean value representing if the coordinate at which the AI's shell is behind or in front of the opposition tank.

    def calcDirectionShell(self):
        
        if self.POIdistanceFromTank < 0:
            self.behindS = True
            '''print("tank behind shell!, exactly " + str(self.POIdistanceFromTank) + " pixels from the tank")'''
        else:
            self.behindS = False
            '''print("tank in front of shell!, exactly " + str(self.POIdistanceFromTank) + " pixels from the tank")'''

    # This procedure calculates the distance between the point of impact of the AI's shell and the opposition tank.

    def calcPoiDist(self):
        distancePOI = self.POI[0] - self.opp_x+21
        self.POIdistanceFromTank = distancePOI

    # This procedure is used to allow all tank and user data to be passed through into the AI class from the main game function.

    def updateTankPositions(self,opp_x,opp_y,x,y,health,POI,angle,velocity):
        self.x = x
        self.y = y
        self.opp_x = opp_x+15
        self.opp_y = opp_y
        self.health = health
        self.POI = POI
        self.gAngle = angle
        self.gVelocity = velocity

    def setFinalX(self,finX):
        self.finalX = finX

    def setGunVel(self):
        return self.gVelocity

    # This function returns the AI's gun to the stock position, this being at a 45 degree angle facing towards the opposition tank.

    def goToBase(self):
        gInPos = False
        return gInPos

    # This procedure changes the mode of the Ai to start using more intelligent decision making.

    def changeMode(self):
        self.skillTwoAdaptation = 0

    # This function takes an angle as a parameter, and moves the tanks gun to said angle.

    def getToAngle(self,angle):
        if self.gAngle < angle:
            self.aDown = True
        else:
            self.aUp = True
            

####################### EXPERIMENTAL ################################   


    # This function is an experimental verison of my already finished AI algorithm. In this version the programme generates a ratio based on the
    # distance between the coordinate at which the shell will land and the AI's tank; and the distance between the same point and the opposition tank.
    # From here i can do certain comparisons e.g. >0.0 or <1.0. However it is not entirely finished and therefore will most likely keep this section of the
    # code inactive unless something is changed.

    def moveRate(self):
        gunOrTan = None
        if self.behindT == True:
            #self.getToAngle(-135)
            XfromSelf = abs(self.finalX-self.tankDistanceFromTank)
            XfromTank = abs(self.finalX+XfromSelf)
            distanceRatio = (XfromSelf,XfromTank)
            if distanceRatio[0] < distanceRatio[1]:
                distList = [0,0]
                distList[1] = (abs(distanceRatio[0])/abs(distanceRatio[1]))
                distList[0] = 1
            else:
                distList = [0,0]
                distList[0] = (abs(distanceRatio[1])/abs(distanceRatio[0]))
                distList[1] = 1
                
                
        if self.behindT == False:
            #self.getToAngle(-45)
            XfromSelf = abs(self.finalX-self.tankDistanceFromTank)
            XfromTank = abs(self.finalX+XfromSelf)
            distanceRatio = (XfromSelf,XfromTank)
            if distanceRatio[0] < distanceRatio[1]:
                distList = [0,0]
                distList[1] = (abs(distanceRatio[0])/abs(distanceRatio[1]))
                distList[0] = 1
            else:
                distList = [0,0]
                distList[0] = (abs(distanceRatio[1])/abs(distanceRatio[0]))
                distList[1] = 1
                
        #print(XfromSelf,XfromTank)
        
                
        distanceRatio =  tuple(distList)
        #print(distanceRatio," #  DActive: ",(self.aDown," UActive: ",self.aUp)," # Grad: ", (self.gAngle))
        return distanceRatio


                
    
    def generateMovementRate(self):

    
        distanceRatio = self.moveRate()
        if self.behindT == True:
            if self.behindS == False:
                if distanceRatio[0] > 0.5:
                    #self.aLeft = True
                    None
            else:
                if distanceRatio[1] < 0.5:
                    #self.aRight = True
                    None

            

        elif self.behindT == False:
            if self.behindS != True:
                if distanceRatio[1] > 0.5:
                    #self.aRight = True
                    None
            else:
                if distanceRatio[0] < 0.5:
                    #self.aLeft = True
                    None


        
        print(self.behindT, self.behindS, round(distanceRatio[0],8),":",round(distanceRatio[1],8))
        
    
####################### EXPERIMENTAL ################################            
        

    def brainOfAi(self):
        gInPos = False
        tInPos = False
        self.tankDistanceFromTank = self.calcDirectionTank()
        self.calcDirectionShell()
        self.calcPoiDist()
        self.gVelocity = 40
        
####### firing angle intelligence #########################
        if self.skillList[self.skillChoice][0] == 1:
            print("working")
            if self.skillList[self.skillChoice][1] == False: # skill level one linitialisation, sets gun angle to determined pos. And fires one this is done.
                if self.behindT == True:
                    if self.gAngle >= -135 and self.gAngle != -136:
                        self.aUp = True
                    else:
                        gInPos = True
                if self.behindT == False:
                    if self.gAngle >= -55 and self.gAngle != -46:
                        self.aUp = True
                    else:
                        gInPos = True
                        
                if gInPos == True:
                    self.aFireShell = True
                    self.skillList[self.skillChoice][1] = True
                    
        ## tank position intelligence ########################
                    
            else:
                if not self.behindS:
                    if self.finalX+self.ranOne > self.opp_x:
                        self.aLeft = True
                        print("moving")
                    else:
                        gInPos = True
                        
                elif self.behindS:
                    if self.finalX+self.ranOne < self.opp_x:
                        self.aRight = True
                        print("moving")
                    else:
                        gInPos = True

                if gInPos == True:
                    gInPos = False
                    self.skillChoice = 1
                    self.aFireShell = True

        ## level two of the tank intelligence, it begins to make decisions based on enviromental factors ############

        if self.skillList[self.skillChoice][0] == 2:
            if self.skillTwoAdaptation == 0:

                if not self.behindS:
                    if self.finalX+self.ranTwo> self.opp_x+20:
                        self.aLeft = True
                    else:
                        self.aLeft = False
                        tInPos = True
                        
                elif self.behindS:
                    if self.finalX+self.ranTwo < self.opp_x+20:
                        self.aRight = True
                    else:
                        self.aRight = False
                        tInPos = True

                if tInPos == True:
                    self.aFireShell = True
                    tInPos = False
                    self.skillTwoAdaption = 1


        
            if self.skillTwoAdaptation == 1:
                if self.behindS:
                    if self.finalX+self.ranTwo < self.opp_x+20:
                        if self.gAngle > -180 or self.gAngle < -90:
                            self.aUp = True
                        if self.gAngle > 90:
                            self.changeMode()
                    else:
                        self.aUp = False
                        tInPos = True
                        
                else:
                    if self.finalX+self.ranTwo > self.opp_x+20:
                        if self.gAngle > -180 or self.gAngle < 0:
                            self.aDown = True
                        if self.gAngle < -90:
                            self.changeMode()

                    else:
                        self.aUp = False
                        tInPos = True

                if tInPos == True:
                    self.aFireShell = True
                    tInPos = False
                    self.skillTwoAdaption = 0

                    
