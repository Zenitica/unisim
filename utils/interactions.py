from utils.constants import G
from utils.objects import UniverseObject
from utils.physical_quantities import Vector, Force, Displacement, Velocity, Acceleration


class Interaction:
    @staticmethod
    def get_gravity_force_upon_former(a, b):
        delta_displacement = b.displacement - a.displacement
        dist = delta_displacement.vector_norm_l2()
        force_magnitude = G * a.mass * b.mass / (dist ** 2)
        force_x = force_magnitude * delta_displacement.x / dist
        force_y = force_magnitude * delta_displacement.y / dist
        return Force(force_x, force_y)