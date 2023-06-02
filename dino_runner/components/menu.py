import pygame
import os

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from dino_runner.utils.text_utils import draw_message_component
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")




class Htp:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))       
        
        # Define o texto da tela
    def draw(self):
        img = pygame.image.load(os.path.join(IMG_DIR, "Menu/ShowHTP.png"))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        self.screen.blit(img, ((0, 0)))
        draw_message_component(
            f"COMO JOGAR:",
            self.screen,
            font_color=(179, 133, 121),
            font_size=36,
            pos_x_center=half_screen_width - 40,
            pos_y_center=half_screen_height - 170
        )
        draw_message_component(
            f"Pressione W pular",
            self.screen,
            font_color=(179, 133, 121),
            font_size=20,
            pos_x_center=half_screen_width ,
            pos_y_center=half_screen_height - 80
        )
        draw_message_component(
            f"Pressione LSHIFT para abrir a história",
            self.screen,
            font_color=(179, 133, 121),
            font_size=20,
            pos_x_center=half_screen_width,
            pos_y_center=half_screen_height - 40
        )
        draw_message_component(
            f"Pressione TAB para abrir o How To Play",
            self.screen,
            font_color=(179, 133, 121),
            font_size=20,
            pos_x_center=half_screen_width,
            pos_y_center=half_screen_height
        )
        draw_message_component(
            f"Precione ESPAÇO iniciar o jogo",
            self.screen,
            font_color=(179, 133, 121),
            font_size=20,
            pos_x_center=half_screen_width,
            pos_y_center=half_screen_height + 40
        )
