import turtle
import random
import sys

#Set up
win = turtle.Screen()
win.bgcolor("white")
win.title("Maze game")
win.setup(width = 700,height = 700)
win.tracer(0)

#Gold calculation
gold = 0

#Register shape
turtle.register_shape("ghost_left.gif")
turtle.register_shape("ghost_right.gif")
turtle.register_shape("treasure.gif")
turtle.register_shape("wall.gif")
turtle.register_shape("enemy.gif")

#Create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        #initialize Turtle class
        turtle.Turtle.__init__(self)
        #self.shape("square")  
        #self.color("black")
        self.shape("wall.gif")
        self.penup()
        self.speed(0)
        

#Create Player class
class Player(turtle.Turtle):
    def __init__(self):
        #initialize Turtle class
        turtle.Turtle.__init__(self)
        self.shape("ghost_left.gif")
        #self.shape("square")  
        #self.color("blue")
        self.penup()
        self.speed(0)
        self.score = 0
        
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
            self.shape("ghost_right.gif")

    def player_left(self):
        #Check whether it is a wall or space
        if(self.xcor()-24, self.ycor()) not in walls:
            self.goto(self.xcor() - 24, self.ycor())
            self.shape("ghost_left.gif")

    #Check whether Player and Treasure have a collision
    def collision(self, treasure):
        if (self.xcor() == treasure.xcor() and self.ycor() == treasure.ycor()):
            return True
        else:
            return False

#Create Treasure class
class Treasure(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("treasure.gif")
        #self.shape("circle")  
        #self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    #Make treasure disappear
    def hideTreasure(self):
        self.goto(1000,1000)
        self.hideturtle()

#Create Enemy
class Enemy(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("enemy.gif")
        self.penup()
        self.speed(0)
        self.goto(x,y)
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        #Create change in enemy coordinate
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0

        #Calculate the coordinates after enemy movement
        enemy_x = self.xcor() + dx
        enemy_y = self.ycor() + dy
        #Enemy Movement
        if(enemy_x,enemy_y) not in walls:
            self.goto(enemy_x, enemy_y)
        else:
            #Choose direction again
            self.direction = random.choice(["up", "down", "left", "right"])

        #Set timer for enemy to move next time
        turtle.ontimer(self.move, t=random.randint(100,400))

    def hideEnemy(self):
        self.goto(1000,1000)
        self.hideturtle()

#Score
score = turtle.Turtle()
score.speed(0)
score.color("black")
score.hideturtle
score.penup()
score.goto(0,320)
score.write("Player Gold : 0", align ="center", font =("Courier", 12, "normal"))

#Game over
gameover = turtle.Turtle()
gameover.speed(0)
gameover.color("black")
gameover.hideturtle
gameover.penup()
gameover.goto(0,0)

#Create Treasures
treasures =[]

#Create Levels
levels = [""]

#Create Enemies
enemies = []

#First level
level1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXE          XXXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"XP       XX  XXX        XX",
"XXXXXX  XX  XXX        XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XT    XXXX  XXXXX",
"X  XXX        XXXX  EXXXX",
"X  XXX  XXXXXXXXXXTXXXXXX",
"X         XXXXXXXXXXXXXXX",
"X                EXXXXXXX",
"XXXXXXXXXXXX     XXXXX  X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX  XXXXXXXXXX         X",
"XXX                     X",
"XXX         EXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX              X",
"XXT   XXXXE             X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX    XXXXXXXXXXXX  XXXXX",
"XX           XXXX       X",
"XXXE                    X",
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

            #Build treasure
            if block == "T":
                treasures.append(Treasure(block_x, block_y))

            #Build enemies
            if block == "E":
                enemies.append(Enemy(block_x, block_y))
                
    
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

#Set timer to keep enemy moves instantly
for enemy in enemies:
    turtle.ontimer(enemy.move, t = 300)

#Main Game loop
while True:
    #If player gets treasure
    for treasure in treasures:
        if player.collision(treasure):
            player.score = player.score + treasure.gold
            gold = player.score
            score.clear()
            score.write("Player Gold :{}".format(gold), align ="center", font =("Courier", 12, "normal"))
            #print("Player Gold :{}".format(player.score))
            #Hide treasure
            treasure.hideTreasure()
            #Remove treasure from treasures list
            treasures.remove(treasure)

    #If player meets enemy
    for enemy in enemies:
        if player.collision(enemy):
            print("You die")
            gameover.write("You die", align ="center", font =("Courier", 24, "normal"))
            sys.exit()
        
    win.update()


