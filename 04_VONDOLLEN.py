import turtle
import random

#Global consts
TILE_SIZE = 40
PERSON_SIZE = TILE_SIZE*0.8
MAP_ROWS = 10
MAP_COLS = 15
SEED = 42

#Global vars
playerRow = 5
playerCol = 5

#=================FUNCTIONS===============================#

#copy drawRectangle()
def drawRectangle(x,y,width,height,color):
    turtle.penup()
    turtle.goto(x - width/2, y - height/2)
    turtle.color(color)
    turtle.pendown()

    turtle.begin_fill()

    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)

    turtle.end_fill()

#define getRandomTileType
def getRandomTileType():
    tileType = random.randint(1,10)
    if tileType < 5:
        return "green"
    elif (tileType >= 5) and (tileType < 9):
        return "dark green"
    else:
        return "blue"

def getTruePixelCenter(row,col):
    cx = TILE_SIZE / 2 + col * TILE_SIZE - TILE_SIZE * MAP_COLS / 2
    cy = TILE_SIZE / 2 + row * TILE_SIZE - TILE_SIZE * MAP_ROWS / 2
    return cx, cy

def drawTile(row,col):
    cx,cy = getTruePixelCenter(row,col)
    color = getRandomTileType()
    drawRectangle(cx,cy,TILE_SIZE-1,TILE_SIZE-1,color)

def drawMap():
    for i in range(MAP_ROWS):
        for j in range(MAP_COLS):
            drawTile(i,j)

def drawCharacter(row,col):
    cx,cy = getTruePixelCenter(row,col)
    drawRectangle(cx,cy - PERSON_SIZE/6, PERSON_SIZE, 2*PERSON_SIZE/3, "red")
    drawRectangle(cx,cy + PERSON_SIZE/6, PERSON_SIZE/3, PERSON_SIZE/3, "yellow")
    
def drawScreen():
    random.seed(SEED)
    drawMap()
    drawCharacter(playerRow,playerCol)
    turtle.update()
    
def moveLeft():
    global playerCol
    playerCol -= 1
    drawScreen()
    
def moveRight():
    global playerCol
    playerCol += 1
    drawScreen()
    
def moveUp():
    global playerRow
    playerRow += 1
    drawScreen()
    
def moveDown():
    global playerRow
    playerRow -= 1
    drawScreen()
    
def main():
    turtle.hideturtle()
    turtle.tracer(0,0)
    turtle.setup(MAP_COLS*TILE_SIZE, MAP_ROWS*TILE_SIZE)
    turtle.onkey(moveRight, "d")
    turtle.onkey(moveLeft, "a")
    turtle.onkey(moveUp, "w")
    turtle.onkey(moveDown, "s")
    turtle.listen()
    drawScreen()
    turtle.done()

main()
