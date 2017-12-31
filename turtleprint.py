import turtle
t = turtle.Turtle()

def square():
    x=80
    y=90
    t.forward(x)
    t.left(y)
    t.forward(x+40)
    t.left(y)
    t.forward(x)
    t.left(y)
    t.forward(x+40)
    t.left(y)
square()

x=200
y=90
t.forward(x)
t.left(y)
t.forward(x-80)
t.left(y)
t.forward(x)
t.right(y)
t.right(y-60)

x=80
y=120
t.forward(x)
t.right(y)
t.forward(x)

y=60
t.left(y)
x=120
t.forward(x)
t.left(x)

x=80
t.forward(x)
t.left(y)
t.forward(x+40)























