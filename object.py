from utils.physical_quantity import *


class UniverseObject:
    def __init__(self, mass, radius, displacement, velocity):
        self.mass = mass
        self.radius = radius
        self.displacement = displacement
        self.velocity = velocity
        self.force = None
        self.acceleration = None

    def apply_force(self, force):
        if self.force is None:
            self.force = force
        else:
            self.force.vector_add(force)

    def update(self, freq):
        delta_t = 1 / freq
        self.acceleration = self.force / self.mass
        self.velocity.vector_add(self.acceleration * delta_t)
        self.displacement.vector_add(self.velocity * delta_t)
        self.force = None





