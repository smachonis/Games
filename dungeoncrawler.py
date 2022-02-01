import turtle
import random

game_dir = "C:\\Users\\smachonis\\Coding Projects\\Dungeon Crawler\\"
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Simple Maze")
wn.setup(700,700)
wn.tracer(0)

wn.register_shape(game_dir+"wizard_right.gif")
wn.register_shape(game_dir+"wizard_left.gif")
wn.register_shape(game_dir+"goblin_right.gif")
wn.register_shape(game_dir+"goblin_left.gif")
wn.register_shape(game_dir+"treasure.gif")
wn.register_shape(game_dir+"wall.gif")
wn.register_shape(game_dir+"up_bolt.gif")
wn.register_shape(game_dir+"down_bolt.gif")
wn.register_shape(game_dir+"left_bolt.gif")
wn.register_shape(game_dir+"right_bolt.gif")
wn.register_shape(game_dir+"key.gif")
wn.register_shape(game_dir+"keyhole.gif")
wn.register_shape(game_dir+"door.gif")
wn.register_shape(game_dir+"blackhole.gif")

class Game(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-290, 310)
        self.speed(0)

    def update_score(self):
        self.clear()
        self.write("Player HP: {}  Lives: {}  Gold: {}  Keys: {}".format(player.hp, player.lives, player.gold, player.keys), False, align="left", font=("Arial", 14, "normal"))

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(game_dir+"wizard_right.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.last_dir = "left"
        self.gold = 0
        self.keys = 0
        self.lives = 3
        self.maxhp = 3
        self.hp = self.maxhp        
        self.currlevel = 1

    def go_up(self):
        x = self.xcor()
        y = self.ycor()+24
        if (x, y) not in walls:
            self.last_dir = "up"
            self.goto(x, y)
            self.setheading(90)

    def go_down(self):
        x = self.xcor()
        y = self.ycor()-24
        if (x, y) not in walls:
            self.last_dir = "down"
            self.goto(x, y)
            self.setheading(270)

    def go_left(self):
        x = self.xcor()-24
        y = self.ycor()
        if (x, y) not in walls:
            self.last_dir = "left"
            self.goto(x, y)
            self.setheading(180)
            self.shape(game_dir+"wizard_left.gif")

    def go_right(self):
        x = self.xcor()+24
        y = self.ycor()
        if (x, y) not in walls:
            self.last_dir = "right"
            self.goto(x, y)
            self.setheading(0)
            self.shape(game_dir+"wizard_right.gif")

    def is_collision(self, other):
        if self.distance(other) < 5:
            return True
        else:
            return False

class Bolt(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5,outline=None)
        self.color("green")
        self.penup()
        self.speed(0)
        self.speed = 3
        self.goto(-1000,1000)
        self.status = "ready"

    def fire(self):
        if self.status == "ready":
            self.goto(player.xcor(), player.ycor())
            h = player.heading()
            if h == 90:
                self.shape(game_dir+"up_bolt.gif")
            elif h == 270:
                self.shape(game_dir+"down_bolt.gif")
            elif h == 180:
                self.shape(game_dir+"left_bolt.gif")
            elif h == 0:
                self.shape(game_dir+"right_bolt.gif")
            self.setheading(h)
            self.status = "firing"
        
    def move(self):
        if self.status == "ready":
            self.goto(-1000,1000)
        if self.status == "firing":
            self.forward(self.speed)
        
        # Border Checking
        if (self.xcor(), self.ycor()) in walls:
            self.goto(-1000,1000)
            self.status = "ready"

    def disappear(self):
        self.goto(-1000,1000)
        self.status = "ready"

class Door(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape(game_dir+"door.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.goto(x,y)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape(game_dir+"treasure.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x,y)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

class Key(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape(game_dir+"key.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.goto(x,y)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

class Keyhole(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape(game_dir+"keyhole.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.goto(x,y)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

class Goblin(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape(game_dir+"goblin_left.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.hp = 1
        self.speed = 750
        self.goto(x,y)
        self.direction = random.choice(["up","down","left","right"])

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
            self.shape(game_dir+"goblin_left.gif")
        elif self.direction == "right":
            dx = 24
            dy = 0
            self.shape(game_dir+"goblin_right.gif")
        else:
            dx = 0
            dy = 0

        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"

        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in walls and (move_to_x, move_to_y) not in blocked_keyholes:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction = random.choice(["up","down","left","right"])

        wn.ontimer(self.move, t=self.speed)        
    
    def is_close(self, other):
        if self.distance(other) < 75:
            return True
        else:
            return False

    def is_collision(self, other):
        if self.distance(other) < 20:
            return True
        else:
            return False
    
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

class Blackhole(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape(game_dir+"blackhole.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 50
        self.hp = 2
        self.speed = 1250
        self.goto(x,y)
        self.direction = random.choice(["up","down","left","right"])

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0

        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"

        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in walls and (move_to_x, move_to_y) not in blocked_keyholes:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction = random.choice(["up","down","left","right"])

        wn.ontimer(self.move, t=self.speed)        
    
    def is_close(self, other):
        if self.distance(other) < 75:
            return True
        else:
            return False

    def is_collision(self, other):
        if self.distance(other) < 20:
            return True
        else:
            return False
    
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

levels = [""]

level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP X                X   X",
    "X  XXXXXXX   XXXXX    E X",
    "X       X    X      XXX X",
    "X       X    XXXXX      X",
    "XXXXX   X    X      XXX X",
    "X   X   X    XXXXX    X X",
    "X   X   X    X      XXX X",
    "X   X        X  XX  X  KX",
    "X            XXXXXT X   X",
    "XXXXXXXXX  XXX   XXXX  XX",
    "XX      X  XX        E XX",
    "XX  XX  X  XXXX  XX  XXXX",
    "XX  XT  X        XX     X",
    "XX  XXXXX  XXXXXXXX  XXXX",
    "XX         B  X        XX",
    "XXXX  XXX  X  X  XXXX  XX",
    "X     X X  X  X  X  X  XX",
    "X       X  XXXX  X      X",
    "X  X T  X    X   XXXXX  X",
    "X  XXXXXX    X       X  X",
    "X        E XXXXXXXX  X  X",
    "XXXXXXXXXXXXX        X  X",
    "XD          H E      XXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

level_2 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP  XXX  XXX    TX   E  X",
    "XX  XXX       XXXX  XX  X",
    "XX  XXX  XXXXXXXXX  XX  X",
    "XX                  XX  X",
    "XXXXXX  E   XXXXXXXXXX  X",
    "XXXXXX  XXXXXXX      X  X",
    "XX          XXX  XX  X  X",
    "XX  XXXXXXXXXXX  XX  X  X",
    "X    XX    E     XX     X",
    "XXX  XX  XXXXXXXXXXXXXXXX",
    "X X  XX  XXXXXX        XX",
    "X X  XX  XXT XX  XXXX  XX",
    "X    XX  XXB     X KX  XX",
    "X  XXXX  XX  XX  X  X  XX",
    "X  XXXX  XXXXXX  X     XX",
    "X   X            XXXX  XX",
    "X E XXXXXXXXXXXXX      XX",
    "X   X        X  X  XXXXXX",
    "XX TX    XX  X         XX",
    "XXXXXXX  XX  XXXX  XX  XX",
    "X E      XX        XX  XX",
    "X  XXXXXXXXXXXXXXXXXXXXXX",
    "X   H                  DX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

levels.append(level_1)
levels.append(level_2)

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape(game_dir+"wall.gif")
                pen.stamp()
                # Add coordinates to wall list
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)
                player_start.append((screen_x, screen_y))
            
            if character == "D":
                door.goto(screen_x, screen_y)

            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))
            
            if character == "K":
                keys.append(Key(screen_x, screen_y))

            if character == "H":
                keyholes.append(Keyhole(screen_x, screen_y))
                blocked_keyholes.append((screen_x, screen_y))
            
            if character == "E":
                goblins.append(Goblin(screen_x, screen_y))

            if character == "B":
                blackholes.append(Blackhole(screen_x, screen_y))

                
game = Game()
pen = Pen()
player = Player()
bolt = Bolt()
door = Door(-1000,1000)

walls = []
treasures = []
goblins = []
blackholes = []
keys = []
keyholes = []
blocked_keyholes = []
player_start = []
game.update_score()



setup_maze(levels[1])
print ("Player Start: {}".format(player_start))
print (player_start[0][0])
print (player_start[0][1])
for goblin in goblins:
    wn.ontimer(goblin.move, t=goblin.speed)

for blackhole in blackholes:
    wn.ontimer(blackhole.move, t=blackhole.speed)

wn.listen()
wn.onkeypress(player.go_left, "a")
wn.onkeypress(player.go_right, "d")
wn.onkeypress(player.go_up, "w")
wn.onkeypress(player.go_down, "s")
wn.onkeypress(bolt.fire, "space")

while True:
    wn.update()
    bolt.move()

    if player.is_collision(door):
        pen.clearstamps()
        walls.clear()
        blocked_keyholes.clear()
        player_start.clear()        
        for treasure in treasures:
            treasure.destroy()
            treasures.remove(treasure)
        for key in keys:
            key.destroy()
            keys.remove(key)
        for keyhole in keyholes:
            keyhole.destroy()
            keyholes.remove(keyhole)
        for goblin in goblins:
            goblin.destroy()
            goblins.remove(goblin)
        for blackhole in blackholes:
            blackhole.destroy()
            blackholes.remove(blackhole)
            
        player.currlevel += 1
        setup_maze(levels[player.currlevel])
        game.update_score()

        for goblin in goblins:
            wn.ontimer(goblin.move, t=goblin.speed)

        for blackhole in blackholes:
            wn.ontimer(blackhole.move, t=blackhole.speed)
               

    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print("Player Gold: {}".format(player.gold))
            game.update_score()
            treasure.destroy()
            treasures.remove(treasure)
    
    for key in keys:
        if player.is_collision(key):
            player.keys += 1
            print("Player Has {} key(s)".format(player.keys))
            game.update_score()
            key.destroy()
            keys.remove(key)
    for keyhole in keyholes:
        if player.is_collision(keyhole):
            if player.keys > 0:
                player.keys -= 1
                print("Door Unlocked. {} Key(s) left".format(player.keys))
                game.update_score()
                keyhole.destroy()
                keyholes.remove(keyhole)
            else:
                print("Door is Locked.  You need a key")
                if player.last_dir == "left":
                    player.go_right()
                elif player.last_dir == "right":
                    player.go_left()
                elif player.last_dir == "up":
                    player.go_down()
                elif player.last_dir == "down":
                    player.go_up()

    for goblin in goblins:
        if player.is_collision(goblin):
            player.hp -= 1
            if player.hp <= 0:
                player.lives -= 1
                if player.lives <= 0:
                    player.goto(1000,1000)
                    game.update_score()
                    print("Game Over")
                else:
                    player.hp = player.maxhp
                    player.goto(player_start[0][0], player_start[0][1])
                    game.update_score()
        
        if goblin.is_collision(bolt):
            if goblin.hp > 1:
                goblin.hp -= 1
                bolt.disappear()
            else:
                player.gold += goblin.gold
                print("Player Gold: {}".format(player.gold))
                game.update_score()
                goblin.destroy()
                goblins.remove(goblin)
                bolt.disappear()

    for blackhole in blackholes:
        if player.is_collision(blackhole):
            player.hp -= 1
            if player.hp <= 0:
                player.lives -= 1
                if player.lives <= 0:
                    player.goto(1000,1000)
                    game.update_score()
                    print("Game Over")
                else:
                    player.hp = player.maxhp
                    player.goto(player_start[0][0], player_start[0][1])
                    game.update_score()

        
        if blackhole.is_collision(bolt):
            if blackhole.hp > 1:
                blackhole.hp -= 1
                bolt.disappear()
            else:
                player.gold += blackhole.gold
                print("Player Gold: {}".format(player.gold))
                game.update_score()
                blackhole.destroy()
                blackholes.remove(blackhole)
                bolt.disappear()

            