import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("black")
window.title("Turtle Graphics Example")

# Create a turtle named alex
alex = turtle.Turtle()
alex.shape("turtle")
alex.color("blue")
alex.speed(2)

# Draw a square
for _ in range(4):
    alex.forward(100)
    alex.right(90)

# Close the window when clicked
window.mainloop()
