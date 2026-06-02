import pygame
from constants import PLAYER_RADIUS
from constants import LINE_WIDTH
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from logger import log_event
import random
#from asteroidfield import AsteroidField

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
    
    def draw(self, screen) -> None:
        pygame.draw.circle(
            screen, 
            "white", 
            self.position, 
            self.radius, 
            LINE_WIDTH
            )
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            new_velocity_1 = (self.velocity.rotate(random_angle)) * 1.2
            new_velocity_2 = (self.velocity.rotate(-random_angle)) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = new_velocity_1
            asteroid_2.velocity = new_velocity_2

            #(new_radius, self.position, new_velocity_1)
            #AsteroidField.spawn(new_radius, self.position, new_velocity_2)