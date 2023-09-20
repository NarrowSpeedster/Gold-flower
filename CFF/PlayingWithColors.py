import colorsys
import turtle

t = turtle.Turtle()
s = turtle.Screen()
t.speed(0)
n = 70
h = 0
for I in range (360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h+= 1/n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range (2):
        t.left(2)
        t.circle(10)
        t.circle(20)
        t.circle(30)
        t.circle(40)
        t.circle(50)
        t.circle(60)
        t.circle(70)
        t.circle(80)
        t.circle(90)
        t.circle(100)