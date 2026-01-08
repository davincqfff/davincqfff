#shidqi noor faadhil
#project snake games

import turtle
import time
import random
delay=0.1
#skor
score=0
high_score=0


#make the screen
wn=turtle.Screen()
wn.title("Permainan ular@iqkfff ")
wn.bgcolor("pink")
wn.setup(width=600,height=600)
wn.tracer(0)

#kepala ular
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction="stop"
#makanan
food=turtle.Turtle()
food.speed(0)
food.shape("triangle")
food.color("yellow")
food.penup()
food.goto(0,100)

segmen=[]
#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,-260)
pen.write ("Score: 0 High Score: 0",align="center",font=("courier",24,"normal"))
#fungsi
def go_up():
    if head.direction !="down":
        head.direction="up"
def go_down():
    if head.direction !="up":
        head.direction="down"
def go_right():
     if head.direction !="left" :  
        head.direction="right"
def go_left():
     if head.direction !="right":  
        head.direction="left"


def move ():
    if head.direction== "up":
        y=head.ycor()
        head.sety(y+20)
    
    if head.direction== "down":
        y=head.ycor()
        head.sety(y-20)
    
    if head.direction== "right":
        x=head.xcor()
        head.setx(x+20)
    
    if head.direction== "left":
        x=head.xcor()
        head.setx(x-20)
    
#keybind
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d") 
#main game loop 
while True:
    wn.update() 
    
    
    
    #cek collision
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        
        #hide segmen
        for segment in segmen:
            segment.goto(1000,1000)
            
         #clear segmen 
        segmen.clear()
        #reset score
        score=0
        #update score
        pen.clear()    
        pen.write("Score:{} High Score:{}".format(score,high_score),align="center",font=("courier",24,"normal")),
    
    
    
    
    #cek makanan
    if head.distance(food)<20:#keterangan jika kepala mengenai makanan
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        #delay
        delay-=0.001
        
        #nambah badan
        new_segmen=turtle.Turtle()
        new_segmen.speed(0)
        new_segmen.shape("square")
        new_segmen.color("brown")
        new_segmen.penup()
        segmen.append(new_segmen)
        
        #skor bertambah
        score+=10
        
        
        if score>high_score:
            high_score=score
        
        pen.clear()    
        pen.write("Score:{} High Score:{}".format(score,high_score),align="center",font=("courier",24,"normal")),
        
    #move the end segmen first in reverse order 
    for index in range (len(segmen)-1,0,-1) :
        x=segmen[index-1].xcor()
        y=segmen[index-1].ycor()
        segmen[index].goto(x,y)  
    #move segmen 0 where head is
    if len(segmen)>0:
        x=head.xcor()
        y=head.ycor()
        segmen[0].goto(x,y)
        
    move()
    for segment in segmen:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            
             #hide segmen
            for segment in segmen:
                segment.goto(1000,1000)
             
            #clear segmen 
            segmen.clear()
             #reset score
            score=0
            #reset delay
            delay=0.1
            pen.clear()    
            pen.write("Score:{} High Score:{}".format(score,high_score),align="center",font=("courier",24,"normal")),

    
    
    
    
    
    
    
    time.sleep(delay)


wn.mainloop()