# Clase Car con apariencia random.


# Importación de módulos
import turtle
import random


# Creación de nueva clase Car.
class Car(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.turtlesize(stretch_len=2)
        self.goto(random.randint(310, 1000), random.randrange(-250,250,20))
        self.setheading(180)
