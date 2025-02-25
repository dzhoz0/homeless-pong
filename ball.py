import pygame
import random
from config import *
class Ball:
    def __init__(self, x, y, radius):
        self.x, self.y = x, y
        self.radius = radius
        self.rect = pygame.Rect(self.x, self.y, self.radius, self.radius)
        self.color = pygame.Color('gray')

        self.direction = random.choice(['left', 'right'])

        self.speed_x, self.speed_y = 0, 0

    def movement(self):
        if self.direction == 'left':
            self.speed_x = -10
        elif self.direction == 'right':
            self.speed_x = 10

        if self.rect.y >= HEIGHT - self.radius:
            self.speed_y = -10
        elif self.rect.y <= 0 + self.radius:
            self.speed_y = 10

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


    def update(self, screen):
        self.movement()
        pygame.draw.rect(screen, self.color, self.rect)