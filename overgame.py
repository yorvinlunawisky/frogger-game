# Crear un "game over" para el juego.

# Importar módulos turtle and constants
import turtle
import constants


# Nueva clase Overgame :
class OverGame(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.color("green")
        self.pensize(10)

    def write_over_game(self):
        self.write("¡HAS GANADO!", False, "center", constants.FONT)
