import random

class food:
    def __init__(self, world_border):
        self.x = random.uniform(0, world_border)
        self.y = random.uniform(0, world_border)
