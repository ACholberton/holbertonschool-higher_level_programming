#!usr/bin/python3
"""Class Square"""

from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Class initiator"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overloading the STR method"""
        return "[square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
    @property
    def size(self):
        """seize method"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value
