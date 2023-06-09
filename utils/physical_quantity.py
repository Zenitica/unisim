class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def vector_add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def vector_subtract(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def vector_dot_product(self, other):
        return self.x * other.x + self.y * other.y
    
    def vector_l2_dist(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def vector_div_by_scalar(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)
    
    def vector_mul_by_scalar(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    

class Force(Vector):
    pass


class Displacement(Vector):
    pass


class Velocity(Vector):
    pass


class Acceleration(Vector):
    pass