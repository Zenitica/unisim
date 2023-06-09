import time

from utils.objects import UniverseObject
from utils.physical_quantity import Vector, Force, Displacement, Velocity, Acceleration
from utils.constants import G
from config import _DISPLAY_FRENQUENCY, _SIM_FREQUENCY, _TIME_SPEED


class Canvas:
    def __init__(self):
        self.objects = []
        self.sim_frequency = None
        self.display_frenquency = None

    def set_sim_frequency(self, freq):
        self.sim_frequency = freq

    def set_display_frequency(self, freq):
        self.display_frenquency = freq
    
    def add_object(self, obj):
        self.objects.append(obj)

    def calculate_combined_forces(self):
        for obj in self.objects:
            # gravity
            for other in self.objects:
                if obj != other:
                    obj.apply_gravity_force_upon_self(other)
            # print(obj.name, obj.force.x, obj.force.y)

    def update_canvas(self):
        assert self.sim_frequency is not None, "Simulation frequency not set."
        for obj in self.objects:
            obj.update(self.sim_frequency)



canvas = Canvas()
canvas.set_sim_frequency(_SIM_FREQUENCY)
canvas.set_display_frequency(_DISPLAY_FRENQUENCY)
canvas.add_object(UniverseObject(name="Earth",
                                 mass=5.97e24, 
                                 radius=6371 * 1e3, 
                                 displacement=Displacement(0, 0), 
                                 velocity=Velocity(0, 0)))
canvas.add_object(UniverseObject(name="Moon",
                                 mass=7.34e22,
                                 radius=1737.4 * 1e3,
                                 displacement=Displacement(384400 * 1e3, 0),
                                 velocity=Velocity(0, 1.022 * 1e3)))
while True:
    time.sleep(1. / canvas.display_frenquency)
    for obj in canvas.objects:
        print(obj.display())
    for i in range(int(_TIME_SPEED * canvas.sim_frequency / canvas.display_frenquency)):
        canvas.calculate_combined_forces()
        canvas.update_canvas()