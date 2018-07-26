"""
 Points and rectangles

Write Python code that defines the following two classes:

    Point2D
        Has an initializer function that receives coordinates x and y as parameters and stores them into the object.
            Use mangled attribute names __x and __y.
            Define both parameters x and y to have default value 0.
        Has getter functions for x and y.
            Define these using the @propery decorator.
        Does not have a setter function for x or y.
        Has a string-transformation function that returns a string of form "Point2D(x=x, y=y)", where the right-side parts x and y are the actual numeric coordinate values shown with 1 decimal precision (e.g. use string formatting).
    Rectangle
        Has an initializer function that receives two points p1 and p2 as parameters. These are assumed to be Point2D-objects
            The points p1 and p2 are assumed to define a rectangle: they are the coordinates of two opposite corners.
            Define the parameters to have default values Point2D().
            The initializer stores the lower-left corner ll and upper-right corner ur as two Point2D-objects, using mangled names __ll and __ur, respectively.
                The parameters p1 and p2 do not necessarily have direct correspondence to ll and ur: they might e.g. be in any order and/or represent the upper-left and lower-right corners. Therefore you need to calculate ll and ur: ll has the smallest x and the smallest y in points p1 and p2 (hence being lower-left corner), and ur in similar manner the largest x and y.
        Has getter functions for ll and rr, defined using the @property decorator.
        Does not have a setter function for ll or ur.
        Has a string-transformation function that returns a string of form "Rectangle(ll=ll, ur=ur)", where the right-side parts ll and ur are the string-representations of the Point2D-objects for the lower-left and upper-rigth corners.
            When constructing the returned string, apply the str string-tranformation function to the Point2D-objects that represent ll and ur.

WETO's first test uses essentially the following test code (where WETO has saved your code into a file named rectangles.py):
"""


class Point2D:
    def __init__(self, x=0, y=0):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return(self.__x)

    @property
    def y(self):
        return(self.__y)

    def __str__(self):
        return("Point2D(x={0:.1f}, y={1:.1f})".format(self.__x, self.__y))


class Rectangle:
    def __init__(self, p1=Point2D(), p2=Point2D()):
        self.__ll = Point2D(p1.x if p1.x < p2.x else p2.x,
                            p1.y if p1.y < p2.y else p2.y)
        self.__ur = Point2D(p1.x if p1.x > p2.x else p2.x,
                            p1.y if p1.y > p2.y else p2.y)

    @property
    def ll(self):
        return(self.__ll)

    @property
    def ur(self):
        return(self.__ur)
        # they are the coordinates of two opposite corners.

    def __str__(self):
        return("Rectangle(ll={ll}, ur={ur})".format(ll=str(self.__ll), ur=str(self.__ur)))

if __name__=="__main__":
    print(Point2D(), end="\n\n")
    p = Point2D(-2, 5)
    print(type(p), p.x, p.y)
    print(p)
    print(p.__dict__, end="\n\n")
    r = Rectangle(p)
    print(type(r), r.ll, r.ur)
    print(r)
    print("ll" in r.__dict__, "ur" in r.__dict__, end="\n\n")
    try:
        p.x = p.y = 0
    except AttributeError:
        print("Changing x or y of Point2D p not allowed!")
    try:
        r.ll = r.ur = Point2D()
    except AttributeError:
        print("Changing ll or ur of Rectangle r not allowed!")
    print(r)
    Point2D.__str__ = lambda x: "UNDEFINED"
    print(r)