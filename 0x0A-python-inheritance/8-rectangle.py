#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        try:
            self.integer_validator("width", width)
        except Exception as e:raise
        else:
            self.__width = width

        try:
            self.integer_validator("height", height)
        except Exception as e: raise
        else:
            self.__height = height
