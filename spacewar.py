# SpaceWar Python 3.8

import turtle
import os
import random
import winsound
import time

game_dir = "C:\\Users\\smachonis\\Coding Projects\\SpaceWar\\"
wn = turtle.Screen()
wn.screensize(800, 800)
wn.bgcolor("black")
wn.title("SpaceWar by @foxvalleygames")
wn.bgpic(game_dir+"bgimg.gif")
wn.tracer(0)

class Game():
    def __init__(self):
        self.level = 1
        self.lives = 3
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.pen.hideturtle()

    def draw_border(self):
        self.pen.color("white")
        self.pen.speed(0)
        self.pen.pensize(5)
        self.pen.penup()
        self.pen.goto(-300,-300)
        self.pen.pendown()
        self.pen.goto(-300, 300)
        self.pen.goto(300, 300)
        self.pen.goto(300, -300)
        self.pen.goto(-300, -300)
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.pendown()

    def show_status(self):
        self.pen.undo()
        self.pen.penup()
        self.pen.goto(-300, 310)
        self.pen.write("Score: {}  Lives: {}".format(self.score, self.lives), False, align="left", font=("Arial", 16, "normal"))
        
    def play_sound(self, filename = ""):
        winsound.PlaySound(game_dir+filename, winsound.SND_ASYNC)

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.penup()
        self.color(color)
        self.shape(spriteshape)
        self.goto(startx, starty)
        self.speed = 1

    def move(self):
        self.forward(self.speed)

        # Border Checking
        if self.xcor() > 290 or self.xcor() < -290:
            self.right(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.right(60)

    def is_collision(self, other):
        if self.distance(other) < 20:
            return True
        else:
            return False

    def jump(self):
        self.goto(random.randint(-250,250),random.randint(-250,250))

class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
        self.speed = 1
        self.maxspeed = 6

    def turn_left(self):
        self.left(45)

    def turn_right(self):
        self.right(45)

    def accelerate(self):
        if self.speed < self.maxspeed:
            self.speed += 1

    def decelerate(self):
        if self.speed > 0:
            self.speed -= 1

class Particle(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.goto(-1000,-1000)
        self.shapesize(stretch_len=0.1, stretch_wid=0.1,outline=None)
        self.speed = 5
        self.frame = 0

    def explode(self, startx, starty):
        self.goto(startx, starty)
        self.setheading(random.randint(0, 360))

    def move(self):
        if self.frame >= 0 and self.frame <= 15:
            self.forward(self.speed)
            self.frame += 1
        else:
            self.frame = 0
            self.goto(-1000,-1000)


class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 1
        self.setheading(random.randint(0, 360))

class Ally(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 1
        self.setheading(random.randint(0, 360))

    def move(self):
        self.forward(self.speed)

        # Border Checking
        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() < -290:
            self.left(60)

class Missile(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_len=0.4, stretch_wid=0.2,outline=None)
        self.speed = 3
        self.status = "ready"
        self.goto(-1000,1000)

    def fire(self):
        if self.status == "ready":
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"
            game.play_sound("laser.wav")
        
    def move(self):
        if self.status == "ready":
            self.goto(-1000,1000)
        if self.status == "firing":
            self.forward(self.speed)
        
        # Border Checking
        if self.xcor() > 290 or self.xcor() < -290 or self.ycor() > 290 or self.ycor() < -290:
            self.goto(-1000,1000)
            self.status = "ready"

game = Game()
game.draw_border()
game.show_status()

player = Player("triangle","white", 0, 0)
#enemy = Enemy("circle", "red", -100, 0)
missile = Missile("triangle", "yellow",0, 0)
#ally = Ally("square", "blue", -250, 250)

allies = []
for i in range(5):
    allies.append(Ally("square", "blue", random.randint(-250,250),random.randint(-250,250)))

enemies = []
for i in range(5):
    enemies.append(Enemy("circle", "red", random.randint(-250,250),random.randint(-250,250)))

particles = []
for i in range(20):
    particles.append(Particle("circle", "orange", 0, 0))

# Keyboard Bindings
wn.listen()
wn.onkeypress(player.turn_left, "Left")
wn.onkeypress(player.turn_right, "Right")
wn.onkeypress(player.accelerate, "Up")
wn.onkeypress(player.decelerate, "Down")
wn.onkeypress(missile.fire, "space")

while True:
    wn.update()
    #time.sleep(0.001)  

    player.move()
    missile.move()

    for particle in particles:
        particle.move()

    for enemy in enemies:
        enemy.move()
        if player.is_collision(enemy):
            enemy.jump()
            game.score -= 100
            game.lives -= 1
            game.play_sound("explosion.wav")
            game.show_status()

        if missile.is_collision(enemy):
            enemy.jump()
            missile.status = "ready"
            game.score += 100
            game.show_status()
            for particle in particles:
                particle.explode(missile.xcor(), missile.ycor())

    for ally in allies:
        ally.move()
        if player.is_collision(ally):
            ally.jump()
            game.score -= 100
            game.lives -= 1
            game.play_sound("explosion.wav")
            game.show_status()

        if missile.is_collision(ally):
            ally.jump()
            missile.status = "ready"
            game.score -= 100
            game.show_status()
