# Crear un "game over" para el juego.

# Importar módulos turtle and constants
import turtle
import constants


# Nueva clase GameOver :
class GameOver(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.color("red")
        self.pensize(6)

    # Mensaje mostrado al perder una partida.
    def write_game_over(self):
        self.write("GAME OVER", False, "center", constants.FONT)