import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("black")

# Create a turtle named t
t = turtle.Turtle()
t.speed(0)

colors = ["red", "yellow", "green", "purple", "orange","pink","blue"]

for i in range(3000):
    t.pencolor(colors[i % 7])  # Use % 5 to match the length of colors
    t.forward(i * 2)
    t.right(61)

window.mainloop()
