from spiecie import *
from food import *
import random

def newSpiecie():
    global spiecies
    spiecies.append(spiecie(
        "normal",
        random.randint(0, world_border),
        random.randint(0, world_border),
        10, 2, world_border, foods))

def newFoods():
    global foods
    foods.clear()
    for i in range(100):
        foods.append(food(world_border))

def round():
    global spiecies
    newFoods()
    #let the players move
    for i in range(100):
        for spiecie in spiecies:    
            spiecie.checkFoods(foods)
            spiecie.move()

    #check what the spiecies schould do
    for spiecie in spiecies:
        act = spiecie.checkScore()
        print(act)
        print(len(foods))

        if act == "die":
            spiecies.remove(spiecie)
        elif act == "live":
            pass
        elif act == "reproduce":
            newSpiecie()

        spiecie.x = random.uniform(0, world_border)
        spiecie.y = random.uniform(0, world_border)
        spiecie.food = 0
    
    print(len(foods))
    print(len(spiecies))
    

foods = []
spiecies = []
world_border = 500

#add new spiecies to the world
for i in range(100):
    newSpiecie()

round()
