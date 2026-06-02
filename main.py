import pygame
from constants import SCREEN_WIDTH 
from constants import SCREEN_HEIGHT
from constants import PLAYER_RADIUS
from logger import log_state
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from logger import log_event
import sys
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0   
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    ateroidfield = AsteroidField()
    Shot.containers = (drawable, updatable, shots)


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        updatable.update(dt)
        player.player_shoot_cooldown -= dt
        for draw in drawable:
            draw.draw(screen)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            else:
                continue
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot) == True:
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        print(dt)
        #print(updatable)
        #print(drawable)
        
        


if __name__ == "__main__":
    main()
