# Case-study #1
# Developers:   Ivanov A. (20%),
#               Petrova S. (60%),
#               Sidorov M. (30%)
import turtle
def triangle(x, y, a, b, ang, c):
   '''
    :return: Function, drawing triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: short-side length of a triangle
    :param b: long-side lenght of a triangle
    :param ang: rotation angle of a triangle
    :param c: color of a triangle
    :return: None
   '''

turtle.up()
turtle.setposition(x, y)
turtle.setheading(ang)
turtle.down()
turtle.color(c)
turtle.begin_fill()
turtle.forward(a)
turtle.right(90)
turtle.forward(a)
turtle.right(135)
turtle.forward(b)
turtle.right(135)
turtle.end_fill()
def main():
    triangle(1,2,10,20,0,"red")

turtle.mainloop()
