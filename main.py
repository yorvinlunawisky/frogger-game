# Juego de cruce de tortuga (turtle crossing game).

# Cración de nueva ventana.

# Import modules
import turtle
import player
import carclass
import scoreboard
import gameover
import random
import time

# Configuración de pantalla:
screen = turtle.Screen()
screen.setup(width=600, height=800)
screen.bgcolor("white")
screen.title("Ayuda a la tortuga a cruzar la calle.")
screen.tracer(0)
screen.listen()
screen.colormode(255)

# Configurar jugador tortuga:
player = player.Player()

# Configurar puntos de la tortuga:
score = scoreboard.ScoreBoard()

# Configurar "juego finalizado":
game_is_over = gameover.GameOver()

# Configurar "juego ganado":
game_is_over = gameover.GameOver()

# Unir llaves de controles:
screen.onkey(fun=player.move_forward, key="w")

# Configurar loop principal del juego:
game_is_on = True
speed = 5
list_of_cars = []

while game_is_on:
    # Configurar actualización de pantalla:
    time.sleep(0.1)
    screen.update()

    # Creación de lógica para devolver al jugador al punto de partida.


    if player.ycor() >= 300:
        player.goto_start()
        score.track_score()
        speed += 2.5

# Configurar carro-tortuga:
    number = random.randint(1, 6)
    if number % 6 == 0:
        cars = carclass.Car()
        list_of_cars.append(cars)

# Mover tortugas
    for car in list_of_cars:
        car.forward(speed)

    # Detectar colisiones con los obstáculos/carros:
    for cars in list_of_cars:
        if player.distance(cars) < 20:
            game_is_over.write_game_over()
            game_is_on = False

# Salir del juego con un click:
screen.exitonclick()
