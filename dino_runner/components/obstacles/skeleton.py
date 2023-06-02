from dino_runner.utils.constants import LARGE_CACTUS
from dino_runner.components.obstacles.obstacle import Obstacle




class Skeleton(Obstacle):
    def __init__(self):
        super().__init__(LARGE_CACTUS, 0)
        self.rect.y = 440
        self.step_index = 0
        self.image_index = 0

    def draw(self, screen):
        screen.blit(self.image[self.image_index], self.rect)
        self.step_index += 1

        if self.step_index >= 2:
            self.step_index = 0
            self.image_index += 1
            if self.image_index >= len(self.image):
                self.image_index = 0
                