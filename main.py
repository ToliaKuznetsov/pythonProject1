# Case-study #1
# Developers:   Ivanov A. (20%),
#               Petrova S. (60%),
#               Sidorov M. (30%)
import turtle
def square(x, y, a, ang, c):

    """
    Function, drawing square.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: short-side length of a triangle
    :param b: long-side lenght of a triangle
    :param ang: rotation angle of a triangle
    :param c: color of a triangle
    :return: None
    """

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




def main():
    '''
    Main function.
    :return: None
    '''
triangle(100, 100, 90,0, "red" )
turtle.mainloop()

if __name__ == '__main__':
    main()