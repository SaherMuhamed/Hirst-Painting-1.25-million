import random
import turtle
from turtle import Turtle, Screen
import colorgram


def extracting_colors():
    """this function extract the colors from a given images."""
    rgb_colors = []
    extracted_color = colorgram.extract("image.jpg", 30)
    for color in extracted_color:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    print(rgb_colors)


color_list = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106),
              (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90),
              (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31),
              (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113),
              (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]

my_turtle = Turtle()
turtle.colormode(255)

screen = Screen()
screen.bgcolor("#FFF8F3")
screen.title("Hirst Painting $1.25 million")

# Turtle start point..
my_turtle.penup()
my_turtle.hideturtle()
my_turtle.setposition(-230, -230)


def doted_line():
    y_pos = -230
    for _ in range(10):
        for i in range(10):
            my_turtle.speed(10)
            random_color = random.choice(color_list)
            my_turtle.dot(20, random_color)
            my_turtle.forward(50)
        y_pos += 50
        my_turtle.setposition(-230, y_pos)


doted_line()

screen.exitonclick()
