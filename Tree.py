import turtle
from random import randint

# screen settings
WIDTH, HEIGHT = 1300, 700
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(3 * WIDTH, 3 * HEIGHT)
screen.bgcolor("black")
screen.delay(0)
# turtle settings
trl = turtle.Turtle()
trl.pensize(1)
trl.speed(0)
turtle.tracer(0)
trl.setpos(0, -HEIGHT // 2)
trl.color("green")
# L-System settings
itr = 9
axiom = "X"
Axm = ""
rules = {"X": "F[@[-X]+X]", "F": "F", "+": "+", "-": "-", "[": "[", "]": "]", "@": "@"}
angle = lambda: randint(0, 45)
step = 80
stack = []
size = 20
color = [0.27, 0, 0]

for i in range(itr):
    for ch in axiom:
        Axm += rules[ch]

    axiom = Axm
    Axm = ""

trl.left(90)
trl.pensize(size)
for ch in axiom:
    trl.color(color)
    if ch == "+":
        trl.right(angle())
    elif ch == "-":
        trl.left(angle())
    elif ch == "[":
        ang, pos = trl.heading(), trl.pos()
        stack.append((ang, pos, size, step, color[1]))
    elif ch == "]":
        ang, pos, size, step, color[1] = stack.pop()
        trl.setheading(ang)
        trl.penup()
        trl.goto(pos)
        trl.pendown()
        trl.pensize(size)
    elif ch == "@":
        color[1] += 0.04
        step -= 6
        size -= 2
        size = max(1, size)
        trl.pensize(size)
    else:
        trl.forward(step)


turtle.update()
turtle.done()
