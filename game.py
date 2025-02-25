import pygame
from config import WIDTH, HEIGHT, P_HEIGHT, P_WIDTH
from player import Player
from ball import Ball
import time

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.generateGame()

    def generateGame(self):
        self.player1 = Player(10, HEIGHT // 2 - P_HEIGHT // 2, P_WIDTH, P_HEIGHT)
        self.player2 = Player(WIDTH - 30, HEIGHT // 2 - P_HEIGHT // 2, P_WIDTH, P_HEIGHT)
        self.ball = Ball(WIDTH // 2 - P_WIDTH, HEIGHT - P_WIDTH, P_WIDTH)

    def playerMove(self):
        keys = pygame.key.get_pressed()

        # Movement for player 1
        if keys[pygame.K_w]:
            self.player1.moveUp()
        if keys[pygame.K_s]:
            self.player1.moveDown()

        # Movement for player 2
        if keys[pygame.K_UP]:
            self.player2.moveUp()
        if keys[pygame.K_DOWN]:
            self.player2.moveDown()

    def ballHit(self):

        if pygame.Rect.colliderect(self.ball.rect, self.player1.rect):
            print("Ball hit")
            self.ball.direction = "right"
        if pygame.Rect.colliderect(self.ball.rect, self.player2.rect):
            self.ball.direction = "left"

        if self.ball.rect.left >= WIDTH:
            # self.playerA.score += 1
            self.ball.rect.x = WIDTH // 2
            self.player1.rect.y = HEIGHT // 2 - P_HEIGHT // 2
            self.player2.rect.y = HEIGHT // 2 - P_HEIGHT // 2
            time.sleep(0.25)
        elif self.ball.rect.right <= 0:
            # self.playerB.score += 1
            self.ball.rect.x = WIDTH // 2
            self.player1.rect.y = HEIGHT // 2 - P_HEIGHT // 2
            self.player2.rect.y = HEIGHT // 2 - P_HEIGHT // 2
            time.sleep(0.25)




    def update(self):
        self.player1.update(self.screen)
        self.player2.update(self.screen)
        self.ballHit()
        self.ball.update(self.screen)