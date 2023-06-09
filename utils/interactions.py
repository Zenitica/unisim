from physical_quantity import G
from objects import UniverseObject


def calculate_gravity_force(obj1, obj2):
    delta_displacement = obj2.displacement.vector_subtract(obj1.displacement)
    dist = delta_displacement.vector_l2_norm()
    force_magnitude = G * obj1.mass * obj2.mass / dist
    return force_magnitude