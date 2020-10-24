# Case-study #1
# Developers:   Ivanov A. (20%),
#               Petrova S. (60%),
#               Sidorov M. (30%)
import turtle
turtle.setup(1200, 800)
turtle.speed(20)


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
    turtle.forward(a*2**.5)
    turtle.right(135)
    turtle.end_fill()
    turtle.right(ang)


def parallelogram(x, y, a, b, r, c):
    """
    Function, drawing parallelogram.
    :param x: upper  obtuse angle coordinate x
    :param y: upper obtuse angle coordinate y
    :param a: long side of the parallelogram
    :param b: short side of the parallelogram
    :param r: degree of rotation relative OX
    :param c: color
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

def hui():
    """
    Function, drawing rabbit.
    Tolian
    :return: None
    """
    square(400, 300, 50, 67.5, '#FF9A5E')
    triangle(402,218,80,90,'#FFFF00')
    triangle(318, 298, 80, 360, '#FF0000')
    parallelogram(398, 166, 70, 50, 225, '#9CBF4E')
    triangle(472, 148, 70, 180, '#00B2EE')
    triangle(376, 138, 40, 270, '#912CEE')
    triangle(452, 144, 40, 0, '#7D26CD')

def hai():
    """
    Function, drawing rabbit.
    Tolian
    :return: None
    """
    square(400, -100, 50, 67.5, '#FF9A5E')
    triangle(380, -189, 85, 90, '#FF0000')
    parallelogram(376, -148, 58, 44, 225, '#9CBF4E')
    triangle(406, -169, 85, 270, '#FFFF00')
    triangle(410, -220, 60, 315, '#00B2EE')
    triangle(406, -340, 44, 135, '#9B30FF')
    triangle(282, -288, 44, 90, '#912CEE')
def main():
    """
    Main function.
    :return: None
    """
    hui()
    hai()
    turtle.done()

if __name__ == '__main__':
    main()