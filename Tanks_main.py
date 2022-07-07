import pygame
import random
import os
import math
import sys
from pygame.locals import *
from changeList import changexny
from proj_motion import *
from tank import *
from pixle import *
from pixleExplode import *
from slider import *
from surfaceGrad import surface_normal_avg
from listString import ListToString
from ai import *
from shell import *
import random
from math import *
import time
from stack import Stack
from avg import averageList
from leaderboards import *

successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
man = (1000,1000)
screen = pygame.display.set_mode((850, 720))

#initialising Tank Class


class game_initiate():

    def __init__(self):
        self.map_1_icon = pygame.image.load("bin/recources/MAP2_icon.png")
        self.map_2_icon = pygame.image.load("bin/recources/MAP3_icon.png")
        self.level_list = [self.map_1_icon,self.map_2_icon]
        self.current_level = 0
        self.game_mode = 0
        self.right_arrow_up = pygame.image.load("bin/buttons/right_up.png").convert_alpha()
        self.right_arrow_p = pygame.image.load("bin/buttons/right_p.png").convert_alpha()
        self.left_arrow_up = pygame.image.load("bin/buttons/left_up.png").convert_alpha()
        self.left_arrow_p = pygame.image.load("bin/buttons/left_p.png").convert_alpha()
        self.select_box = pygame.image.load("bin/recources/select_box.png")
        self.name_1 = ""
        self.name_2 = ""
        self.factor = 0
        self.init_ptwo = False
        self.pos_adjust = 0
        self.factorcomp = False
        self.backround = pygame.image.load("bin/imenu/background.png").convert_alpha()
        self.select_up = pygame.image.load("bin/buttons/select_map.png").convert_alpha()
        self.select_p = pygame.image.load("bin/buttons/select_map_pressed.png").convert_alpha()
        self.select_T_up = pygame.image.load("bin/buttons/select-tank.png").convert_alpha()
        self.ai_p = pygame.image.load("bin/buttons/ai_p.png").convert_alpha()
        self.ai_up = pygame.image.load("bin/buttons/ai_up.png").convert_alpha()
        self.ai = False
        self.select_T_p = pygame.image.load("bin/buttons/select-tank-pressed.png").convert_alpha()
        self.second_back = pygame.image.load("bin/imenu/bacc2.png").convert_alpha()
        self.stack = Stack()
        self.listofletters = []

    #The function initiate_menu simply lays the building blocks of the level selection such as the backround, buttons and map icons.

    def initiate_menu(self):
        screen.blit(self.backround, (0,0))
        pos = (850/2)-141
        screen.blit(self.select_box, (pos-34,44))
        screen.blit(self.level_list[self.current_level], (pos,80))
        start = self.change_map(pos)
        return start

    #This function handles input from the user via mouse click to determine the map the user would like to play

    def change_map(self,pos):
        a_dist = 11
        leftx = ((850/2)-141-34)+158
        lefty = 80+250
        rightx = (pos-34)+178
        righty = 80+250
        start = True
        pos = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        if pos[0] > leftx and pos[0] < leftx+a_dist and pos[1] > lefty and pos[1] < lefty+22 and press[0] == True:
            time.sleep(0.12)
            screen.blit(self.left_arrow_p,(leftx,lefty))
            if self.current_level == 0:
                self.current_level = 1
            else:
                self.current_level = 0

        else:
            screen.blit(self.left_arrow_up,(leftx,lefty))


        if pos[0] > rightx and pos[0] < rightx+a_dist and pos[1] > righty and pos[1] < righty+22 and press[0] == True:
            time.sleep(0.12)
            screen.blit(self.right_arrow_p,(rightx, righty))
            if self.current_level == 0:
                self.current_level = 1
            else:
                self.current_level = 0

        else:
            screen.blit(self.right_arrow_up,(rightx, righty))


        n = (173,42)
        buttonx = (leftx+17)-(173/2)
        buttony = 390
        if pos[0] > buttonx and pos[0] < buttonx+173 and pos[1] > buttony and pos[1] < buttony+46 and press[0] == True:
            screen.blit(self.select_p,(buttonx,buttony))
            start = False
            time.sleep(0.2)
        else:
            screen.blit(self.select_up,(buttonx,buttony-4))


        return start


    #The function chooseGame has one main goal, to allow the user to select their name and if they would like to play against an computer or another
    #person. However to do this it is compromised of multiple functions handling user inputs for name, Dynamic name rendering and game selection.

    def chooseGame(self):
        screen.fill(WHITE)
        screen.blit(self.second_back, (0,0))
        start = True
        pos1 = (850/2)-141
        a_dist = 11
        leftx = ((850/2)-141-34)+158
        lefty = 80+250
        rightx = (pos1-34)+178
        righty = 80+250
        pos = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        n = (173,42)
        buttonx = ((leftx+17)-(173/2))-228
        buttony = 390
        screen.blit(self.select_box, (pos1-250,44))
        screen.blit(self.select_box, (pos1+183,44))
        if self.init_ptwo == False:
            screen.blit(self.select_T_up,(buttonx+(250+190),buttony-4))
            screen.blit(self.ai_up,((pos1+400,75)))
            if pos[0] > buttonx and pos[0] < buttonx+173 and pos[1] > buttony and pos[1] < buttony+46 and press[0] == True:
                screen.blit(self.select_T_p,(buttonx,buttony))
                self.init_ptwo = True
                self.name_1 = ListToString(self.stack.items)
                self.listOfLetters = []
                self.stack.items = []
                self.pos_adjust = 0
                self.factorcomp = False
                time.sleep(0.2)
            else:
                screen.blit(self.select_T_up,(buttonx,buttony-4))


            self.set_name(122-14)
            self.display_letter(122-14)

        else:
            screen.blit(self.select_T_up,(buttonx,buttony-4))
            pygame.draw.rect(screen,BLACK,(buttonx-42,buttony+55,35*8+(8*2)-20,40))
            pygame.draw.rect(screen,WHITE,(buttonx-42,buttony+55,35*8+(8*2)-20,40),2)
            if pos[0] > buttonx+(250+190) and pos[0] < buttonx+173+(250+190) and pos[1] > buttony and pos[1] < buttony+46 and press[0] == True:
                screen.blit(self.select_T_p,(buttonx+(250+190),buttony))
                self.name_2 = ListToString(self.stack.items)
                start = False
                time.sleep(0.2)
            else:
                screen.blit(self.select_T_up,(buttonx+(250+190),buttony-4))


            if self.ai == False:
                screen.blit(self.ai_up,((pos1+400,75)))
            else:
                screen.blit(self.ai_p,((pos1+400,75+4)))

            if pos[0] > pos1+400 and pos[0] < pos1+(400+69) and pos[1] > 75 and pos[1] < 75+44 and press[0] == True:
                if self.ai == True:
                    self.ai = False
                else:
                    self.ai = True
                time.sleep(0.1)

            self.set_name((122-14)-216)
            self.display_letter((122-14)-216)

        return start


    #This function handles the users input via up and down arrows and assigns the correct ordinal value of all 26 characters in the alphabet, to turn this
    #into ascii a simple addition of 65 is needed to correctly generate the desired letter, looping from A to Z and back to A.

    def change_letter(self):
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.factor = (self.factor + 1)%25
            time.sleep(0.07)
        elif keys[K_DOWN]:
            self.factor = (self.factor - 1)%25
            time.sleep(0.07)

    #This function handles the rendering of the letters in the correct positions, this is neccessary due to the nature of the retro-style text
    #input, the user selects a letter with the up and down arrows and presses enter to confirm.

    def display_letter(self,factor):
        keys = pygame.key.get_pressed()
        myfont = pygame.font.SysFont("monospace", 25)
        init_pos =  0
        leftx = (((850/2)-141-34)+158)-factor
        buttonx = ((leftx+17)-(19*8+(8*2)/2))-factor
        buttony = 390+30
        pos = (buttonx+26+(35*self.pos_adjust),buttony+30)
        self.change_letter()
        no_ = chr(65+self.factor)
        letter = myfont.render(str(no_), 24, (255,255,255))
        if not self.factor > 25:
            screen.blit(letter,pos)
        else:
            letter = myfont.render("A", 24, (255,255,255))
            screen.blit(letter,pos)


        if self.pos_adjust <= 6:
            if keys[K_RETURN]:
                self.stack.push(no_)
                try:

                    letter = myfont.render(self.stack.items[self.pos_adjust], 24, (255,255,255))
                    newpos = (buttonx+26+(35*self.pos_adjust),buttony+30)
                    self.listofletters.append([letter,pos])
                    self.pos_adjust += 1
                except:
                    None
                time.sleep(0.2)

        if keys[K_BACKSPACE]:
            try:
                self.stack.pop()
                self.listofletters.pop()
                self.pos_adjust -= 1
            except:
                print("Stack and or List is already empty!")
            #time.sleep(0.007)

        self.display_pos_letters(factor)


    #This handles the actual rendering of the letters.


    def display_pos_letters(self,factor):
        myfont = pygame.font.SysFont("monospace", 25)
        leftx = (((850/2)-141-34)+158)-factor
        buttonx = ((leftx+17)-(19*8+(8*2)/2))-factor
        buttony = 390+30
        pos = (buttonx+26+(35*0),buttony+30)
        for n in range(len(self.listofletters)):
            screen.blit(self.listofletters[n][0],self.listofletters[n][1])

    #This function sets up the basis of the visual text box.

    def set_name(self,factor):
        leftx = (((850/2)-141-34)+158)-factor
        buttonx = ((leftx+17)-(19*8+(8*2)/2))-factor
        buttony = 390+30
        letter_no = 8
        box_rect = (19*8+(8*2),40)
        pygame.draw.rect(screen,BLACK,(buttonx+19,buttony+25,35*8+(8*2)-20,40))
        pygame.draw.rect(screen,WHITE,(buttonx+19,buttony+25,35*8+(8*2)-20,40),2)

#This class is one of the most important, it has many uses and mainly handles base game requirements such as the options bar, health bar, velocity adjustment,
#

class game():

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.image = pygame.Surface((32, 32))
        self.Map1_Boundry_list = [(1,541),(93,528),(187,525),(287,528),(431,546),(561,568),(591,574),(677,609),(724,631),(746,642),(766,648),(783,646),(799,629),(805,607),(804,582),(837,541),(870,523),(890,510),(937,495),(979,479),(1000,477)]
        self.Map1 = pygame.image.load("bin/recources/MAP2.png").convert_alpha()
        self.Map2 = pygame.image.load("bin/recources/MAP3.png").convert_alpha()
        self.topbar = pygame.image.load("bin/main/Round Box.png").convert_alpha()
        self.tank1bar = pygame.image.load("bin/main/bar t1.png").convert_alpha()
        self.tank2bar = pygame.image.load("bin/main/bar t2.png").convert_alpha()
        self.bar1 = pygame.image.load("bin/main/Vbar.png").convert_alpha()
        self.bar2 = pygame.image.load("bin/main/Vbar.png").convert_alpha()
        self.g1 = pygame.image.load("bin/main/g1.png").convert_alpha()
        self.g2 = pygame.image.load("bin/main/g2.png").convert_alpha()
        self.g3 = pygame.image.load("bin/main/g3.png").convert_alpha()
        self.g4 = pygame.image.load("bin/main/g4.png").convert_alpha()
        self.winBack = pygame.image.load("bin/win/win_back.png")
        self.p1Win = pygame.image.load("bin/win/player1.png").convert_alpha()
        self.p2Win = pygame.image.load("bin/win/player2.png").convert_alpha()
        self.b_tank = Tank()
        self.a_tank = Tank()
        self.level_list = [self.Map1,self.Map2]
        self.currentLevel = 0
        self.currentMap = self.level_list[self.currentLevel]
        self.SLID1 = Slider()
        self.SLID2 = Slider()
        self.turn = 0
        self.pressed_inside = False
        self.pressed_inside_2 = False
        self.shell = Shell()
        self.current = 24
        self.current_2 = self.b_tank.Tank_x
        self.current_x = self.a_tank.Tank_x
        self.name1 = ""
        self.name2 = ""
        self.win = 2
        self.startTime = 0.0
        self.endTime = 0.0
        self.entryAdded = False

    # returns an integer that is rounded

    def rndint(self,number):
        return int(round(number))

    # This procedure sets the velocity of the current players tank to whatever
    # it should be subtracted by the ammount the user has lowered the slider
    # controlling velocity.

    def update_velocity_1(self,factor):
        factor = int(factor)
        n = 95-factor

        self.a_tank.v = n


    def update_velocity_2(self,factor):
        factor = int(factor)
        n = 95-factor

        self.b_tank.v = n

    # this function returns the unsigned difference between two intgers

    def calc_dfrom_p(self,x1,x2):
        dist = x1-x2
        dist = abs(dist)
        return dist

    # This function returns a damage variable dependant on the distance between
    # the shell impact and the closest edge of the opposition tank

    def determine_shell_damage(self,distance):
        if distance <= 10:
            damage = 45
        elif distance <= 15:
            damage = 40
        elif distance <= 20:
            damage = 35
        elif distance <= 25:
            damage = 30
        elif distance <= 30:
            damage = 20
        elif distance <= 40:
            damage = 10
        else:
            damage = 0
        return damage


    # this function handles collisions between the shells and the tanks.

    def determine_shell_tank_col(self,x1,y1,determined,turn):
        hit_pos = (x1,y1)
        collision_wt = False
        distance = 100
        if turn == 1:
            tank_pos = (self.a_tank.Tank_x,self.a_tank.Tank_y)
        else:
            tank_pos = (self.b_tank.Tank_x,self.b_tank.Tank_y)
        damage = 0
        if hit_pos[1] < tank_pos[1]+(17+15) and hit_pos[1] > tank_pos[1]-15 and hit_pos[0] < tank_pos[0]+(42+15) and hit_pos[0] > tank_pos[0]-15 and determined == False:
            collision_wt = True
            determined = True

        if collision_wt:
            distance = self.calc_dfrom_p(hit_pos[0],tank_pos[0])
            damage = self.determine_shell_damage(distance)


        return damage,determined


    # this function removes the determined health based on previous functions
    # from both tanks.


    def remove_health(self,turn,determined,x1,y1):
        damage,determined = self.determine_shell_tank_col(x1,y1,determined,turn)
        if turn == 1:
            self.a_tank.tank_health -= damage
        else:
            self.b_tank.tank_health -= damage
        return determined


    # this function does multiple things to ensure the tank is spawned correctly
    # for example it sets the centre of rotation for the tank and gun bitmap.

    def spawn_tank(self):
        rect = self.a_tank.Tank_main.get_rect(center=(self.a_tank.Tank_x+21,self.a_tank.Tank_y+9)) #Set the centre of rotation
        screen.blit(pygame.transform.rotozoom(self.a_tank.Tank_main,self.a_tank.t_angle,1.0),rect)
        height = self.a_tank.Tank_gun.get_height()/2.0
        width = self.a_tank.Tank_gun.get_width()/2
        rect = self.a_tank.gun_blit(pygame.transform.rotozoom(self.a_tank.Tank_gun,self.a_tank.angle,1.0),self.a_tank.Tank_y-width,self.a_tank.Tank_y+height)
        self.fix_height_skew()
        return rect

    def spawn_tank2(self):
        rect = self.b_tank.Tank_main.get_rect(center=(self.b_tank.Tank_x+21,self.b_tank.Tank_y+9)) #Set the centre of rotation
        screen.blit(pygame.transform.rotozoom(self.b_tank.Tank_main,self.b_tank.t_angle,1.0),rect)
        height = self.b_tank.Tank_gun.get_height()/2.0
        width = self.b_tank.Tank_gun.get_width()/2
        rect = self.b_tank.gun_blit(pygame.transform.rotozoom(self.b_tank.Tank_gun,self.b_tank.angle,1.0),self.b_tank.Tank_y-width,self.b_tank.Tank_y+height)
        return rect

    # This procedure is used to ensure the x coordinate is not offset by the
    # adjustment of the angle of the tank itself

    def fix_height_skew(self):
        if self.a_tank.t_angle < 11:
            self.a_tank.tank_height = 18
        else:
            self.a_tank.tank_height = 26

        if self.b_tank.t_angle < 11:
            self.b_tank.tank_height = 18
        else:
            self.b_tank.tank_height = 26



    # This procedure sets the y-coordinate of each tank to the y-coordinate of the
    # current corresponding height from the terrain plus the height of the tank

    def floor_collision(self,ny,x,dist_list,x2,ny2):
        self.a_tank.Tank_y = ny+(dist_list[int(x)][0]-self.a_tank.tank_height)
        self.b_tank.Tank_y = ny2+(dist_list[int(x2)][0]-self.a_tank.tank_height)

    # This procedure subtracts the ammount of health lost from the size of the health bar in the main game screen.

    def health_adjust(self):
        size = 116
        rect1loc = (24+self.a_tank.tank_health,24,size-self.a_tank.tank_health,20)
        rect2loc = (450+self.b_tank.tank_health,24,size-self.b_tank.tank_health,20)
        pygame.draw.rect(screen, WHITE, rect1loc, 0)
        pygame.draw.rect(screen, WHITE, rect2loc, 0)


    # This function returns a boolean variable depending on who won the match.

    def determineWin(self,game_over):
        if self.a_tank.tank_health <= 0:
            self.win = 1
            print("player2 win!")
            game_over = True

        if self.b_tank.tank_health <= 0:
            self.win = 0
            print("player1 win!")
            game_over = True

        return game_over

    # This function renders the splash screen telling the users who won the game.

    def renderWinScreen(self):
        print("in render")
        screen.fill(WHITE)
        screen.blit(self.winBack,(0,0))
        if self.win == 0:
            screen.blit(self.p1Win,((850/2)-727/2,(720/2)-104/2))
        if self.win == 1:
            screen.blit(self.p2Win,((850/2)-736/2,(720/2)-104/2))

    # This procedure calls the slider class' and gets sets the factor variables to the ammount the user has moved it from the original position.

    def draw_boxes_forV(self,turn):
        if turn == 0:
            self.SLID1.slide()
        else:
            self.SLID2.slide()
        complete = True
        factor = self.SLID1.return_pos()
        factor2 = self.SLID2.return_pos()
        self.update_velocity_1(factor)
        self.update_velocity_2(factor2)
        rect1 = self.SLID1.rect
        rect2 = self.SLID2.rect
        pygame.draw.rect(screen, (255,105,180), rect1, 0)
        pygame.draw.rect(screen, (255,105,180), rect2, 0)



    # This procedure handles the actual rendering of sliders

    def vel_bar_draw(self):
        n = 61+116
        screen.blit(self.bar1,(n,24))
        screen.blit(self.g1,(n-22,24))
        screen.blit(self.g2,(n+12,24))

        m = 48+116+424
        screen.blit(self.bar2, (m,24))
        screen.blit(self.g3, (m-22,24))
        screen.blit(self.g4, (m+12,24))

    # This procedure renders the entire main game screen options bar.

    def bar_draw(self):
        topl = (850-823)/2
        screen.blit(self.topbar, (topl,topl))
        screen.blit(self.tank1bar, (topl+13,topl+13))
        screen.blit(self.tank2bar, (topl+424,topl+13))

    # This function handles all main menu rendering and actions eg clickiing and button changing.

    def draw_menu(self,m):
        options_b = pygame.image.load("bin/menu/options_button.png").convert_alpha()
        start_b = pygame.image.load("bin/menu/start_button.png").convert_alpha()
        howto_b = pygame.image.load("bin/menu/howto_button.png").convert_alpha()
        options_p = pygame.image.load("bin/menu/options_pressed.png").convert_alpha()
        start_p = pygame.image.load("bin/menu/start_pressed.png").convert_alpha()
        howto_p = pygame.image.load("bin/menu/howto_pressed.png").convert_alpha()
        menu = pygame.image.load("bin/menu/menu_main.png").convert_alpha()
        bw,bh = 197,55
        sx=((850/2)-(bw/2))
        hx=((850/2)-(bw/2))
        ox=((850/2)-(bw/2))
        sy = 230
        hy = 330
        oy = 430
        pygame.transform.scale(options_p, (bw, bh))
        pygame.transform.scale(howto_p, (bw, bh))
        pygame.transform.scale(start_p, (bw, bh))
        screen.fill(WHITE)
        screen.blit(menu,(0,0))
        press = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        if pos[0] >sx and pos[0] < sx+bw and pos[1] > sy and pos[1] < sy+bh and press[0] == True:
            screen.blit(start_p,(sx,sy))
            screen.blit(howto_b,(hx,hy))
            screen.blit(options_b,(ox,oy))
            pygame.display.flip()
            time.sleep(0.2)
            m = False
        else:
            screen.blit(start_b,(sx,sy))
        if pos[0] >hx and pos[0] < hx+bw and pos[1] > hy and pos[1] < hy+bh and press[0] == True:
            screen.blit(howto_p,(hx,hy))
        else:
            screen.blit(howto_b,(hx,hy))

        if pos[0] >ox and pos[0] < ox+bw and pos[1] > oy and pos[1] < oy+bh and press[0] == True:
            screen.blit(options_p,(ox,oy))
        else:
            screen.blit(options_b,(ox,oy))
        return m

    # This function handles the rendering of the imaginary shell which is used for calculations and collision detections.

    def draw_objects(self,count,crater_list,fired,proj_list,dist_list,fired2,proj_list2,count2):
        count_goal = len(proj_list)
        count_goal2 = len(proj_list2)
        if fired != False:
            count,fired,tup = self.shell.fireShell_i(proj_list,count,count_goal,fired)
        else:
            tup = (1000,1000)

        if fired2 != False:
            count2,fired2,tup = self.shell.fireShell_i(proj_list2,count2,count_goal2,fired2)
        else:
            tup2 = (1000,1000)

        return count,fired,tup,crater_list,count_goal,fired2,proj_list2,count2,count_goal2

    # This function makes the game turn based.

    def check_fired_active(self,fired):
        if fired == True:
            fired = False
            self.turn += 1
        return fired

    # This function returns the final x coordinate that the trajectory of the shell will follow.

    def getFinalX(self):
        finalX = giveFinalX(self.b_tank.v, self.b_tank.shell_angle+540, hs=3, g=9.8)
        finalX = (finalX+self.b_tank.Tank_x+(self.a_tank.tank_width/2)+5)
        #pygame.draw.line(screen,(255,0,0),(finalX,600),(finalX,200))
        return finalX

    # This function handles the ordering of procedure calling dependant of where in the explosion-cycle the explosion itself.

    def applyExplosion(self,pix_collision,man,temp_col,exp_init,turn,oppPOI,pix_list,exp_complete,determined,exp_count,exp_count_goal):
        if pix_collision == True or temp_col == True:

             if exp_complete == False:
                 temp_col = pix_collision
                 if turn == 1:
                     oppPOI = man
                 pix_list,exp_complete = calc_rad_pix(man[0]+10,man[1],16,exp_complete)
                 pix_list = animate_pix(pix_list)
                 self.remove_health(turn,determined,man[0],man[1])
                 if pix_collision == True:
                     if turn == 0:
                         turn = 1
                     else:
                         turn = 0

             if exp_count <= exp_count_goal:
                 pix_list = construct_exp(pix_list,int(exp_count))
                 exp_count += 14
             else:
                 exp_count = 0
                 exp_complete = False
                 temp_col = False

        return temp_col,oppPOI,pix_list,exp_complete,turn,exp_count,exp_init,exp_complete

    # This procedure sets the tanks angle variables to the calculated gradient for the current coordinates.

    def adjustTankAngle(self):
        grad_from_func = surface_normal_avg(int(self.a_tank.Tank_x),400)
        grad_from_func -= grad_from_func*2
        self.a_tank.t_angle = grad_from_func
        grad_from_func = surface_normal_avg(int(self.b_tank.Tank_x),400)
        grad_from_func -= grad_from_func*2
        self.b_tank.t_angle = grad_from_func


    # This procedure draws the main game bar.

    def drawMain(self,turn):
        self.bar_draw()
        self.health_adjust()
        self.vel_bar_draw()
        self.draw_boxes_forV(turn)

    # This function alternates which tanks controlls are controllable by the current user/AI.

    def alternateTanks(self,fired,fired2,switch_a):
        if fired == True or fired2 == True:
            switch_a = False

        return switch_a

    # This function handles the rendering of the non-imaginary shell which is used as the actual shell image.

    def applyShellAnimation(self,turn,fired,count,tup,proj_list,count_goal,fired2,count2,tup2,proj_list2,count_goal2,fired_add2):

        if turn == 0:
            if fired != False:
                count,fired,tup = self.shell.fireShell(proj_list,count,count_goal,fired)
            else:
                tup = (1000,1000)
        elif turn == 1:

            if fired2 != False:

                count2,fired2,tup2 = self.shell.fireShell(proj_list2,count2,count_goal2,fired2)

                fired_add2 = False
            else:
                tup2 = (1000,1000)


        return tup,count,fired,tup2,count2,fired2,fired_add2


    # In this instance i itterate through, starting from x = 0 and y = 400, increasing y by one each time until it reaches the terrain.


    def xyGen(self):
        xylist = []
        current = (255,255,255)
        print("reading map 2")
        for i in range(0,850):
            y = 400
            current = screen.get_at((i,y))
            while current == (255,255,255):
                current = screen.get_at((i,y))
                if current != (255,255,255,255):
                    xylist.append(y)
                y += 1

        return xylist


    # This is the main game function, this handles many things including user controlls and variable declarations; also containing the
    # main game loop


    def main(self):
        c_x,c_x2 = self.current_x,self.current_2
        self.SLID2.x += 411
        self.image .fill(WHITE)
        ny,ny2 = self.a_tank.Tank_y,self.b_tank.Tank_y
        tank_group,tank_group2 = self.spawn_tank(),self.spawn_tank2()
        in_menu,in_game_choice = True,True
        rect,counter,current = 0,0,24
        proj_list,proj_list2,crater_list,pix_list = [],[],[],[]
        checked,checked2 = False,False
        vel_bar_init = False
        x_checked,x_checked2 = False,False
        fired,fired2 = False,False
        anim_start2 = False
        switch_a,completed_gen = True,False
        count,count2 = 0,0
        turn,current = 0,0
        tup,tup2 = (1000,1000),(1000,1000)
        intermediate_menu = game_initiate()
        clist,clist2,circlelist = [None],[None],[]
        fired_active,fired_add,fired_add2 = False,False,False
        in_start,game_over = True,False
        exp_count,exp_count_goal,exp_init = 0,720,True
        calculated,determined,complete = False,False,False
        shell_collided,shell_collided2 = True,True
        temp_col,anim_start = False,False
        gen_complete,exp_complete = False,False
        oppPOI = (1000,1000)
        man = (300,200)
        old_turn = turn
        checkstrt = False
        checkend = False
        board = False
        in_end = True
        ai = artificialIntelligence(self.a_tank.Tank_x,self.a_tank.Tank_y,self.b_tank.Tank_x,self.b_tank.Tank_y,self.b_tank.tank_health)
        while True:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            if in_menu == True:

                in_menu = self.draw_menu(in_menu)
            else:

                if in_start == True:

                    in_start = intermediate_menu.initiate_menu()

                else:

                    if in_game_choice == True:

                        in_game_choice = intermediate_menu.chooseGame()
                    else:

                        if game_over != True:


                            self.currentLevel = intermediate_menu.current_level
                            self.currentMap = self.level_list[self.currentLevel]
                            self.determineWin(game_over)
                            game_over = self.determineWin(game_over)
                            current_x = self.a_tank.Tank_x
                            self.name1 = intermediate_menu.name_1
                            self.name2 = intermediate_menu.name_2
                            temp_angle = int(self.b_tank.shell_angle)
                            ai.updateTankPositions(self.a_tank.Tank_x,self.a_tank.Tank_y,self.b_tank.Tank_x,self.b_tank.Tank_y,self.b_tank.tank_health,oppPOI,temp_angle,self.b_tank.v)
                            keys = pygame.key.get_pressed()

                            if turn == 1:

                                if intermediate_menu.ai == True:
                                    ai.brainOfAi()

                                self.b_tank.v = ai.setGunVel()
                                ai.setFinalX(self.getFinalX())

                            else:
                                ai.setAllFalse()

                            if keys[pygame.K_LEFT] or ai.aLeft == True:
                                if switch_a:
                                    if turn == 0:
                                        x_checked = self.a_tank.move(0,x_checked)
                                    else:
                                        x_checked2 = self.b_tank.move(0,x_checked2)

                            if keys[pygame.K_RIGHT] or ai.aRight == True:
                                if switch_a:
                                    if turn == 0:
                                        x_checked = self.a_tank.move(1,x_checked)
                                    else:
                                        x_checked2 = self.b_tank.move(1,x_checked2)

                            if keys[K_UP] or ai.aUp == True:
                                if switch_a:
                                    if turn == 0:
                                        self.a_tank.u = 0
                                        self.a_tank.angle = self.a_tank.gun_angle()
                                        self.a_tank.shell_angle = self.a_tank.gun_angle_2()
                                    else:
                                        self.b_tank.u = 0
                                        self.b_tank.angle = self.b_tank.gun_angle()
                                        self.b_tank.shell_angle = self.b_tank.gun_angle_2()

                            if keys[K_DOWN] or ai.aDown == True:
                                if switch_a:
                                    if turn == 0:
                                        self.a_tank.u = 1
                                        self.a_tank.angle = self.a_tank.gun_angle()
                                        self.a_tank.shell_angle = self.a_tank.gun_angle_2()
                                    else:
                                        self.b_tank.u = 1
                                        self.b_tank.angle = self.b_tank.gun_angle()
                                        self.b_tank.shell_angle = self.b_tank.gun_angle_2()

                            switch_a = True

                            if keys[K_SPACE] or ai.aFireShell == True:

                                if checkstrt == False:

                                    checkstrt = True

                                if fired != True or fired2 != True:

                                    determined = False
                                    if turn == 0:
                                        counter += 1
                                        proj_list = projectile_xy(self.a_tank.v, self.a_tank.shell_angle+540, hs=3, g=9.8)
                                        proj_list = changexny(proj_list,self.a_tank.Tank_x,self.a_tank.Tank_y)
                                        fired = True
                                        shell_collided = False
                                        anim_start = True
                                    elif turn == 1:
                                        counter += 1
                                        proj_list2 = projectile_xy(self.b_tank.v, self.b_tank.shell_angle+540, hs=3, g=9.8)
                                        proj_list2 = changexny(proj_list2,self.b_tank.Tank_x,self.b_tank.Tank_y)
                                        fired2 = True
                                        shell_collided2 = False
                                        anim_start2 = True

                            switch_a = self.alternateTanks(fired,fired2,switch_a)
                            screen.fill(WHITE)
                            screen.blit(self.currentMap,(0,0))


                            if checked == False:
                                xylist = self.xyGen()
                                dist_list,checked = pixl_chec(checked)
                                checked = True

                            #pix_collision = get_pix_collide(man[0],man[1])
                            pix_collision,pixpos = newPixCol(man,xylist)

                            #print(pix_collision)


                            self.drawMain(turn)
                            count,fired,man,crater_list,count_goal,fired2,proj_list2,count2,count_goal2 = self.draw_objects(count,crater_list,fired,proj_list,dist_list,fired2,proj_list2,count2)
                            tup,count,fired,tup2,count2,fired2,fired_add2 = self.applyShellAnimation(turn,fired,count,tup,proj_list,count_goal,fired2,count2,tup2,proj_list2,count_goal2,fired_add2)
                            self.adjustTankAngle()
                            temp_col,oppPOI,pix_list,exp_complete,turn,exp_count,exp_init,exp_complete = self.applyExplosion(pix_collision,pixpos,temp_col,exp_init,turn,oppPOI,pix_list,exp_complete,determined,exp_count,exp_count_goal)
                            rect = self.spawn_tank()
                            self.b_tank.Tank_y = ny2+(dist_list[int(self.b_tank.Tank_x+10)][0]-self.b_tank.tank_height)
                            rect2 = self.spawn_tank2()
                            self.a_tank.tank_health,turn = self.shell.vel_increase(self.a_tank.tank_health,turn)

                            if x_checked == False:
                                self.floor_collision(ny,self.a_tank.Tank_x,dist_list,self.b_tank.Tank_x+10,ny2)
                                x_checked = True

                            self.a_tank.calcAccuracy(man,self.b_tank.Tank_x)
                            self.b_tank.calcAccuracy(man,self.a_tank.Tank_x)
                            avg1 = averageList(self.a_tank.accuracyList)
                            avg2 = averageList(self.b_tank.accuracyList)

                        elif game_over == True and in_end == True:

                            if checkend == False:

                                checkend == True

                            #print((self.endTime-self.startTime))
                            #print(avg1)
                            #print(avg2)

                            if self.win == 0:
                                winName = self.name1
                                winScore = (avg1*((self.endTime-self.startTime)*100))
                            else:
                                winName = self.name2
                                winScore = (avg2*((self.endTime-self.startTime)*100))

                            #print(winScore)


                            screen.fill(WHITE)
                            self.renderWinScreen()

                            board = True
                            in_end = False


            if board == True:
                screen.fill(WHITE)

                if self.entryAdded == False:
                    leaderSet = leaderboardSetup()
                    leaderSet.csv.loadWrite()
                    leaderSet.csv.entry([winName,int(winScore)])
                    leaderSet.csv.closeWrite()
                    self.entryAdded = True

                leaderSet.loadLeader()





            pygame.display.flip()
##            if game_over == True:
##                time.sleep(0)


        return winName,winScore






G = game()
name,score = G.main()

print(name,score)
