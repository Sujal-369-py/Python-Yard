import turtle

wn = turtle.Screen()
wn.bgcolor("black")

t= turtle.Turtle()
t.color("white")
t.speed(0)

t.circle(90,steps = 9)
t.hideturtle()

wn.mainloop()