# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 17:17:47 2022

@author: Aqeel Ahmed
"""

import turtle
import math

def draw_circle(radius, x, y):    
    turtle.up()
    turtle.goto(x,y+radius) # go to (0, radius)
    turtle.begin_fill() # start fill
    turtle.down() # pen down
    turtle.color('red')
    times_y_crossed = 0
    x_sign = 1.0
    while times_y_crossed <= 10:
        turtle.forward(2*math.pi*radius/360.0) # move by 1/360
        turtle.right(1.0)
        x_sign_new = math.copysign(1, turtle.xcor())        
        if(x_sign_new != x_sign):
            times_y_crossed += 1
        x_sign = x_sign_new

    return


draw_circle(100, 10, 10)

turtle.pen(shown=False)
turtle.done()