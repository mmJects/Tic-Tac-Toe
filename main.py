# user/bin/env Python3
# Python Tic Tac Toe Game with turtle graphics
# Developed by Yun Yun

import turtle                   # import turtle module to get turtle graphic features
import time                     # import time module to wait for certain seconds
import for_turtle               # import for_turtle module file for tutle graphics
from two_players import Two_Players as Ply2     # import two_player module file to play two players        
import computer_easy            # import computer_easy module file to play with easy computer mode

turt = turtle.Turtle()
turt.hideturtle()
scre = turtle.Screen()

class YGame:
    def __init__(self):
        pass

    def game_intro(self):       # a function to display thel intro of the games
        # message variable that stores lines of information
        message = "Welcome to the Tic Tac Toe Game..\nAvailable Modes : \n\t(1) Player Vs Player \n\t(2) Player Vs Easy Ai \n\t(3) Player Vs Unbeatable Ai "
        turt.write(message,move=False, font=('arial',10,'bold'),align='center')     # display the message
        time.sleep(5)                                                               # wait 8 seconds for the message
        turt.clear()                                                                # clear the message and 
        mode = scre.textinput("Tic Tac Toe Game","Choose the modes : ")             # ask user for the modes
        if mode not in ["1","2","3"]:                                               # if input is invalid
            self.game_intro()                                                       # invoke intro method recursively
        else:                                                                       # if valid 
            return int(mode)                                                        # return the mode typecasting int

if __name__ == '__main__':
    game = YGame()
    
    mode = game.game_intro()
    ply = Ply2(600,600)                     # create an instance of two_players with height and width
    ply.create_sectors()                    # draw sectors on canvas
    ply.ask_ply_one_mark()                  # invoke ask mark for player one
    if mode == 1:                               # if user chose player Vs player mode
        # write an announcement with relating signs and players
        turt.write(f"Player 1 ({ply.ply_one_mark}) Vs Player 2 ({ply.ply_two_mark}) ", font=('Courier', 25, 'bold'),align='center')
        time.sleep(3)                           # wait 3 seconds for announcement
        turt.clear()                            # clear the announcement 
        for j in range(9):                      # loop through 9 times as there are 9 places on board
            ply.choose_location()               # invoke a method for choose location
        turtle.Screen().mainloop()              # call mainloop so that click points will be detected
    else:                                   # if user didn't choose two player mode
        if mode == 2:                       # if user chode easy mode
            # make an instance of computer easy mode (parameter:player mark)
            ai_ez = computer_easy.Computer(600,600,ply.ply_one_mark)    
            # write an announcement with relating signs and player and computer
            turt.write(f" Player ({ply.ply_one_mark}) Vs Easy AI ({ply.ply_two_mark}) ", font=('Courier', 25, 'bold'),align='center')
        elif mode == 3:                     # if user chose the unbeatable mode
            # make an instance of computer easy mode (parameter:player mark , False boolean to easy mode)
            ai_ez = computer_easy.Computer(600,600,ply.ply_one_mark,False)  
            turt.write(f" Player ({ply.ply_one_mark}) Vs Unbeatable AI ({ply.ply_two_mark}) ", font=('Courier', 20, 'bold'),align='center')                 
        time.sleep(3)                           # wait 3 seconds for announcement
        turt.clear()                            # clear the announcement
        for j in range(5):                      # loop through 5 times coz player have to choose at most 5 times
            ai_ez.choose_location()             # invoke a method to choose location
        turtle.Screen().mainloop()              # call mainloop so that click points will be detected

    
         