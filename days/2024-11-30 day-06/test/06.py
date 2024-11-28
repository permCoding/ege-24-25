from turtle import *

tracer(0)

step = 50
for i in range(3):
    right(60)
    forward(7*step)
    right(60)

up()
for x in range(-10, +10):
    for y in range(-10, +10):
        goto(x*step, y*step)
        dot(5, 'red')

done()
