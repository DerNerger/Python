from math import sqrt

class Point(object):
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def norm(self):
        return sqrt(self*self)
