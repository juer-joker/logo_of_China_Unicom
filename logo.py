import turtle
import time


turtle.screensize(600, 800)

turtle.pensize(14)
turtle.pencolor("red")
turtle.speed(5)

f_d = 150
x = -2**(1/2)
r = 25
turtle.hideturtle()
turtle.penup()
turtle.goto(x*37.5, -x*25)
turtle.left(135)
turtle.pendown()
turtle.circle(r, 270)
turtle.forward(f_d)
turtle.circle(-r, 180)
turtle.forward(f_d)
turtle.circle(r, 180)
turtle.forward(f_d)
turtle.circle(-r, 270)
turtle.forward(f_d)
turtle.circle(r, 180)
turtle.forward(f_d)
turtle.circle(-r, 180)
turtle.forward(f_d)
turtle.penup()

turtle.goto(-80, -175)
turtle.pendown()
turtle.write('中国联通', font=('华文隶书', 45, 'bold'))


time.sleep(3)
