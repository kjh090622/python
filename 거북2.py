from turtle import *
color("red","yellow")
begin_fill()
speed(-1)
pensize(5)
while True:
    forward(200)
    left(170)
    if abs(pos())<2:
        break

end_fill()
done()
