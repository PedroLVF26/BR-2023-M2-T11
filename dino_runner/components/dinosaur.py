import pygame
import pygame.mixer
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, HAMMER_TYPE, DUCKING_HAMMER, DUCKING_SHIELD, JUMPING_HAMMER, JUMPING_SHIELD, RUNNING_HAMMER, RUNNING_SHIELD, JUMP, SLOW, SLOW_TYPE

DUCK_IMG = { DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER, SLOW_TYPE: DUCKING }
JUMP_IMG = { DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER, SLOW_TYPE: JUMPING }
RUN_IMG = { DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER, SLOW_TYPE: RUNNING }
X_POS = 80
Y_POS = 455
Y_POS_DUCK = 500
JUMP_VEL = 8.5


class Dinosaur(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index =  0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.dino_jump_vel = JUMP_VEL

        self.setup_state()

    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.hammer = False  
        self.slow = False
        self.show_text = False
        self.shield_time_up = 0

    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

        if user_input[pygame.K_w] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
            effect_jump = pygame.mixer.Sound(JUMP)
            effect_jump.play()
            self.dino_duck = False

        elif user_input[pygame.K_LSHIFT] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True

        elif not self.dino_jump and not self.dino_duck:
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False


        if self.step_index >= 9:
            self.step_index = 0
    

    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 2]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.dino_jump_vel * 5
            self.dino_jump_vel -= 0.8
        if self.dino_jump_vel < -JUMP_VEL:
            self.dino_rect_y = Y_POS
            self.dino_jump = False
            self.dino_jump_vel = JUMP_VEL

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index // 2]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS_DUCK
        self.dino_duck = False
        self.step_index += 1
            
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
