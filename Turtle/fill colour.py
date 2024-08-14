import turtle


wn = turtle.Screen()
wn.bgcolor("Black")


t = turtle.Turtle()
t.shape("turtle")
t.color("red","orange")
t.begin_fill()
t.fillcolor("purple")
for i in range (4):
    t.speed(0)
    t.fd(250)
    t.left(90)
t.hideturtle()
t.end_fill()


wn.mainloop()