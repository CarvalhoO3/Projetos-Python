import turtle
import colorsys


def setup_turtle():
    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    return t


def draw_spiral(t, num_colors, start_radius, increment, angle):
    for i in range(360):
        color = colorsys.hsv_to_rgb(i / num_colors, 1.0, 1.0)
        t.color(color)
        t.forward(start_radius + i * increment / num_colors)
        t.left(angle)


def draw_art():
    t = setup_turtle()
    num_colors = 36
    angle = 59
    start_radius = 5
    increment = 3
    draw_spiral(t, num_colors, start_radius, increment, angle)
    t.right(120)
    draw_spiral(t, num_colors, start_radius, increment, angle)
    t.right(120)
    draw_spiral(t, num_colors, start_radius, increment, angle)

    t.penup()
    t.goto(0, -200)
    t.pendown()

    draw_spiral(t, num_colors, start_radius, increment * 2, angle)
    t.right(120)
    draw_spiral(t, num_colors, start_radius, increment * 2, angle)
    t.right(120)
    draw_spiral(t, num_colors, start_radius, increment * 2, angle)

    t.penup()
    t.goto(0, 200)
    t.pendown()

    draw_spiral(t, num_colors, start_radius, increment * 1.5, angle)
    t.right(120)
    draw_spiral(t, num_colors, start_radius, increment * 1.5, angle)
    t.right(120)
    draw_spiral(t, num_colors, start_radius, increment * 1.5, angle)

    turtle.done()


draw_art()
