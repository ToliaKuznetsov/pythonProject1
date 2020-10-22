# Case-study #1
# Developers:   Ivanov A. (20%),
#               Petrova S. (60%),
#               Sidorov M. (30%)
import turtle
def triangle(x, y, a, ang, c):
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
turtle.forward(a)
turtle.right(90)
turtle.forward(a)
turtle.right(135)
turtle.forward(b)
turtle.right(135)


turtle.mainloop()

if __name__ == '__main__':
    main()