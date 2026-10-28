import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return

        log_event("asteroid_split")
        r = random.uniform(20, 50)

        child_dir1 = self.velocity.rotate(r)
        child_dir2 = self.velocity.rotate(-r)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        child1 = Asteroid(self.position.x, self.position.y, new_radius)
        child2 = Asteroid(self.position.x, self.position.y, new_radius)

        child1.velocity = child_dir1 * 1.2
        child2.velocity = child_dir2 * 1.2
