from turtle import *

tracer(0)
st = 40

for _ in range(42):
    rt(60)
    fd(7 * st)
    rt(60)

up()
for x in range(-10, +10):
    for y in range(-10, +10):
        goto(x*st, y*st)
        dot(6, 'red')

done()
