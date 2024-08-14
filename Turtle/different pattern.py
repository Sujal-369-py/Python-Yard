import turtle

wn = turtle.Screen()
wn.bgcolor("black")


t= turtle.Turtle()
t.color("white")
t.speed(9)

# 1st
t.up()
t.goto(0,-50)
t.down()
t.begin_fill()
t.fillcolor("green")
t.circle(50)
t.end_fill()
t.up()
t.home()

# 2nd
t.goto(200,200)
t.begin_fill()
t.fillcolor("orange")
t.circle(50)
t.end_fill()
t.home()


t.goto(-200,200)
t.begin_fill()
t.fillcolor("blue")
t.circle(50)
t.end_fill()
t.home()

t.goto(200,-200)
t.begin_fill()
t.fillcolor("yellow")
t.circle(-50)
t.end_fill()
t.home()

t.goto(-200,-200)
t.begin_fill()
t.fillcolor("red")
t.circle(-50)
t.end_fill()
t.home()

wn.mainloop()