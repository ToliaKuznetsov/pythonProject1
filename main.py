import turtle


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
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(45)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(45)
    turtle.right(r)
dfghjkl
sdfghjk