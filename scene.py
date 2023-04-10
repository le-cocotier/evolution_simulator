import pygame

class Scene:
    def __init__(self, width, height) -> None:
        self.sky = pygame.Color(150, 193, 240)
        self.ground = pygame.Color(60, 120, 60)
        self.width = width
        self.height = height
        
    def draw(self, screen):
        screen.fill(self.sky)
        pygame.draw.rect(screen, self.ground, pygame.Rect(0, 2* self.height / 3, self.width, self.height))