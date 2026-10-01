from circleshape import CircleShape
import pygame
import random
from constants import *
from logger import log_event, log_state

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        old_radius = self.radius
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angle1 = self.velocity.rotate(random.uniform(20, 50))
            new_angle2 = self.velocity.rotate(-1 * random.uniform(20,50))
            small_asteroid_radius = old_radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, small_asteroid_radius)
            new_asteroid1.velocity = 1.2 * new_angle1
            new_asteroid2 = Asteroid(self.position.x, self.position.y, small_asteroid_radius)
            new_asteroid2.velocity = 1.2 * new_angle2
