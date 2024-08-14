import turtle

wn = turtle.Screen()
wn.bgcolor("black")

t = turtle.Turtle()
t.color("grey","orange")
t.speed(0)

def n_circle(x,y,rad,frd) :
    t.up()
    t.goto(x,y)
    t.down()
    t.circle(rad)
    t.up()
    t.home()
    t.forward(frd)


n_circle(0,-100,90,200)
n_circle(100,-100,90,200)
n_circle(200,-100,90,200)
n_circle(300,-100,90,200)
n_circle(400,-100,90,200)
t.bk(900)
n_circle(-600,-100,60,200)
n_circle(-480,-100,60,200)
n_circle(-360,-100,60,200)
n_circle(-240,-100,60,200)








wn.mainloop()