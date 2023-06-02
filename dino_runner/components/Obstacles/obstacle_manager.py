import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.skeleton import Skeleton
from dino_runner.utils.constants import GAME_OVER


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):      
        obstacle_type = [       
            Cactus(), 
            Bird(),  
            Skeleton()  
        ]
        if len(self.obstacles) == 0:  
            self.obstacles.append(obstacle_type[random.randint(0,2)])  
            
        for obstacle in self.obstacles:       
            if game.player.dino_rect.colliderect(obstacle.rect): 
                if not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.playing = False
                    pygame.mixer.music.stop()
                    game_over = pygame.mixer.Sound(GAME_OVER)
                    game_over.play()
                    game.death_count += 1
                    break
                elif game.player.hammer:
                    self.obstacles.remove(obstacle)
                    break

                    
                    
                    
                    
                    

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
                
    def reset_obstacles(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)