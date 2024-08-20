import turtle

# Set Up Turtle
t = turtle.Turtle()

#Set Up Screen
s = turtle.Screen()
s.title("Heart")
s.delay(5)
s.bgcolor("black")

# Draw Shape
t.fillcolor("red")
t.pencolor("red")
t.begin_fill()
t.left(140)
t.forward(113)

for i in range(200):
    t.right(1)
    t.forward(1)
t.left(120)

for i in range(200):
    t.right(1)
    t.forward(1)
t.forward(112)

t.end_fill()
t.ht()

# Exit on Click
s.exitonclick()