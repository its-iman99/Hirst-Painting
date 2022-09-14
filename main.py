import turtle
# import colorgram

turtle.colormode(255)
timmy = turtle.Turtle()

# colors = colorgram.extract('image.jpg', 30)
#
# color_list = []
#
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     tup = (r, g, b)
#     color_list.append(tup)

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157),
              (215, 74, 12), (15, 154, 16), (199, 14, 10), (243, 33, 165), (229, 17, 121), (73, 9, 31),
              (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239),
              (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]


def hirst_paint():
    color_index = 0
    for _ in range(10):
        for i in range(10):
            timmy.pendown()
            timmy.dot(20, color_list[color_index])
            color_index += 1
            if color_index == len(color_list):
                color_index = 0
            timmy.penup()
            timmy.forward(50)
        timmy.left(90)
        timmy.forward(50)
        timmy.right(90)
        timmy.backward(50 * 10)
    # timmy.hideturtle()


timmy.hideturtle()
timmy.penup()
timmy.setx(-200)
timmy.sety(-200)
timmy.pendown()
hirst_paint()

screen = turtle.Screen()
screen.exitonclick()
