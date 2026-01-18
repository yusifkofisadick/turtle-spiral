from turtle import *

for steps in range(1_000):
    for c in ('blue', 'red', 'green'):
        color(c)
        forward(steps)
        right(30)