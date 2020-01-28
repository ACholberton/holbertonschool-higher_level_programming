#!/usr/bin/python3

"""importing from base.py"""
from models.base import Base
"""Rectangle class"""


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class init"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
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

    def update(self, *args, **kwargs):
        """ Update method"""
        arg_len = len(args)
        if arg_len > 0:
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
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
