import pygame
from constants import PLAYER_RADIUS
from constants import LINE_WIDTH
from circleshape import CircleShape

class Player(CircleShape):
    def __init__self(self, x, y):
        self.x = x
        self.y = y
        self.radius = PLAYER_RADIUS
        self.rotation = 0
    
    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen) -> None:
        self.polygon = pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
