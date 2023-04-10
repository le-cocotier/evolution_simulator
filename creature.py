import random, pygame, constant

class Creature:
    """graph"""
    def __init__(self) -> None:
        pass

class Node:
    """Create a node"""
    def __init__(self, strength, x, y) -> None:
        self.strength = strength
        self.radius = 20
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

    def gravity(self, floor):
        if self.y + self.radius >= floor:
            self.vy = 0
            self.y = floor - self.radius
        else:
            self.vy += 0.017 * constant.g
            self.y += self.vy

    def draw(self, screen, floor):
        self.gravity(floor)
        pygame.draw.circle(screen, "red", (self.x, self.y), self.radius)


class Muscle:
    """Create a muscle between 2 nodes"""
    def __init__(self) -> None:
        self.length = random.randint(10, 20)