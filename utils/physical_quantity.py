class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def vector_add(self, other):
        self.x += other.x
        self.y += other.y

    def vector_dot_product(self, other):
        return self.x * other.x + self.y * other.y
    

class Force(Vector):
    pass


class Displacement(Vector):
    pass


class Velocity(Vector):
    pass


class Acceleration(Vector):
    pass