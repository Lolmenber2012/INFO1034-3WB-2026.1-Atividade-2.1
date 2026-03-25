from turtle import * 

t = Turtle() 

def desenha_quadrado(x, y, tamanho, color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill() 
    t.fillcolor(color)
    for _ in range(4):
        t.fd(tamanho) 
        t.rt(90)
    t.end_fill()

desenha_quadrado(-200, -300, 1000, 'blue')

desenha_quadrado(-150, 200, 300, 'green')







































































mainloop() 