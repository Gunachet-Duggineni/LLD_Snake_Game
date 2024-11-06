# This file manages the fruits that appear in the Pacman game, which give bonus points when eaten.
# fruit.py is used for:
#   Creating different types of fruit that appear as bonus items.
#   Handling when and where these fruits appear in the game.
#   Managing point values for each type of fruit, so players earn extra points.

# fruit.py is used in:
#   pacman.py: to allow Pacman to collect fruits and gain bonus points.
#   sprites.py: to show and animate the fruit on the screen.
#   constants.py: to get point values and appearance settings for each fruit.

# In short: fruit.py adds extra rewards to the game for players who love a high score!


import pygame
from entity import Entity
from constants import *
from sprites import FruitSprites

class Fruit(Entity):
    def __init__(self, node):
        Entity.__init__(self, node)
        self.name = FRUIT
        self.color = GREEN
        self.lifespan = 5
        self.timer = 0
        self.destroy = False
        self.points = 100
        self.setBetweenNodes(RIGHT)
        self.sprites = FruitSprites(self)

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.lifespan:
            self.destroy = True