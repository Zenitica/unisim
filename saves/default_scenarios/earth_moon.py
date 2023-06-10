from utils.scenarios import Scenario
from utils.objects import UniverseObject
from utils.physical_quantities import Vector, Force, Displacement, Velocity, Acceleration


class EarthMoonDoublePlanet(Scenario):
    def __init__(self):
        self.name = "Earth-Moon Double Planet"
        self.description = "A simulation of the Earth-Moon double planet system."
        self.objects = [UniverseObject(name="Earth",
                                       mass=5.97e24, 
                                       radius=6371 * 1e3, 
                                       displacement=Displacement(0, 0), 
                                       velocity=Velocity(0, 0)),
                        UniverseObject(name="Moon",
                                       mass=7.34e22,
                                       radius=1737.4 * 1e3,
                                       displacement=Displacement(384400 * 1e3, 0),
                                       velocity=Velocity(0, 1.022 * 1e3))]
        self.default_sim_frequency = 60
        self.default_display_frenquency = 1
        self.default_time_speed = 1


class EarthMoonCrash(EarthMoonDoublePlanet):
    def __init__(self):
        super().__init__()
        self.name = "Earth-Moon Crashing"
        self.description = "A simulation of the moon heading towards the earth."
        self.objects = [UniverseObject(name="Earth",
                                       mass=5.97e24, 
                                       radius=6371 * 1e3, 
                                       displacement=Displacement(0, 0), 
                                       velocity=Velocity(0, 0)),
                        UniverseObject(name="Moon",
                                       mass=7.34e22,
                                       radius=1737.4 * 1e3,
                                       displacement=Displacement(384400 * 1e3, 0),
                                       velocity=Velocity(-1 * 1e3, 200.99))]