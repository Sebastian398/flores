from turtle import *

#Configuración inicial
header_text = "Para ti con mucho cariño"
color("white")
penup()
goto(-100, 250)
pendown()
write(header_text, align="left", font=("Lucida Calligraphy", 16, "normal"))

speed(0)
bgcolor("black")

# Dibujar el tallo verde del girasol
penup()
goto(-14, -80)
pendown()
color("green")
begin_fill()
right(90)
fd(400)
left(90)
fd(20)
left(90)
fd(400)
left(90)
fd(20)
end_fill()

# Dibujar los pétalos de la flor
penup()
goto(0, 0)
pendown()
h = 0
for i in range(16):
    for j in range(10):
        color("violet")
        h += 0.005
        right(90)
        circle(150 - j * 6, 90)
        left(90)
        circle(150 - j * 6, 90)
        right(180)
    circle(40, 24)

# Dibujar el centro de la flor
penup()
goto(-20, 0)
pendown()
color("goldenrod")
begin_fill()
circle(44)
end_fill()

done()