import turtle

#CONSTANTS
SIDE_LENGTH = 300

#Turtle Conditions
turtle.hideturtle()
turtle.speed(0)

#Draw the Box 
turtle.goto(SIDE_LENGTH,0)
turtle.goto(SIDE_LENGTH, SIDE_LENGTH)
turtle.goto(0, SIDE_LENGTH)
turtle.goto(0,0)

#Travel to the center of the box, leaving no marks on the way.
turtle.penup()
turtle.goto(SIDE_LENGTH/2, SIDE_LENGTH/2)
turtle.showturtle()

turtle.speed(3)

keepGoing = True
while keepGoing == True:
    direction = input("Direction? (N,S,E,W): ") #if a value other than N,S,E,W entered, print DONE!
    if direction == "N":
        turtle.setheading(90)
    elif direction == "W":
        turtle.setheading(180)
    elif direction == "S":
        turtle.setheading(270)
    elif direction == "E":
        turtle.setheading(0)
    else:
        keepGoing = False
        break
    #Ask the user how far the turtle should go
    distance = int(input("Distance?: "))
    turtle.forward(distance)
    #Check if the turtle is inside or outside the box
    x = turtle.xcor()
    y = turtle.ycor()
    if (x < 0) or (x > SIDE_LENGTH) or (y < 0) or (y > SIDE_LENGTH):
        print("OUTSIDE!")
    else:
        print("INSIDE!")
        
print("DONE!")


