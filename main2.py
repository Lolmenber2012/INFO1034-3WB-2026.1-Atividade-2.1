from turtle import * 
 
t = Turtle()

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

t.pu()
t.goto(200,200)
t.pd()
t.begin_fill()
t.fillcolor('red')
t.fd(100)
t.lt(90)
t.fd(50)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(50)
t.end_fill()












































mainloop()
