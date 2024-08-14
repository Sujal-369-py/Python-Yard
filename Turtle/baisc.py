import turtle

window = turtle.Screen()
tr = turtle.Turtle()
tr.shape("turtle")

tr.color("blue","orange") # first color is of line (blue = line,orange = turtle)

#clor using RBG
# tr.colormode(255)
# tr.color(244,56,78)

#this makes a rectangle
tr.forward(300)
tr.left(90)
tr.forward(300)
tr.left(90)
tr.forward(300)
tr.left(90)
tr.forward(300)


window.mainloop()
