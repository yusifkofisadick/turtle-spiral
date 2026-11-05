from turtle import *

for steps in range(1_000):
    for line in ('blue', 'red', 'green'):
        color(line)
        forward(steps)
        right(30)
