import turtle

wn = turtle.Screen()
wn.bgcolor("black")

t = turtle.Turtle()
t.color("brown")
t.speed(0)


for i in range(1,1000,100):
    t.circle(90+i)

for i in range(1,1000,100):
    t.circle(-90-i)
t.hideturtle()

wn.mainloop()