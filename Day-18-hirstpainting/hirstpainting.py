import colorgram

import turtle as t
from random import choice

my_turtle = t.Turtle()
# my_turtle.shape("turtle")
my_turtle.color("red")


# colors = colorgram.extract('Day-18-hirstpainting/image.jpg',30)
t.colormode(255)
# rgb_color = []

# for col in colors:
#     r = col.rgb.r
#     g = col.rgb.g
#     b = col.rgb.b
#     new_color = (r,g,b)
#     rgb_color.append(new_color)
#     my_turtle.color(r,g,b)
# print(rgb_color)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

my_turtle.hideturtle()
my_turtle.speed("fastest")

my_turtle.penup()
def draw_dot(x,y):
    for _ in range(10):
        ran_color = choice(color_list)  
        my_turtle.setpos(x,y)
        my_turtle.dot(20,ran_color)
        x = x+50
for i in range(10):
    y = -200
    y = y + i*50
    draw_dot(-250,y)
screen = t.Screen()
screen.exitonclick()