import random
import pygame
from dino_runner.components.powerups.shield import Shield
from dino_runner.components.powerups.hammer import Hammer
from dino_runner.components.powerups.slow import Slow
from dino_runner.utils.constants import SHIELD_SOUND 


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        self.slow_power_up_active = False
        self.slow_factor = 0.5

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200, 300) 
            opcoes = random.randint(0, 3) == 0
            if opcoes == 1:
                self.power_ups.append(Hammer())
            elif opcoes == 2:
                self.power_ups.append(Shield())
            else:
                self.power_ups.append(Slow())

    def update(self, score, game_speed, player):
        self.generate_power_up(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                effect = pygame.mixer.Sound(SHIELD_SOUND)
                effect.play()
                power_up.start_time = pygame.time.get_ticks()

                if isinstance(power_up, Shield):
                    player.shield = True
                    player.hammer = False
                elif isinstance(power_up, Hammer):
                    player.shield = False
                    player.hammer = True
                elif isinstance(power_up, Slow):
                    player.slow = True
                    game_speed * 0.5
                player.has_power_up = True
                player.type = power_up.type
                player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)