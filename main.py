import turtle
turtle.speed(10)


def square(x, y, a, angle, color):
    '''
    Function, drawing square.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a square
    :param angle: rotation angle of a square
    :param color: color of a square
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.setheading(angle)
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

def main():
    '''
    Main function.
    :return: None
    '''
    square(20, -20, 180, 30, 'blue')
    turtle.done()


if __name__ == '__main__':
    main()