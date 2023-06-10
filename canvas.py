import time

import numpy as np
import matplotlib.pyplot as plt

from utils.constants import G
from utils.objects import UniverseObject
from utils.interactions import Interaction
from saves.default_scenarios.earth_moon import EarthMoonDoublePlanet, EarthMoonCrash
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

    def detect_collision(self):
        ret = list()
        for obj in self.objects:
            for other in self.objects:
                if obj != other:
                    if Interaction.detect_if_collided(obj, other):
                        if (other, obj) not in ret:
                            ret.append((obj, other))
        return ret



# initialize canvas
canvas = Canvas()

# load scenario
# canvas.load_canvas_from_scenario(EarthMoonDoublePlanet())
canvas.load_canvas_from_scenario(EarthMoonCrash())

# override default configuations
canvas.set_display_frequency(_DISPLAY_FRENQUENCY)
canvas.set_sim_frequency(_SIM_FREQUENCY)
canvas.set_time_speed(_TIME_SPEED)

# plt.axis([-500000 * 1e3 * 1.36 * 1.49, 500000 * 1e3 * 1.36 * 1.49, -500000 * 1e3, 500000 * 1e3])

while True:
    t = 0.
    time.sleep(1. / canvas.display_frenquency)
    for obj in canvas.objects:
        print(obj.display())
        # if obj.name == "Earth":
        #     plt.scatter(obj.displacement.x, obj.displacement.y, color = 'blue')
        # else:
        #     plt.scatter(obj.displacement.x, obj.displacement.y, color = 'red')
        # plt.pause(0.01)
    for i in range(int(canvas.time_speed * canvas.sim_frequency / canvas.display_frenquency)):
        canvas.calculate_combined_forces()
        canvas.update_canvas()
        collided_objects_tuple = canvas.detect_collision()
        if len(collided_objects_tuple) > 0:
            print("Collision detected!")
            print("====================")
            print("Current time: {}".format(t))
            for (obj1, obj2) in collided_objects_tuple:
                print("\t", obj1, obj2)
            exit(0)
        t += 1. / canvas.sim_frequency
        