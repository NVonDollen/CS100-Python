import turtle
import random

#Global consts
TILE_SIZE = 40
PERSON_SIZE = TILE_SIZE*0.8
MAP_ROWS = 10
MAP_COLS = 15
SEED = 42
VALID_MOVE_TILES = (0,1)
TILE_COLORS = ("green","dark green","blue")
SAVE_FILENAME = "VONDOLLEN" +"_SAVE.txt"

#Global vars
playerRow = 5
playerCol = 5
mapData = []
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
    tileType = random.randint(0,10)
    if tileType < 5:
        return "green"
    elif tileType < 9:
        return "dark green"
    else:
        return "blue"

def getTruePixelCenter(row,col):
    cx = TILE_SIZE / 2 + col * TILE_SIZE - TILE_SIZE * MAP_COLS / 2
    cy = TILE_SIZE / 2 + row * TILE_SIZE - TILE_SIZE * MAP_ROWS / 2
    return cx, cy

def drawTile(row,col):
    global mapData
    cx,cy = getTruePixelCenter(row,col)
    tileType = mapData[row][col]
    color = TILE_COLORS[tileType]
    drawRectangle(cx,cy,TILE_SIZE-1,TILE_SIZE-1,color)

def drawMap():
    for i in range(MAP_ROWS):
        for j in range(MAP_COLS):
            drawTile(i,j)

def drawCharacter(row,col):
    cx,cy = getTruePixelCenter(row,col)
    drawRectangle(cx,cy - PERSON_SIZE/6, PERSON_SIZE, 2*PERSON_SIZE/3, "red")
    drawRectangle(cx,cy + PERSON_SIZE/3, PERSON_SIZE/3, PERSON_SIZE/3, "yellow")
    
def drawScreen():
    random.seed(SEED)
    turtle.clear
    drawMap()
    drawCharacter(playerRow,playerCol)
    turtle.update()
    
def moveLeft():
    global playerCol
    if isValidMove(playerRow,playerCol-1):
        playerCol -= 1
    drawScreen()
    
def moveRight():
    global playerCol
    if isValidMove(playerRow,playerCol+1):
        playerCol += 1
    drawScreen()
    
def moveUp():
    global playerRow
    if isValidMove(playerRow+1,playerCol):
        playerRow += 1
    drawScreen()
    
def moveDown():
    global playerRow
    if isValidMove(playerRow-1,playerCol):
        playerRow -= 1
    drawScreen()

def isValidMove(row,col):
    if mapData[row][col] in VALID_MOVE_TILES:
        return True
    else:
        return False

def loadMap(filename):
    map = []
    try:
        f = open(filename,"r")
        for row in range(MAP_ROWS):
            map.append([]) 
            for col in range(MAP_COLS):
                tileType = int(f.readline())
                #print(row, " ", col)
                map[row].append(tileType)
        f.close()
    except IOError as err:
        print(err)
        map = []
    except ValueError as err:
        f.close()
        print(err)
        map = []
    return map

def loadGame():
    try:
        f = open(SAVE_FILENAME,"r")
        global playerRow
        playerRow = int(f.readline())
        global playerCol
        playerCol = int(f.readline())
        f.close()
    except Exception:
        print("")
    
def saveGame():
    try:
        #print(playerRow)
        #print(playerCol)
        f = open(SAVE_FILENAME,"w")
        f.write(str(playerRow) +"\n")
        f.write(str(playerCol) + "\n")
        f.close()
        print("Game saved.")
    except Exception:
        print("ERROR: Could not save game!")
        

def main():
    filename = input("Enter a map to load: ")
    global mapData
    mapData = loadMap(filename)
    if len(mapData) is not 0:
        loadGame()
        turtle.hideturtle()
        turtle.tracer(0,0)
        turtle.setup(MAP_COLS*TILE_SIZE, MAP_ROWS*TILE_SIZE)
        turtle.onkey(moveRight, "d")
        turtle.onkey(moveLeft, "a")
        turtle.onkey(moveUp, "w")
        turtle.onkey(moveDown, "s")
        turtle.onkey(saveGame,"q")
        turtle.listen()
        drawScreen()
        turtle.done()
          
main()

