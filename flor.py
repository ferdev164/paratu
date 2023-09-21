from turtle import *
import turtle as tur

tur = tur.Turtle()

tur.penup()
tur.left(90)
tur.fd(200)
tur.pendown()
tur.right(90)

# Cambiar el color de la flor a amarillo
tur.fillcolor("yellow")  # Cambia el color de relleno de la flor
tur.begin_fill()
tur.circle(10, 180)
tur.circle(25, 110)
tur.left(50)
tur.circle(60, 45)
tur.circle(20, 170)
tur.right(24)
tur.fd(30)
tur.left(10)
tur.circle(30, 110)
tur.fd(20)
tur.left(40)
tur.circle(90, 70)
tur.circle(30, 150)
tur.right(30)
tur.fd(15)
tur.circle(80, 90)
tur.left(15)
tur.fd(45)
tur.right(165)
tur.fd(20)
tur.left(155)
tur.circle(150, 80)
tur.left(50)
tur.circle(150, 90)
tur.end_fill()

tur.left(150)
tur.circle(-90, 70)
tur.left(20)
tur.circle(75, 105)
tur.setheading(60)
tur.circle(80, 98)
tur.circle(-90, 40)

tur.left(180)
tur.circle(90, 40)
tur.circle(-80, 98)
tur.setheading(-83)

tur.fd(30)
tur.left(90)
tur.fd(25)
tur.left(45)

# Cambiar el color de las hojas a verde
tur.fillcolor("dark green")  # Cambia el color de relleno de las hojas
tur.begin_fill()
tur.circle(-80, 90)
tur.right(90)
tur.circle(-80, 90)
tur.end_fill()

tur.right(135)
tur.fd(60)
tur.left(180)
tur.fd(85)
tur.left(90)
tur.fd(80)

tur.right(90)
tur.right(45)

# Cambiar el color de las hojas a verde
tur.fillcolor("dark green")  # Cambia el color de relleno de las hojas
tur.begin_fill()
tur.circle(80, 90)
tur.left(90)
tur.circle(80, 90)
tur.end_fill()

tur.left(135)
tur.fd(60)
tur.left(180)
tur.fd(60)
tur.right(90)
tur.circle(200, 60)

# Agregar texto animado
tur.penup()
tur.goto(0, -250)  # Posición del texto
tur.pendown()
tur.color("blue")  # Color del texto

# Puedes cambiar el mensaje que se muestra
tur.write("para ti :v", align="center", font=("Arial", 16, "bold"))

# Esperar a que el usuario haga clic antes de cerrar la ventana
tur.screen.mainloop()