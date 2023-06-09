from utils.physical_quantity import Vector, Force, Displacement, Velocity, Acceleration
from utils.constants import G


class UniverseObject:
    def __init__(self, name, mass, radius, displacement, velocity):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.displacement = displacement
        self.velocity = velocity
        self.force = None
        self.acceleration = None

    def display(self):
        return "{}: {}".format(self.name, (self.displacement.x, self.displacement.y))

    def apply_force_upon_self(self, force):
        if self.force is None:
            self.force = force
        else:
            self.force.vector_add(force)

    def apply_gravity_force_upon_self(self, other):
        delta_displacement = other.displacement.vector_subtract(self.displacement)
        dist = delta_displacement.vector_l2_dist()
        force_magnitude = G * self.mass * other.mass / (dist ** 2)
        # print(force_magnitude)
        force_x = force_magnitude * delta_displacement.x / dist
        force_y = force_magnitude * delta_displacement.y / dist
        force = Force(force_x, force_y)
        self.apply_force_upon_self(force)

    def update(self, freq):
        delta_t = 1 / freq
        self.acceleration = self.force.vector_div_by_scalar(self.mass)
        # print(self.name, self.acceleration.x, self.acceleration.y)
        self.velocity = self.velocity.vector_add(self.acceleration.vector_mul_by_scalar(delta_t))
        # print(self.name, self.velocity.x, self.velocity.y)
        self.displacement = self.displacement.vector_add(self.velocity.vector_mul_by_scalar(delta_t))
        # print(self.name, self.displacement.x, self.displacement.y)
        self.force = None


