from object import UniverseObject

from utils.constants import G


class Canvas:
    def __init__(self):
        self.objects = []
        self.frequency = None

    def set_frequency(self, freq):
        self.frequency = freq
    
    def add_object(self, obj):
        self.objects.append(obj)

    def init_canvas(self):
        for obj in self.objects:
            for other in self.objects:
                if obj != other:
                    obj.apply_force(calculate_gravity_force(obj, other))

    def update_canvas(self):
        assert self.frequency is not None, "Frequency not set."
        for obj in self.objects: