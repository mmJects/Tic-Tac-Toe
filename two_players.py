import turtle                       # import turtle module to create turtle objects
import time                         # import time module to wait seconds
import for_turtle as ttt            # import another module that is created 
from for_turtle import board as B   # also import a board class from for_turtle module

tur = turtle.Turtle()               # create an instacne of turtle to write on canvas
tur.hideturtle()                    # hide turtle so that there will be only notices
tur.color("deep sky blue")          # set the color of a turtle 

class Two_Players(B):               # create a Two players class that inherited from 

    count = 0                       # count variable to track two player's sings 
    click = []                      # click list to store user's click point turtle 

    def __init__(self, h: int, w: int):                     # initialize a class with parent's attributes
        super().__init__(h, w)                              # inherit all parent's attributes        
        self.lst = [" "," "," "," "," "," "," "," "," "]    # create a class list to store player's choices signs

    # function to ask user location with input field
    def ask_user_location(self,ply:int,mark:str):                 
        chocies_lst = ["1","2","3","4","5","6","7","8","9"]     # to check user's inputs
        while True :                                            # always loop until break
            # turtle input field to ask location for user
            choice = ttt.screen.textinput(f"Your mark {mark}",f"Player {ply} enter the location on board(1-9)=>")
            if choice in chocies_lst:                           # if user only choose 1 to 9
                choice = int(choice)            # type cast it into integer                    
                if self.lst[choice-1] == ' ':   # if user's input is valid     # subtract one from user choice
                    self.lst[choice-1] = mark   # assign mark in user's choice # beacuse board range is 0 to 8
                elif self.lst[choice-1] != ' ': # if user's mark is not empty
                    # warn user if player's choice is occupied
                    tur.write("Your input is occupied..", font=('Courier', 25, 'bold'),align='center')
                    time.sleep(2)               # wait 2 seconds for the warning
                    tur.clear()                 # clear the warning
                    continue                    # restart the loop since user's input is invalid
                break           # break the always looping if  the choice is correct
        return choice           # return user's valid choice loaction on board 

    def fxn(self, x, y):                                # a function to call if user click on screen
        for i in range(1,10):                           # loop through 9 times as there are 9 sections on board
            x1,y1,x2,y2,x3,y3,x4,y4 = self.POINTS[i-1]  # get the 4 coordinates points of each section
            # check user's click location and 4 coordination # whether user's coordinates is in a specific section
            if self.check(x1,y1,x2,y2,x3,y3,x4,y4,x,y): # if user's click point is a valid in one section
                mk = self.ply_one_mark if self.count % 2 == 0 else self.ply_two_mark    # track user's mark
                if self.lst[i-1] == " ":                # if user's click point is valid and not occupied
                    try:                                # try
                        del self.click[0]               # delete click point turtle so that one click will be affected
                    except:                             # if there is an error
                        return 0                        # return and do nothing
                    self.draw_markings(mk,i)            # draw marks on canvas  with user's mark and clicl location
                    self.lst[i-1] = mk                  # assign user's mark into class list
                    if self.check_winner(mk):           # check winner with class list  # if some one wins , lose or tie
                        turtle.Screen().onclick(None)   # set onclick None so that we can't click anymore
                    self.count += 1                     # increment count variable so that mark sings will change
                elif self.lst[i-1] != " ":              # if user's choice is occupied
                    # warn user if player's choice is occupied 
                    tur.write("Your input is occupied..", font=('Courier', 25, 'bold'),align='center') # warn user
                    time.sleep(0.5)                     # wait half seconds and 
                    tur.clear()                         # clear the warning

    def ask_ply_one_mark(self):                         # ask mark for player one 
        mark = "Z"     
        # assign mark variable with nonsense so that while loop  will be active                                 
        while mark not in ["X","O"]:                    # if the mark variable is not a valid mark
            # ask user to say your mark
            mark = ttt.screen.textinput("Welcome to the Tic Toe Game","Player 1's mark(O/X) => ").capitalize()
        self.ply_one_mark = "X" if mark == "X" else "O" # set ply_one's mark "X" or "O"
        self.ply_two_mark = "O" if mark == "X" else "X" # set ply_two's mark "X" or "O"
        # make a dictionary to match the sign and player
        self.mark_sign = {self.ply_one_mark:1,self.ply_two_mark:2}   

    def check_winner(self,mark):    # check winner function with mark_sign
        for i in range(0,7,3):      # check rows whether win or not
            if self.lst[i] == self.lst[i+1] == self.lst[i+2] == mark:   # if win with the signs
                # Declare player that wins with the signs  and 
                tur.write(f"Player {self.mark_sign[mark]} won the game.", font=('Courier', 25, 'bold'),align='center')
                return True         # return True
        for i in range(0,3):        # check columns whether win or not
            if self.lst[i] == self.lst[i+3] == self.lst[i+6] == mark:
                # Declare player that wins with the signs  and 
                tur.write(f"Player {self.mark_sign[mark]} won the game.", font=('Courier', 25, 'bold'),align='center')
                return True         # return True
        # check diagonals 
        if (self.lst[0] == self.lst[4]==self.lst[8]==mark) or (self.lst[2]==self.lst[4]==self.lst[6]==mark):
            tur.write(f"Player {self.mark_sign[mark]} won the game.", font=('Courier', 25, 'bold'),align='center')
            return True
        elif " " not in self.lst:   # if the canvas is full
            tur.write(f"A Tie match", font=('Courier', 25, 'bold'),align='center')  # declare a tie match 
            return True             # return True

    def choose_location(self):              # choose location method for user to make a click
        src = turtle.Screen()               # create an instance of screen 
        self.click.append(src)              # append that instance into click list
        self.click[0].onclick(self.fxn)     # make onclick function and invoke a method 
        
if __name__ == "__main__":                  # driver function
    game = Two_Players(600,600)             # create an instance of two_players with height and width
    game.ask_ply_one_mark()                 # invoke ask mark for player one
    # write an announcement with relating signs and players
    tur.write(f"Player 1 ({game.ply_one_mark}) Vs Player 2 ({game.ply_two_mark}) ", font=('Courier', 25, 'bold'),align='center')
    time.sleep(3)                           # wait 3 seconds for announcement
    tur.clear()                             # clear the announcement        

    # ------------------ For Two Players with Input Field ---------------------
    #
    # i = 0                                 # to check whether user make less than 10 choices or not     
    # while " " in game.lst and i < 9:      # always loop through while there will be blank spaces in list      
    #     mark = game.ply_one_mark if (i%2) == 0 else game.ply_two_mark     # assign user's mark and change 
    #     ply = game.mark_sign[mark]                                        # assign player with dictionary
    #     lct = game.ask_user_location(ply,mark)                            # ask user location
    #     game.draw_markings(mark,lct)                                      # draw marks with location and sign
    #     chk = game.check_winner(mark)                                     # check winner with marks
    #     if chk == 0 or chk == 1:                                          # if someone wins or there is a tie match
    #         break                                                         # break the loop
    #     i += 1                                                            # if no one wins , change next player
    # ttt.screen.exitonclick()                                              # make a screen exit on click
    #
    # ------------------ For Two players with click point ---------------------

    for j in range(9):                  # loop through 9 times as there are 9 places on board
        game.choose_location()          # invoke a method for choose location
    turtle.Screen().mainloop()          # call mainloop so that click points will be detected
