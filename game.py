import turtle,random,time
#-setting background
wn=turtle.Screen()
wn.title('Flappy_Bird by sudarshan')
wn.bgcolor('AQUA')
wn.setup(width=1024,height=500)
wn.tracer(0)
#----
pen=turtle.Turtle()
pen.color('MAROON')
pen.penup()
pen.hideturtle()
pen.goto(50,300)
score = 0
high_score = score
pen.write("Score: {} High Score: {}".format(score,high_score),align='left',font=('Courier',30,'normal'))
##
#####-creating bird object
bird=turtle.Turtle()
bird.color('red')
bird.shape('circle')
bird.shapesize(2,2)
bird.penup()
bird.goto(-450,0)
bird.direction='down'
##
#pipes
upper_pipe,bottom_pipe=turtle.Turtle(),turtle.Turtle()
upper_pipe.color('black'),bottom_pipe.color('black')
upper_pipe.shape('square')
bottom_pipe.shape('square')
upper_pipe.shapesize(17,4)
bottom_pipe.shapesize(12,4)
upper_pipe.penup()
bottom_pipe.penup()
upper_pipe.goto(280,270)
bottom_pipe.goto(280,-270)
#####
upper1_pipe,bottom1_pipe = turtle.Turtle(),turtle.Turtle()
upper1_pipe.color('black'),bottom1_pipe.color('black')
upper1_pipe.shape('square')
bottom1_pipe.shape('square')

upper1_pipe.shapesize(30,4)
bottom1_pipe.shapesize(5,4)
upper1_pipe.penup()
bottom1_pipe.penup()
upper1_pipe.goto(upper_pipe.xcor()+300,250)
bottom1_pipe.goto(bottom_pipe.xcor()+300,-350)

def go_up():
    bird.direction='up'

def move():
    if bird.direction == 'up':
        y=bird.ycor()
        bird.sety(y + 27)

    if bird.direction =='down':
        y=bird.ycor()
        bird.sety(y-4.6)

def collison():
    width,height,ro=upper_pipe.shapesize()
    #collison at front face
    if (bird.ycor()-(4*10)>=upper_pipe.ycor()-(width*10)) and abs(upper_pipe.xcor()-bird.xcor())<=(4*10) :
        return True
    width,height,ro=upper1_pipe.shapesize()
    if (bird.ycor()-(4*10)>=upper1_pipe.ycor()-(width*10)) and abs(upper1_pipe.xcor()-bird.xcor())<=(4*10):
        return True
    width,height,ro=bottom_pipe.shapesize()
    if (bird.ycor()-(4*10)<=bottom_pipe.ycor()+(width*10)) and abs(bottom_pipe.xcor()-bird.xcor())<=(4*10):
        return True
    width,height,ro=bottom1_pipe.shapesize()
    if (bird.ycor()-(4*10)<=bottom1_pipe.ycor()+(width*10)) and abs(bottom1_pipe.xcor()-bird.xcor())<=(4*10):
        return True
    return False

wn.listen()
wn.onkeypress(go_up,'w')
delay=0.04
curr_speed=10
while True:
    wn.update()
    time.sleep(delay)
    move()
    if delay<0.023:
        delay=0.018
        upper_pipe.setx(upper_pipe.xcor()-curr_speed)
        bottom_pipe.setx(bottom_pipe.xcor()-curr_speed)
        upper1_pipe.setx(upper1_pipe.xcor()-curr_speed)
        bottom1_pipe.setx(bottom1_pipe.xcor()-curr_speed)
    if collison():
        score=0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score),align='left',font=('Courier',30,'normal'))
        time.sleep(0.3)
        bird.goto(-450,0)
        bird.direction='down'
        upper_pipe.goto(280,250)
        bottom_pipe.goto(280,-250)  
        upper_pipe.shapesize(19,4)
        bottom_pipe.shapesize(14,4)
        upper1_pipe.goto(upper_pipe.xcor()+300,250)
        bottom1_pipe.goto(bottom_pipe.xcor()+300,-350)

    if bird.ycor()>330:
        bird.sety(bird.ycor()-5)
        bird.direction='down'

    if bird.ycor()<-350:
        bird.sety(bird.ycor())
        bird.direction='stop'
    if bird.direction=='up':
        move()
        bird.direction='down'
    if upper_pipe.xcor()<-600:
        x=random.randrange(10,20)
        upper_pipe.goto(500,350)
        bottom_pipe.goto(500,-230)
        height,width=random.randrange(25,30),random.randrange(2,5)
        upper_pipe.shapesize(height-x,width)
        bottom_pipe.shapesize(height,width)

    if upper1_pipe.xcor()<-600:
        x=random.randrange(10,15)
        height,width=random.randrange(22,25),random.randrange(2,5)
        upper1_pipe.shapesize(height,width)
        bottom1_pipe.shapesize(height-x,width)
        upper1_pipe.goto(upper_pipe.xcor()+random.randrange(400,700),300)
        bottom1_pipe.goto(upper1_pipe.xcor(),-250)

    width,height,ro=upper_pipe.shapesize()
    if bird.xcor()+4*10==upper_pipe.xcor()+height*10:
        score+=10
    if score>high_score:
        high_score=score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score),align='left',font=('Courier',30,'normal'))

    width,height,ro=upper1_pipe.shapesize()
    if bird.xcor()+4*10==upper1_pipe.xcor()+height*10:
        score+=10
    if score>high_score:
        high_score=score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score),align='left',font=('Courier',30,'normal'))
    if score%50==0:
        delay-=0.001
wn.mainloop()
