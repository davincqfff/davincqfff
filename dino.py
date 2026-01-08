import turtle
import time
import random


#skor
score=0
high_score=0

#untuk windows
wn=turtle.Screen()
wn.title("Projek Dino Lompat")
wn.bgcolor("white")
wn.setup(width=1280,height=960)
wn.tracer(0)

#untuk dino
kepala=turtle.Turtle()
kepala.speed(0)
kepala.shape("circle")
kepala.color("black")
kepala.penup()

ground_y=-200    #tanah berada di y-200
kepala.goto(-250,ground_y+30)   #kepala=badan+tinggi

#state buat dino
kepala.velocity_y=0
kepala.on_ground=True


#badan dino
badan=turtle.Turtle()
badan.speed(0)
badan.shape("square")
badan.color("green")
badan.penup()

badan.goto(-250,ground_y+10)

#sintax obstacle
obstacle=turtle.Turtle()
obstacle.speed(0)
obstacle.shape("square")
obstacle.color("black")
obstacle.penup()

#tinggi rnd dari obstacle
height=random.randint(40,100)
#ubah tinggi obstacle 20px per 1 strecth
obstacle.shapesize(stretch_wid=height/20,stretch_len=1)
#posisi obstacle
obstacle_x=700
obstacle_y=ground_y+height/2
obstacle.goto(obstacle_x,obstacle_y)

obstacle_speed=5
def jump():
    if kepala.on_ground:
        kepala.velocity_y=15
        kepala.on_ground=False

##pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,-400)
pen.write ("Score: 0 High Score: 0",align="center",font=("courier",30,"normal"))

#keybind
wn.listen()
wn.onkeypress(jump,"space")

#biar obstacle mau gerak ke kiri
while True:
    wn.update()
    #gerak kekiri
    x=obstacle.xcor()
    obstacle.setx(x-obstacle_speed)
    time.sleep(0.02)
    #reset obstacle kalau udah lewat layar
    if obstacle.xcor()<-700:
        obstacle.setx(700)
        height =random.randint(40,100)
        obstacle.shapesize(stretch_wid=height/20,stretch_len=1)
        obstacle.sety(ground_y+height/2)
        
    
        score+=1
        if score>high_score:
            high_score=score
        pen.clear()
        pen.write("Score:{} High Score:{}".format(score,high_score),align="center",font=("courier",30,"normal"))
        
    #pyshic
    kepala.velocity_y-=1
    kepala.sety(kepala.ycor()+kepala.velocity_y)
    badan.sety(kepala.ycor()-20)
    
    
    if kepala.ycor()<=ground_y+30:
        kepala.sety(ground_y+30)
        badan.sety(ground_y+10)
        kepala.velocity_y=0
        kepala.on_ground=True       
        
        
    #jika ada colision
    if obstacle.distance(kepala) <30 or obstacle.distance(badan) <30:
        time.sleep(0.5)
        obstacle.setx(700)
        height=random.randint(40,100)
        obstacle.shapesize(stretch_wid=height/20,stretch_len=1)
        obstacle.sety(ground_y+height/2)
        
        kepala.goto(-250, ground_y + 30)
        badan.goto(-250, ground_y + 10)
        kepala.velocity_y = 0
        kepala.on_ground = True
        score=0
        pen.clear()    
        pen.write("Score:{} High Score:{}".format(score,high_score),align="center",font=("courier",30,"normal"))
        
      











