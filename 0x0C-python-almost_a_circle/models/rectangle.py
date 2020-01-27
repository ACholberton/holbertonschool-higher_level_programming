#!/usr/bin/python3


from models.base import Base
"""Rectangle class"""


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    """width getter"""
    def width(self):
        return self.__width

    @width.setter
    """width setter"""
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    """height getter"""
    def height(self):
        return self.__height

    @height.setter
    """height setter"""
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    """x getter"""
    def x(self):
        return self.__x

    @x.setter
    """x setter"""
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    """y getter"""
    def y(self):
        return self.__y

    @y.setter
    """y setter"""
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area Method"""
        return self.__height * self.__width

    def display(self):
        """display method"""
        for a in range(self.__y):
            print()
        for b in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """STR method"""
        rec = "[Rectangle] ({}) {}/{} - {}/{}"
        return rec.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """ Update method"""
        arg_len = len(args)
        if arg_len >= 1:
            self.id = args[0]
        if arg_len >= 2:
            self.width = args[1]
        if arg_len >= 3:
            self.height = args[2]
        if arg_len >= 4:
            self.x = args[3]
        if arg_len >= 5:
            self.y = args[4]
