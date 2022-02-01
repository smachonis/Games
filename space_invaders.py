import turtle
import random
import platform

if platform.system() == "Windows":
    try:
        import winsound
    except:
        print("Winsound module not available")

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.tracer(0)
wn.bgpic("c:\\users\\smachonis\\Coding Projects\\Space Invaders\\space_invaders_background.gif")

wn.register_shape("c:\\users\\smachonis\\Coding Projects\\Space Invaders\\invader.gif")
wn.register_shape("c:\\users\\smachonis\\Coding Projects\\Space Invaders\\player.gif")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.goto(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Score
score = 0

# Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.goto(-290,280)
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False, align="left", font=("Arial",14,"normal"))
score_pen.hideturtle()

# Enemies
number_of_enemies = 30
enemies = []
enemy_start_x = -200
enemy_start_y = 250
enemy_number = 0

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.speed(0)
    enemy.color("red")
    enemy.shape("c:\\users\\smachonis\\Coding Projects\\Space Invaders\\invader.gif")
    enemy.penup()
    x = enemy_start_x + (50 * enemy_number)
    y = enemy_start_y
    enemy.goto(x, y)
    enemy_number += 1
    if enemy_number == 10:
        enemy_start_y -= 50
        enemy_number = 0

enemyspeed = 0.10



bullet = turtle.Turtle()
bullet.speed(0)
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 2

# Bulletstate = ready or fire
bulletstate = "ready"


player = turtle.Turtle()
player.color("blue")
player.shape("c:\\users\\smachonis\\Coding Projects\\Space Invaders\\player.gif")
player.penup()
player.speed(0)
player.goto(0,-250)
player.setheading(90)

player.speed = 0

def move_left():
    player.speed = -0.65

def move_right():
    player.speed = 0.65
    
def move_player():
    x = player.xcor()
    x += player.speed
    if x < -280:
        x = -280
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # Move the bullet to the player
        x = player.xcor()
        y = player.ycor()
        bullet.goto(x, y+10)
        bullet.showturtle()
        play_sound("C:\\Users\\smachonis\\Coding Projects\\Space Invaders\\laser.wav")

def isCollision(t1, t2):
    if t1.distance(t2) < 15:
        return True
    else:
        return False

def play_sound(sound_file, time = 0):

    if platform.system() == "Windows":
        winsound.PlaySound(sound_file, winsound.SND_ASYNC)
    elif platform.system == "Linux":
        os.system("aplay -q {}&".format(sound_file))
    else:
        os.system("afplay {}&".format(sound_file))

    if time > 0:
        turtle.ontimer(lambda: play_sound(sound_file, time), t=int(time))

wn.listen()
wn.onkeypress(move_left,"Left")
wn.onkeypress(move_right,"Right")
wn.onkeypress(fire_bullet, "space")

play_sound("C:\\Users\\smachonis\\Coding Projects\\Space Invaders\\bgm.wav",119000)

while True:
    wn.update()
    move_player()
    
    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # Reverse and move enemy down
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                e.sety(y-40)
            enemyspeed *= -1    
        
        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                e.sety(y-30)
            enemyspeed *= -1

        # Check for hit
        if isCollision(bullet,enemy):
            # reset bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.goto(0, -400)

            # reset enemy
            #x = random.randint(-200,200)
            #y = random.randint(100,250)
            enemy.goto(0, 10000)

            score += 10
            scorestring = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial",14,"normal"))

            play_sound("C:\\Users\\smachonis\\Coding Projects\\Space Invaders\\explosion.wav")

        if isCollision(player,enemy):
            player.hideturtle()
            for ene in enemies:
                ene.hideturtle()
            print ("Game Over")
            break

    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"
