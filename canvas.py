import time

from utils.constants import G
from utils.objects import UniverseObject
from utils.interactions import Interaction
from saves.default_scenarios.earth_moon import EarthMoonDoublePlanet
from utils.physical_quantities import Vector, Force, Displacement, Velocity, Acceleration

from config import _DISPLAY_FRENQUENCY, _SIM_FREQUENCY, _TIME_SPEED


class Canvas:
    def __init__(self):
        self.objects = []
        self.sim_frequency = None
        self.display_frenquency = None
        self.time_speed = None

    def load_canvas_from_scenario(self, scenario):
        self.objects = scenario.objects
        self.sim_frequency = scenario.default_sim_frequency
        self.display_frenquency = scenario.default_display_frenquency
        self.time_speed = scenario.default_time_speed

    def set_sim_frequency(self, freq):
        self.sim_frequency = freq

    def set_display_frequency(self, freq):
        self.display_frenquency = freq

    def set_time_speed(self, t_speed):
        self.time_speed = t_speed
    
    def add_object(self, obj):
        self.objects.append(obj)

    def calculate_combined_forces(self):
        for obj in self.objects:

            # gravity
            for other in self.objects:
                if obj != other:
                    g = Interaction.get_gravity_force_upon_former(obj, other)
                    obj.apply_force_upon_self(g)

    def update_canvas(self):
        assert self.sim_frequency is not None, "Simulation frequency not set."
        for obj in self.objects:
            obj.update(self.sim_frequency)


canvas = Canvas()
canvas.load_canvas_from_scenario(EarthMoonDoublePlanet())

while True:
    time.sleep(1. / canvas.display_frenquency)
    for obj in canvas.objects:
        print(obj.display())
    for i in range(int(canvas.time_speed * canvas.sim_frequency / canvas.display_frenquency)):
        canvas.calculate_combined_forces()
        canvas.update_canvas()