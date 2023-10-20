from turtle import *

pensize(2)
speed(4)
bgcolor("black")

renkler = ["pink","orange","yellow","blue","purple"]

x = [0,-100,100,-100,-50]
y = [200,-100,-100,100,-375]

sayac = 0

for i in range(len(renkler)):
    color(renkler[i])

    for a in range(36):
        forward(100)
        backward(100)
        left(10)
    if i >= 1:
        goto(x[i],y[i])
    sayac += 1
    if sayac == 1:
        setpos(100, 100)

goto(-50,-370)
color("white")
write("@klc.bll0", font=("Verdana", 17,"bold"))

exitonclick()
done()
