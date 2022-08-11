# Crear clase de pantalla de puntos y que le de seguimiento a los puntos.

# Importar módulos.
import turtle
import constants
import overgame
import time


# Configurar "juego finalizado":
you_win = overgame.OverGame()
screen = turtle.Screen()

# Crear una nueva clase para la pantala de puntos
class ScoreBoard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color("black")
        self.goto(-250, 260)
        self.level = 1
        self.write_score()

    def write_score(self):
        self.write(f"Nivel: {self.level}", False, "center", constants.FONT)

    def track_score(self):
        # i = 0
        while self.level < 5:
            self.level += 1
            self.clear()
            self.write_score()
            break
        if self.level == 5:
            you_win.write_over_game()
            screen.exitonclick()





