# Easy computer mode is created with random choices which means doesn't move optimally

import turtle
import random                                       # import random module to get random numbers
import time
from two_players import Two_Players 
from hard_ai import Unbeatable

tur = turtle.Turtle()               # create an instacne of turtle to write on canvas
tur.hideturtle()                    # hide turtle so that there will be only notices
tur.color("deep sky blue")          # set the color of a turtle 

class Computer(Two_Players):        # create an instance of Computer class for computer modes (inherting two players)
    def __init__(self, h: int, w: int,mark:str,easy=True):     # mark for player sign , easy for checking two modes
        super().__init__(h, w)                                 # inherting two attributes from two players class
        self.player_mark = mark                                # make player's mark class attribute 
        self.ai_mark = "X" if self.player_mark == "O" else "O" # decide for ai_mark according to player_mark
        self.mark_sign = {self.player_mark:"Human",self.ai_mark:"Computer"} # mark sign for declaration
        self.easy = easy                                       # boolean type to check easy mode or not
        if not self.easy:                                      # if not easy mode
            self.ai_mode = Unbeatable(self.player_mark,self.ai_mark)    # make an instance of hard ai mode

    def draw_random(self, mark:str):                # draw random class for easy_ai mode
        while True:                                 # while looping to get valid position
            x = random.randint(1,9)                 # make a random choice from 1 to 9
            if self.lst[x-1] != " ":                # if the random number's location is occupied
                continue                            # restart the loop
            self.lst[x-1] = mark                    # if valid , assign mark into the list
            self.draw_markings(self.ai_mark,x)      # draw mark in canvas
            break                                   # break the while loop

    def fxn(self, x, y):                                # override the method of two players 
        for i in range(1,10):                           # loop through 9 times as there are 9 sections on board
            x1,y1,x2,y2,x3,y3,x4,y4 = self.POINTS[i-1]  # get the 4 coordinates points of each section
            # check user's click location and 4 coordination # whether user's coordinates is in a specific section
            if self.check(x1,y1,x2,y2,x3,y3,x4,y4,x,y): # if user's click point is a valid in one section
                if self.lst[i-1] == " ":                # if user's click point is valid and not occupied
                    try:                                # try
                        del self.click[0]               # delete click point turtle so that one click will be affected
                    except:                             # if there is an error
                        return 0                        # return and do nothing
                    self.draw_markings(self.player_mark,i)   # draw marks on canvas  with user's mark and clicl location
                    self.lst[i-1] = self.player_mark         # assign user's mark into class list
                    if self.check_winner(self.player_mark):           # check winner with class list  # if some one wins , lose or tie
                        turtle.Screen().onclick(None)   # set onclick None so that we can't click anymore
                    else:                               # if player didn't win
                        if self.easy:                           # if it is easy mode
                            self.draw_random(self.ai_mark)      # draw mark randomly
                        else:                                           # if it is computer serious mode
                            self.ai_mode.set_lst_to_test(self.lst)      # put the main list into algorithm to test
                            pos = self.ai_mode.ai_hd()                  # get the best move for ai
                            self.lst[pos] = self.ai_mark                # assign the mark into the original list
                            self.draw_markings(self.ai_mark,pos+1)      # draw mark onto canvas
                        if self.check_winner(self.ai_mark):           # check winner with class list  # if some one wins , lose or tie
                            turtle.Screen().onclick(None)   # set onclick None so that we can't click anymore
                elif self.lst[i-1] != " ":              # if user's choice is occupied
                    # warn user if player's choice is occupied 
                    tur.write("Your input is occupied..", font=('Courier', 25, 'bold'),align='center') # warn user
                    time.sleep(0.5)                     # wait half seconds and 
                    tur.clear()                         # clear the warning

    def choose_location(self):              # choose location method for user to make a click
        src = turtle.Screen()               # create an instance of screen 
        self.click.append(src)              # append that instance into click list
        self.click[0].onclick(self.fxn)     # make onclick function and invoke a method 