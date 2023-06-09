class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        x = self.x * scalar
        y = self.y * scalar
        return Vector(x, y)
    
    def __truediv__(self, scalar):
        x = self.x / scalar
        y = self.y / scalar
        return Vector(x, y)

    def vector_dot_product(self, other):
        return self.x * other.x + self.y * other.y
    
    def vector_norm_l2(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    
class Force(Vector):
    pass


class Displacement(Vector):
    pass


class Velocity(Vector):
    pass


class Acceleration(Vector):
    pass