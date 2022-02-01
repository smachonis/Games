# Falling Skies in Python 3

import turtle
import random

score = 0
lives = 3
game_state = "start"

game_dir = "C:\\Users\\smachonis\\Coding Projects\\Boonefall\\"
wn = turtle.Screen()
wn.title("BooneFall")
wn.bgcolor("black")
wn.bgpic(game_dir+"bg.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

wn.register_shape(game_dir+"smallhound.gif")
wn.register_shape(game_dir+"smallmoon.gif")
wn.register_shape(game_dir+"smallball.gif")

# Add player

player = turtle.Turtle()
player.speed(0)
player.shape(game_dir+"smallhound.gif")
player.color("white")
player.penup()
player.goto(0,-250)
player.direction = ''
player.speed = 1

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.write("Score: {}  Lives: {}".format(score,lives), align="center", font=("Courier", 24, "normal"))

good_guys = []
number_of_good_guys = 10

for _ in range(number_of_good_guys):
    good_guy = turtle.Turtle()
    good_guy.speed(0)
    good_guy.shape(game_dir+"smallball.gif")
    good_guy.color("blue")
    good_guy.penup()
    good_guy.goto(random.randint(-380,380), random.randint(300,400))
    good_guy.speed = random.random()+.2
    good_guys.append(good_guy)

bad_guys = []
number_of_bad_guys = 10

for _ in range(number_of_bad_guys):
    bad_guy = turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.shape(game_dir+"smallmoon.gif")
    bad_guy.color("red")
    bad_guy.penup()
    bad_guy.goto(random.randint(-380,380), random.randint(300,400))
    bad_guy.speed = random.random()+.2
    bad_guys.append(bad_guy)

def move_left():
    player.direction = "left"

def move_right():
    player.direction = "right"

def move_player():
    if player.direction == 'left':
        x = player.xcor()
        x -= player.speed
        if x < -375:
            x = -375
        player.setx(x)

    if player.direction == 'right':
        x = player.xcor()
        x += player.speed
        if x > 375:
            x = 375
        player.setx(x)

def move_good_guys():
    for good_guy in good_guys:
        y = good_guy.ycor()
        x = good_guy.xcor()
        y -= good_guy.speed
        if y < -300:
            y = random.randint(300,400)
            x = random.randint(-380,380)
        elif good_guy.distance(player) < 40:
            global score
            score += 10
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score,lives), align="center", font=("Courier", 24, "normal"))
            y = random.randint(300,400)
            x = random.randint(-380,380)
        good_guy.goto(x,y)

def move_bad_guys():
    for bad_guy in bad_guys:
        y = bad_guy.ycor()
        x = bad_guy.xcor()
        y -= bad_guy.speed
        if y < -300:
            y = random.randint(300,400)
            x = random.randint(-380,380)
        elif bad_guy.distance(player) < 40:
            global score
            global lives
            score -= 10
            lives -= 1
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score,lives), align="center", font=("Courier", 24, "normal"))
            y = random.randint(300,400)
            x = random.randint(-380,380)
        bad_guy.goto(x,y)

def start_game():
    global game_state
    game_state = "running"

wn.listen()
wn.onkeypress(move_left, 'Left')
wn.onkeypress(move_right, 'Right')
wn.onkeypress(start_game, 'space')

while True:
    if game_state == "start":
        pen.clear()
        pen.write("Press Space to Start", align="center", font=("Courier", 24, "normal")) 
    elif game_state == "running":
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score,lives), align="center", font=("Courier", 24, "normal"))
        move_good_guys()
        move_bad_guys()
        move_player()
        if lives <= 0:
            game_state = "gameover"
    else:
        pen.clear()
        pen.write("GAME OVER! Final Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
    wn.update()