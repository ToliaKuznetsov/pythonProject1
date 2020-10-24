# Case-study #1
# Developers:   Lapochkin D. (0%),
#               Kuznetsov A. (0%),
#               Krivoshapova D. (0%)
import turtle

turtle.screensize(1200, 800)


def boarders():
    turtle.color('black')
    turtle.up()
    turtle.setposition(-600, 0)
    turtle.down()
    turtle.forward(1200)
    turtle.up()
    turtle.setposition(-200, -400)
    turtle.left(90)
    turtle.down()
    turtle.forward(800)
    turtle.up()
    turtle.setposition(200, -400)
    turtle.down()
    turtle.forward(800)


def square(x, y, a, angle, color):
    """
    Function, drawing square.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a square
    :param angle: rotation angle of a square (counterclockwise)
    :param color: color of a square
    :return: None
    """
    turtle.up()
    turtle.setposition(x, y)
    turtle.setheading(angle)
    turtle.left(angle)
    turtle.color(color)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()
    turtle.right(angle)


def triangle(x, y, a, ang, c):
    """
    Function, drawing triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: short-side length of a triangle
    :param ang: rotation angle of a triangle
    :param c: color of a triangle
    :return: None
    """
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
    turtle.forward(a * 2 ** .5)
    turtle.right(135)
    turtle.end_fill()
    turtle.right(ang)


def parallelogram(x, y, a, b, c, r):
    """
    Function, drawing parallelogram.
    :param x: upper  obtuse angle coordinate x
    :param y: upper obtuse angle coordinate y
    :param a: long side of the parallelogram
    :param b: short side of the parallelogram
    :param c: color
    :param r: degree of rotation relative OX
    """
    turtle.penup()
    turtle.color(c)
    turtle.setposition(x, y)
    turtle.left(r)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(45)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(45)
    turtle.end_fill()
    turtle.right(r)


def rabbit():
    """
    Function, drawing rabbit.
    TODO: Lapochkin D.
    :return: None
    """
    square(10, 260, 50, 0, '#FF9A5E')
    parallelogram(-15, 264, 70, 50, '#9CBF4E', 135)
    triangle(6, 255, 100, -90, '#FF552B')
    triangle(-94, 51, 100, 90, '#5BC78C')
    triangle(-15, 124, 75, -90, '#9CBF4E')
    triangle(39, 49, 50, 180, '#F2A0B6')
    triangle(10, 184, 50, -45, '#CCCACF')


def rooster():
    """
    Function, drawing rooster.
    TODO: Lapochkin D.
    :return:
    """
    square(35, -115, 50, 0, '#F2EC91')
    triangle(35, -111, 45, 45, '#F2785C')
    triangle(-15, -269, 100, 90, '#9FAABF')
    triangle(60, -269, 50, 135, '#F2A0B6')
    triangle(-119, -109, 100, 0, '#FF552B')
    triangle(-119, -105, 71, 45, '#D9ADC5')
    parallelogram(-95, -138, 71, 35, '#9CBF4E', -90)


def main():
    """
    Main function.
    :return: None
    """
    turtle.speed(20)
    boarders()
    rabbit()
    rooster()
    turtle.done()


if __name__ == '__main__':
    main()
