import turtle
t=turtle.Pen()
s=turtle.Screen()
t.speed(0);t.ht();s.bgcolor('black')
t.color('green')
a,b=0,0
for i in range(220):
   t.fd(a);t.rt(b)
   a+=3
   b+=1

turtle.mainloop()
