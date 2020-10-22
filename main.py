import turtle

def triangle(x, y, a, b, ang, c):
    '''
    Function, drawing square.
    :return: Function, drawing triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a square
    :param angle: rotation angle of a square (counterclockwise)
    :param color: color of a square
    :param a: short-side length of a triangle
    :param b: long-side lenght of a triangle
    :param ang: rotation angle of a triangle
    :param c: color of a triangle
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.left(angle)
    turtle.color(color)
    turtle.setheading(ang)
    turtle.down()
    turtle.color(c)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(135)
    turtle.end_fill()
    turtle.right(angle)


def main():
    '''
    Main function.
    :return: None
    '''
    turtle.done()

    triangle(0, 0, 80, 80, 45, 'red')


if __name__ == '__main__':
    main()