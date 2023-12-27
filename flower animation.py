from turtle import *
title("Flower Pattern")
bgcolor('black')
speed(0)
col=['red','yellow','pink','cyan','green','blue']
for i in range(120):
    pencolor(col[i%6])
    circle(190-i/2,90)
    left(90)
    circle(190-i/3,90)
    left(60) 