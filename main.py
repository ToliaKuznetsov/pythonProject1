import turtle
turtle.speed(100000)


def square(x, y, a, c):
    '''
    Function, drawing square.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a square
    :return: None
    '''
    turtle.up()
    turtle.color(c)
    turtle.setposition(x, y)
    turtle.down()
    turtle.fill(1)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.fill(0)

def main():
    '''
    Main function.
    :return: None
    '''
    square(-200, 200, 180, 'blue')
    square(20, 200, 180, 'blue')
    square(20, -20, 180, 'blue')
    square(-200, -20, 180, 'blue')
    turtle.done()


if __name__ == '__main__':
    main()