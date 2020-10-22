# Case-study #1
# Developers:   Ivanov A. (20%),
#               Petrova S. (60%),
#               Sidorov M. (30%)
import turtle

def triangle(x, y, a, b, ang, c):
    '''
    Function, drawing triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a:long side length of a triangle
    :param b:short side length of a triangle
    :param ang: angle of a triangle
    :param c: color of a triangle
    :return: None
    '''
turtle.up()
turtle.setposition(x, y, ang)
turtle.down()
turtle
turtle.forward(b)
turtle.right(90)
turtle.forward(b)
turtle.right()
turtle.forward(a)
turtle.right(120)




def main():
    '''
    Main function.
    :return: None
    '''
triangle(100, 100, 90)
turtle.mainloop()

if __name__ == '__main__':
    main()