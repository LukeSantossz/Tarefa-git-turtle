import turtle

# Configuração da tela
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("light blue")

# Desenhar a casa
pen = turtle.Turtle()
pen.penup()
pen.goto(-100, -100)
pen.pendown()
pen.color("yellow")
pen.begin_fill()
for _ in range(4):
    pen.forward(200)
    pen.left(90)
pen.end_fill()

# Desenhar o telhado
pen.penup()
pen.goto(-120, 100)
pen.pendown()
pen.color("red")
pen.begin_fill()
pen.goto(110, 100)
pen.goto(-20, 180)
pen.goto(-120, 100)
pen.end_fill()

# Desenhar a porta
pen.penup()
pen.goto(-30, -100)
pen.pendown()
pen.color("brown")
pen.begin_fill()
for _ in range(2):
    pen.forward(60)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
pen.end_fill()

# Desenhar a janela
pen.penup()
pen.goto(20, 0)
pen.pendown()
pen.color("blue")
pen.begin_fill()
for _ in range(4):
    pen.forward(60)
    pen.left(90)
pen.end_fill()

# Esconder a caneta
pen.hideturtle()

# Manter a janela aberta
screen.mainloop()