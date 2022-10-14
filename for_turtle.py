import turtle               # import turtle library
import time                 # import time library
screen = turtle.Screen()    # initialize the screen for turtle
lines_points = [(-295,100),(-295,-100),(-100,295),(100,295)]    # tuple coordinate points to draw "X" or "Y"
angle_degress = [0,0,270,270]                                   # degree list to set heading for "X" or "Y"


class board:                # create a class
    POINTS = [(-290.0, 290.0,-110.0, 290.0,-110.0, 110.0,-290.0, 110.0),    # cooridnates of each sector
          (-90.0, 290.0, 90.0, 290.0, 90.0, 110.0, -90.0, 110.0), 
          (110.0, 290.0, 290.0, 290.0, 290.0, 110.0, 110.0, 110.0),
          (-290.0, 90.0, -110.0, 90.0, -110.0, -90.0, -290.0, -90.0), 
          (-90.0, 90.0, 90.0, 90.0, 90.0, -90.0, -90.0, -90.0), 
          (110.0, 90.0, 290.0, 90.0, 290.0, -90.0, 110.0, -90.0), 
          (-290.0, -110.0, -110.0, -110.0, -110.0, -290.0, -290.0, -290.0), 
          (-90.0, -110.0, 90.0, -110.0, 90.0, -290.0, -90.0, -290.0), 
          (110.0, -110.0, 290.0, -110.0, 290.0, -290.0, 110.0, -290.0)]

    # a dictionary to get the center point of each sector => key : sector number , values : coordinates tuples
    center_of_sectors = {1:(-197,197),2:(0,195),3:(197.5, 197.5),4:(-197.5, 0.0),5:(0.0, 0.0),6:(197.5, 0.0),7:(-197.5, -197.5),8:(0.0, -197.5),9:(197.5, -197.5)}
    def __init__(self,h:int,w:int): # constructor function to initialize an object (height of screen , width of screen)
        screen.setup(h,w)   # setup the screen with the parameters
        self.draw_lines()   # invoke a method of draw lines so that there will be nine sectors
    
    def draw_lines(self):   # method of draw lines
        for i in range(4):  # As there are four lines in a board of Tic Tac Toe , loop through four times
            lines = turtle.Turtle()             # initialize the turtle
            lines.speed("fast")                 # to make turtle faster
            lines.penup()                       # penup turtle not to appear black lines while moving the turtle
            lines.goto(lines_points[i])         # move the turtle specific coordinates with the line_points list
            lines.setheading(angle_degress[i])  # set the heading of turtle with the degrees list
            lines.pendown()                     # pendown so that black lines will be drown
            lines.pensize(3)                    # set the pensize of 3 to make big thickeness lines
            lines.forward(600)                  # draw a line habing a length of 600 pixels

    def draw_markings(self,sign:str,location:int):   # method of draw_markings : parameters("X" or "Y",sector_number)
        x , y = self.center_of_sectors[location]     # get the center coordinates related the sector
        if sign == "X":                              # if the sign is "X"
            # invoke the cross method to draw the "X" sign with the center coordinates
            self.cross(x,y)                          
        else:                                        # if the sign is "O"             
            # invoke the cross method to draw the "O" sign with the center coordinates
            self.circle(x,y)


    def circle(self,x,y):                           # circle method to draw circle on board
        # dictionary containing  based corodinates and radius of circle
        o_shape = {"coor":(x,y-80),"radius":80}     # As the circle is drew from the base , set the y-axis below   
        o = turtle.Turtle()                         # create a turtle instance
        o.speed("fast")                             # to make turtle faster
        o.penup()                                   # penup turtle not to appear black lines while moving the turtle
        o.setpos(o_shape["coor"])                   # move the turtle to the base start point of a circle
        o.pendown()                                 # pendown so that black lines will be drown      
        o.pensize(2)                                # set the pensize of 2 to make big thickeness lines
        o.hideturtle()                              # hide turtle to be visible only the sing
        o.color("firebrick")                        # set the color of a line
        o.circle(o_shape["radius"])                 # draw a circle with radius

    def cross(self,c_x,c_y):                        # cross method to draw cross on board    
        # nested dictionary containing  based corodinates and angles of heading and length of lines              
        x_shpae = {"coor":[(c_x-60,c_y+60),(c_x+60,c_y+60)],"angles":[315,225],"len":170}
        for i in range(2):                          # as there is 2 lines in cross , loop through two times
            x = turtle.Turtle()                     # create a turtle of instance
            x.speed("fast")                             # to make turtle faster
            x.penup()                               # penup turtle not to appear black lines while moving the turtle
            x.setpos(x_shpae["coor"][i])            # move the turtle to the base start point of a cross line
            x.pendown()                             # pendown so that black lines will be drown     
            x.pensize(2)                            # set the pensize of 2 to make big thickeness lines
            x.hideturtle()                          # hide turtle to be visible only the sing
            x.setheading(x_shpae["angles"][i])      # set the heading of a turtle to get a 45 degree angle line
            x.color("dark goldenrod")               # set the color of a line
            x.forward(x_shpae["len"])               # draw a line with the length

       # A utility function to calculate area of triangle formed by (x1, y1), (x2, y2) and (x3, y3)
    def area(self, x1, y1, x2, y2, x3, y3):
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)    # return the area of a triangle        

    # A function to check whether point P(x, y) lies inside the rectangle
    # formed by A(x1, y1), B(x2, y2), C(x3, y3) and D(x4, y4)
    def check(self, x1, y1, x2, y2, x3, y3, x4, y4, x, y):  
        # Calculate area of rectangle ABCD
        A = (self.area(x1, y1, x2, y2, x3, y3) + self.area(x1, y1, x4, y4, x3, y3))
        # Calculate area of triangle PAB
        A1 = self.area(x, y, x1, y1, x2, y2)
        # Calculate area of triangle PBC
        A2 = self.area(x, y, x2, y2, x3, y3)
        # Calculate area of triangle PCD
        A3 = self.area(x, y, x3, y3, x4, y4)
        # Calculate area of triangle PAD
        A4 = self.area(x, y, x1, y1, x4, y4)
        # Check if sum of A1, A2, A3  and A4 is same as A
        return (A == A1 + A2 + A3 + A4)  
                 