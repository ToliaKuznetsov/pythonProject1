import turtle


def square(x, y, a, angle, color):
    '''
    Function, drawing square.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a square
    :param angle: rotation angle of a square (counterclockwise)
    :param color: color of a square
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
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

def main():
    '''
    Main function.
    :return: None
    '''
    turtle.done()


if __name__ == '__main__':
    main()