from utils.constants import G
from utils.physical_quantities import Vector, Force, Displacement, Velocity, Acceleration


class UniverseObject:
    def __init__(self, name, mass, radius, displacement, velocity):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.displacement = displacement
        self.velocity = velocity
        self.force = None
        self.acceleration = None

    def __str__(self):
        return "{}: {}".format(self.name, (self.displacement.x, self.displacement.y))

    def display(self):
        return self.__str__()

    def apply_force_upon_self(self, force_outside):
        if self.force is None:
            self.force = force_outside
        else:
            self.force = self.force + force_outside

    def update(self, freq):
        delta_t = 1 / freq
        self.acceleration = self.force / self.mass
        self.velocity = self.velocity + self.acceleration * delta_t
        self.displacement = self.displacement + self.velocity * delta_t
        self.force = None
