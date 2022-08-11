# TODO: 2.  Create a player turtle class.

# Import modules:
import turtle
import constants


# Creación de nueva clase:
class Player(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.goto(constants.START)
        self.setheading(90)

    def move_forward(self):
        self.forward(constants.MOVE_SPEED)

    def goto_start(self):
        self.goto(constants.START)
