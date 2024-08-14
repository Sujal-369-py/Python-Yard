import turtle

wn = turtle.Screen()
wn.bgcolor("black")


t= turtle.Turtle()
t.color("white")
t.speed(9)

def draw_circle(x,y,color,rad):
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(rad)
    t.end_fill()
    t.up()
    t.home()


draw_circle(0,-50,"red",50)
draw_circle(0,300,"orange",25)
draw_circle(200,200,"yellow",50)
draw_circle(0,-300,"brown",25)
draw_circle(-200,200,"blue",50)
draw_circle(300,0,"dark blue",25)
draw_circle(200,-200,"purple",50)
draw_circle(-200,0,"pink",25)
draw_circle(-200,-200,"cyan",50)




wn.mainloop()