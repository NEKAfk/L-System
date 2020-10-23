import turtle

turtle.hideturtle()
turtle.tracer(0)
turtle.penup()
turtle.setposition(0, -200)
turtle.pendown()
turtle.pensize(3)

axiom = "FX"
tempAx = ""

translate = {"X":"X+YF+", "Y":"-FX-Y", "F":"F", "+":"+", "-":"-"}
l = 2
ang = 90
for k in range(15):
    for ch in axiom:
            tempAx += translate[ch]

    axiom = tempAx
    tempAx = ""

for ch in axiom:
    if ch == "+":
        turtle.right(ang)
    elif ch == "-":
        turtle.left(ang)
    elif ch == "F":
        turtle.forward(l)

turtle.update()
turtle.done()
