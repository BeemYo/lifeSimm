import random
import math

class spiecie:
    def __init__(self, typ, x, y, ran, speed, border, foods):
        self.typ = typ
        self.x = x
        self.y = y
        self.ran = ran
        self.speed = speed
        self.food = 0
        self.world_border = border

    def move(self):
        open_x = self.x 
        self.x += random.uniform(-self.speed, self.speed)
        if not(self.x < 0 or self.x > self.world_border):
            self.x = open_x
        
        open_y = self.y
        self.y += random.uniform(-self.speed, self.speed)
        if not(self.y < 0 or self.y > self.world_border):
            self.y = open_y
    
    def checkFoods(self, foods):
        for food in foods:
            dis = math.sqrt((food.x - self.x) ** 2 + (food.y - self.y) ** 2)
            if dis < self.ran:
                print("found food")
                self.food += 1
                foods.remove(food)
    
    def checkScore(self):
        if self.food == 0:
            return "die"
        elif self.food == 1:
            return "live"
        elif self.food >= 2:
            return "reproduce"
