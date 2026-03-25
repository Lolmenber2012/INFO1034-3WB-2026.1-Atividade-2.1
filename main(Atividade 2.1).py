from turtle import * 
 
t = Turtle()


#Plano Cartesiano


t.hideturtle()
t.color('red')

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


#Retangulo


t.pu()
t.goto(300,150)
t.pd()
t.begin_fill()
t.fillcolor('orange')
t.fd(100)
t.lt(90)
t.fd(250)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(250)
t.end_fill()

color = textinput('obter cor', 'digite a cor desejada')

t.pu()
t.goto(-200,200)
t.pd()


#Triângulo


t.begin_fill()
t.fillcolor(color) 
for _ in range(3):
    t.fd(100)
    t.lt(120)
t.end_fill()

#Octógono


t.pu()
t.goto(-200,-350)
t.pd()

t.begin_fill()
t.fillcolor(color)
for _ in range(8):
    t.fd(100)
    t.lt(45)

t.end_fill()


 #Dodecágono


t.pu()
t.goto(200,-380)
t.pd()


t.begin_fill()
t.fillcolor(color)
for _ in range(12):
     t.fd(75)
     t.lt(30)
t.end_fill()

#Espiral

t.pu()
t.goto(-200,200)
t.pd()


t.color(color)
t.speed(10) 
for i in range(360):
    t.fd(i)
    t.right(30)






































mainloop()
