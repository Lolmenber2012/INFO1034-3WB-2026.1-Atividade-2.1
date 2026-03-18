from turtle import *



t = Turtle()


#Desenhando um Quadrado

for _ in range(4):
    t.forward

t.pu()
t.goto(100,200)
t.pd()

#Da para fazer mais rápido?
t.color('#3c17e3')
t.begin_fill()
t.fillcolor('red')
for _ in range(4):
    t.fd(100)
    t.lt(90) 
t.end_fill()

# Começo do Plano Cartesiano
t.color('red')
t.pu()
t.goto(0,0)
t.pd()

t.fd(400)
t.stamp()

t.pu()
t.goto(-300,0)
t.pd()

t.fd(200)




color = textinput('Obter cor', 'digite a cor desejada')


t.color('blue')



mainloop() 


