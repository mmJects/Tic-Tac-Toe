import turtle
import time
import for_turtle as ttt
from for_turtle import board as B

tur = turtle.Turtle()
tur.Screen().setup(600,600)
tur.hideturtle()
tur.penup()
tur.color("gold")

class Two_Players(B):
    count = 0
    click = []
    def __init__(self, h: int, w: int):
        super().__init__(h, w)
        self.lst = [" "," "," "," "," "," "," "," "," "]

    # function to ask user location with input field
    def ask_user_location(self,ply:int,mark:str):               
        chocies_lst = ["1","2","3","4","5","6","7","8","9"]     # to check user's inputs
        while True :                                            # always loop until break
            choice = ttt.screen.textinput(f"Your mark {mark}",f"Player {ply} enter the location on board(1-9)=>")
            if choice in chocies_lst:                           # if user only choose 1 to 9
                choice = int(choice)                        
                if self.lst[choice-1] == ' ':   # if user's input is valid     # subtract one from user choice
                    self.lst[choice-1] = mark   # assign mark in user's choice # beacuse board range is 0 to 8
                elif self.lst[choice-1] != ' ': # if user's mark is not empty
                    tur.write("Your input is occupied..", font=('Courier', 25, 'bold'),align='center') # warn user
                    time.sleep(2)
                    tur.clear()
                    continue
                break           # break the always looping if  the choice is corrext
        return choice           # return modified list 

    def fxn(self, x, y):
        for i in range(1,10):
            x1,y1,x2,y2,x3,y3,x4,y4 = self.POINTS[i-1]
            if self.check(x1,y1,x2,y2,x3,y3,x4,y4,x,y):
                mk = self.ply_one_mark if self.count % 2 == 0 else self.ply_two_mark
                if self.lst[i-1] == " ":
                    try:
                        del self.click[0]
                    except:
                        return 0
                    self.draw_markings(mk,i)
                    self.lst[i-1] = mk
                    if self.check_winner(mk):
                        turtle.Screen().onclick(None)
                    self.count += 1
                elif self.lst[i-1] != " ":
                    tur.write("Your input is occupied..", font=('Courier', 25, 'bold'),align='center') # warn user
                    time.sleep(0.5)
                    tur.clear()

    def ask_ply_one_mark(self):
        mark = "Z"
        while mark not in ["X","O"]:
            mark = ttt.screen.textinput("Welcome to the Tic Toe Game","Player 1's mark(O/X) => ").capitalize()
        self.ply_one_mark = "X" if mark == "X" else "O"
        self.ply_two_mark = "O" if mark == "X" else "X"
        self.mark_sign = {self.ply_one_mark:1,self.ply_two_mark:2}

    def check_winner(self,mark):
        for i in range(0,7,3):
            if self.lst[i] == self.lst[i+1] == self.lst[i+2] == mark:
                tur.write(f"Player {self.mark_sign[mark]} won the game.", font=('Courier', 25, 'bold'),align='center')
                return True  
        for i in range(0,3):
            if self.lst[i] == self.lst[i+3] == self.lst[i+6] == mark:
                tur.write(f"Player {self.mark_sign[mark]} won the game.", font=('Courier', 25, 'bold'),align='center')
                return True
        if (self.lst[0] == self.lst[4]==self.lst[8]==mark) or (self.lst[2]==self.lst[4]==self.lst[6]==mark):
            tur.write(f"Player {self.mark_sign[mark]} won the game.", font=('Courier', 25, 'bold'),align='center')
            return True
        elif " " not in self.lst:
            tur.write(f"A Tie match", font=('Courier', 25, 'bold'),align='center')
            return True

    def choose_location(self):
        src = turtle.Screen()
        self.click.append(src)
        self.click[0].onclick(self.fxn)
        
if __name__ == "__main__":
    game = Two_Players(600,600)
    game.ask_ply_one_mark()
    tur.write(f"Player 1 ({game.ply_one_mark}) Vs Player 2 ({game.ply_two_mark}) ", font=('Courier', 25, 'bold'),align='center')
    time.sleep(3)
    tur.clear()
    i = 0
    # ------------------ For Two Players with Input Field ---------------------
    # while " " in game.lst and i < 9:
    #     mark = game.ply_one_mark if (i%2) == 0 else game.ply_two_mark
    #     ply = game.mark_sign[mark]
    #     lct = game.ask_user_location(ply,mark)
    #     game.draw_markings(mark,lct)
    #     chk = game.check_winner(mark)
    #     if chk == 0 or chk == 1:
    #         break
    #     i += 1
    # ttt.screen.exitonclick()

    # ------------------ For Two players with click point ---------------------

    for j in range(9):
        game.choose_location()
    turtle.Screen().mainloop()
