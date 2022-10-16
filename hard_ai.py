# Unbeatable computer mode is designed with the Minimax algorithm.
# Minimax algorithm is a backtracking algorithm to calculate all possible moves of opponents
# and get the best move 


class Unbeatable:                           # create a Unbeatable class for minmax algorithm

    def __init__(self,player:str,ai:str):   # intialize a class with player mark and ai mark
        self.player = player                # set player mark
        self.ai = ai                        # set ai mark
        self.lst = ["O"," "," ","O"," "," "," "," "," "]

    # test function for all available places
    def ai_hd(self):
        best = -1000                    # set the initial value to minimize 
        best_mv = None                  # declare best move
        for i in range(9):              # for all available places
            if self.lst[i] == " ":           # if the place is available
                self.lst[i] = self.player         # assign  that position with player's mark
                val = self.find_best(False,0) # call the minimax algorithm with False boolean which meamns to maximize
                self.lst[i] = " "                    # remove player's mark
                if val > best:                  # if the value from recursion is greater than the initial value
                    best_mv =  i                # assign that position as best move for AI
                    best = val                  # reassing the initial value with the value from recursion
        return best_mv

    # unbeatable mode for ai
    # find best position for ai to beat player using minmax algorithm
    def find_best(self,isMax,depth):    # (boolean,depth)

        val = self.check_winner_ai()    # check winner to check who got terminal state
        if val == 10:                   # if player wins
            return val - depth          # return 10 
        if val == -10:                  # if ai wins
            return val + depth          # return 10 
        if " " not in self.lst:         # if the board is full
            return 0                    # return 0
        if isMax:                       # if True boolean condition
            # set the negative compared value so that nearly every conditions is greater 
            best = -1000                
            best_mv = None              # set the best move as none
            for i in range(9):          # loop through the all states  to find best move     
                if self.lst[i] == " ":       # if the position is empty   
                    self.lst[i] = self.player     # set that position with player mark      
                    # if we've inserted that postion , find the other possibilities 
                    # by assigning AI mark and return the value => turn minimizing
                    eval = self.find_best(not isMax,depth + 1)   # recursion (False boolean , depth + 1)
                    self.lst[i] = " "                            # after recursive , remove player mark in that position 
                    if eval > best:     # if the value is greater than the compared value ;
                        best = eval     # assign that value into that compared value
                        best_mv = i     # set that postion as best_position
            return best_mv              #  return the best_position
        else:                           # if False boolean condition
            # set the postitive compared value so that nearly every conditions is greater 
            best = 1000                 
            best_mv = None              # set the best move as none
            for i in range(9):          # loop through the all states  to find best move  
                if self.lst[i] == " ":            # if the position is empty
                    self.lst[i] = self.ai         # set that position with ai mark
                    # if we've inserted that postion , find the other possibilities 
                    # by assigning AI mark and return the value => turn maximizing
                    eval = self.find_best(isMax,depth+1)     # recursion (True boolean , depth + 1) 
                    self.lst[i] = " "                        # after recursive , remove player mark in that position 
                    if eval < best:                          # if the value is greater than the compared value ;              
                            best = eval                      # assign that value into that compared value
                            best_mv = i                      # set that postion as best_position
            return best_mv                                   # return the best position

    def check_winner_ai(self):
        for i in range(0,7,3):                                  # check rows whether win or not
            if self.lst[i] == self.lst[i+1] == self.lst[i+2]:   # if someone wins
                if self.lst[i] == self.player:                  # if player's possible move wins
                    return 10                                   # return 10
                elif self.lst[i] == self.ai:                    # if ai's move wins
                    return -10                                  # return -10
        for i in range(0,3):                                    # check columns whether win or not
            if self.lst[i] == self.lst[i+3] == self.lst[i+6]:
                if self.lst[i] == self.player:
                    return 10
                elif self.lst[i] == self.ai:
                    return -10
        if (self.lst[0] == self.lst[4]==self.lst[8]):           # check the up left diagonal 
            if self.lst[i] == self.player:
                return 10
            elif self.lst[i] == self.ai:
                return -10
        elif  (self.lst[2]==self.lst[4]==self.lst[6]):          # chek the up right diagonal
            if self.lst[i] == self.player:
                return 10
            elif self.lst[i] == self.ai:
                return -10

hd = Unbeatable("O","X")
pos = hd.ai_hd()
hd.lst[pos] = hd.ai
print(hd.lst)