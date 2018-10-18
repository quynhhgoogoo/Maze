import turtle

#Set up
win = turtle.Screen()
win.bgcolor("white")
win.title("Maze game")
win.setup(width = 700,height = 700)


#Create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        #initialize Turtle class
        turtle.Turtle.__init__(self)
        self.shape("square")  
        self.color("black")
        self.penup()
        self.speed(0)

#Create Player
class Player(turtle.Turtle):
    def __init__(self):
        #initialize Turtle class
        turtle.Turtle.__init__(self)
        self.shape("square")  
        self.color("yellow")
        self.penup()
        self.speed(0)
        
    #Player Movement
    def player_up(self):
        #Check whether it is a wall or space
        if(self.xcor(), self.ycor()+24) not in walls:
            self.goto(self.xcor(), self.ycor() + 24)

    def player_down(self):
        #Check whether it is a wall or space
        if(self.xcor(), self.ycor()-24) not in walls:
            self.goto(self.xcor(), self.ycor() - 24)

    def player_right(self):
        #Check whether it is a wall or space
        if(self.xcor()+24, self.ycor()) not in walls:
            self.goto(self.xcor() + 24, self.ycor())

    def player_left(self):
        #Check whether it is a wall or space
        if(self.xcor()-24, self.ycor()) not in walls:
            self.goto(self.xcor() - 24, self.ycor())

#Create Levels
levels = [""]

#First level
level1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXX          P XXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X       XX  XXX        XX",
"XXXXXX  XX  XXX        XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXX        XXXX  XXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"X                XXXXXXXX",
"XXXXXXXXXXXX     XXXXX  X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX  XXXXXXXXXX         X",
"XXX                     X",
"XXX         XXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX              X",
"XX   XXXXX              X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX    XXXXXXXXXXXX  XXXXX",
"XX           XXXX       X",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]

#Append level 1 to level list
levels.append(level1)

#Set up maze
def SetupMaze(level):
    for y in range(25):
        for x in range(25):
            #Create blocks of wall for maze
            block = level[y][x]
            #Calculate coordinates for each blocks of wall
            block_x = -288 + (x*24)
            block_y = 288 - (y*24)
            
            #Build wall
            if block == "X":
                pen.goto(block_x, block_y)
                pen.stamp()    #Put block on screen and leave it there
                #Add coordinates to wall list
                walls.append((block_x, block_y))

            #Build player
            if block == "P":
                player.goto(block_x, block_y)
                
    
#Create Pen instances
pen = Pen()
player = Player()

#Create wall as an obstacle
walls=[]

#Set up Level
SetupMaze(levels[1])
#print(walls)

#Keyboard binding
win.listen()
win.onkeypress(player.player_up,"Up")
win.onkeypress(player.player_down,"Down")
win.onkeypress(player.player_right,"Right")
win.onkeypress(player.player_left,"Left")

#Main Game loop
while True:
    win.update()


