from turtle import * 
from random import randint
t = Turtle()
t.hideturtle()
t.color('red')

#Plano Cartesiano

def plano_cartesiano(x, y):
    t.pu()
    t.goto(-400,0)
    t.pd() 
    t.fd(800)
    t.stamp() 
    t.pu()
    t.goto(0,-400)
    t.pd()
    t.lt(90)
    t.fd(800)
    t.stamp() 

x=randint(100,300)
y=randint(100,300)

#Retangulo

def Retangulo(x, y, tamanho1,tamanho2, colores):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.fillcolor(colores)
    for _ in range(2):
        t.fd(tamanho1)
        t.lt(90)
        t.fd(tamanho2)
        t.lt(90)
    t.end_fill()

#Triângulo
def triângulo (x, y, tamanho, colores):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(colores) 
    for _ in range(3):
        t.fd(tamanho)
        t.lt(120)
    t.end_fill()
    
#Octógono
def octógono (x, y, tamanho, colores):
    t.pu()
    t.goto(x,y)
    t.pd()

    t.begin_fill()
    t.fillcolor(colores)
    for _ in range(8):
        t.fd(tamanho)
        t.lt(45)

    t.end_fill()


 #Dodecágono
def Dodecágono (x, y, tamanho, colores):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(colores)
    for _ in range(12):
        t.fd(75)
        t.lt(30)
    t.end_fill()

#Polígono Generico
def poligono_generico(x, y, graus, tamanho, lados, colores):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(colores)
    for _ in range(lados):
        t.fd(tamanho)
        t.lt(graus)
    t.end_fill()









plano_cartesiano(x, y) 
colores = textinput('obter cor', 'digite a cor desejada')
poligono_generico(x, y, 72, 80, 5, colores) 
colores = textinput('obter cor', 'digite a cor desejada')
Retangulo(x, x, 100, 50, colores)
colores = textinput('obter cor', 'digite a cor desejada') 
triângulo(-x, y, 60, colores)
colores = textinput('obter cor', 'digite a cor desejada')
octógono(-x, -y, 100, colores)
colores = textinput('obter cor', 'digite a cor desejada')
Dodecágono(x, -y, 100, colores)





#Espiral



t.pu()
t.goto(-200,200)
t.pd()


t.color('black')
t.speed(10) 
for i in range(360):
    t.fd(i)
    t.right(30)






































mainloop()
