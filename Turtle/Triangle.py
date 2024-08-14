import turtle

wn = turtle.Screen()
wn.bgcolor("Black")


t = turtle.Turtle()
t.shape("turtle")
t.color("red","blue")

t.speed(0)
t.fillcolor("yellow")
#triangle
t.left(60)
t.forward(350)
t.right(120)
t.forward(350)
t.right(120)
t.forward(350)
t.backward(350)
t.left(60)
t.forward(350)
t.right(120)
t.forward(350)

wn.mainloop()