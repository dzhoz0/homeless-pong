import pygame

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.rect = pygame.Rect(x, y, width, height)
        self.color = pygame.Color("gray")
        self.playerSpeed = 18
        self.score = 0

    def moveUp(self):
        self.rect.y -= self.playerSpeed

    def moveDown(self):
        self.rect.y += self.playerSpeed

    def update(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)