# import colorgram
import turtle as t
from random import choice

# colors = colorgram.extract('spot_image.jpg', 100)
tim = t.Turtle()
t.colormode(255)

rgb_colors = [ (108, 110, 127), (213, 154, 94), (140, 141, 152), (227, 214, 104), (
    195, 60, 24), (181, 159, 38), (99, 108, 176), (211, 145, 178), (200, 17, 5),
    (24, 23, 69), (25, 43, 24), (34, 37, 15), (227, 167, 198), (220, 82, 55), (42, 43, 108), (194, 9, 16),
    (230, 174, 163), (156, 168, 159), (220, 72, 97), (135, 74, 88), (182, 184, 214), (84, 99, 87), (222, 207, 21),
    (40, 23, 43), (73, 72, 36), (51, 72, 55), (183, 199, 185), (115, 135, 123), (117, 132, 135), (184, 194, 197),
    (49, 71, 73)]
x , y = -200, -200
tim.penup()
for _ in range(10):
    for _ in range(10):
        tim.goto(x, y)
        tim.pendown()
        tim.dot(20, choice(rgb_colors))
        tim.penup()
        # tim.forward(40)
        x += 40
    y += 40
    x = -200
    tim.goto(x, y)








# for color in colors:
#     c = color.rgb
#     rgb_colors.append((c[0], c[1], c[2]))
#
#
# print(rgb_colors)





#
# tim.shape("turtle")
# tim.color("red")
#
#
# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     rgb = (r, g, b)
#     return rgb
# #
# # for side in range(3, 11):
# #     turn_angle = 360 / side
# #     tim.color(choice(colors))
# #     for _ in range(side):
# #         tim.forward(100)
# #         tim.right(turn_angle)
#
#
# distance = 20
# # tim.pensize(10)
# tim.speed("fastest")
# # for _ in range(200):
# # while True:
# #     angle = choice([90, 180, 270, 360])
# #     tim.color(random_color())
# #     tim.forward(distance)
# #     tim.setheading(angle)
#
# tilt = 0
# while tilt < 360:
#     tim.color(random_color())
#     tim.circle(100)
#     tilt = tim.heading() + 2.0
#     tim.setheading(tilt)
#     tilt += 1
#
screen = t.Screen()
screen.exitonclick()


