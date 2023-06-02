import pygame
import os 

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from dino_runner.utils.text_utils import draw_message_component

IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

class About:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))       
        
        # Define o texto da tela
    def draw(self):
        img = pygame.image.load(os.path.join(IMG_DIR, "Menu/About.png"))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        self.screen.blit(img, ((0, 0)))
        draw_message_component(
            f"A NOSSA HISTÓRIA É",
            self.screen,
            font_color=(179, 154, 63),
            font_size=20,
            pos_x_center=half_screen_width,
            pos_y_center=half_screen_height - 200
        )
        draw_message_component( 
            f'A nossa história se passa em Cvstodia, um local que foi terrivelmente afetado por uma',
            self.screen,
            font_color=(134, 118, 102),
            font_size=15,
            pos_x_center=half_screen_width,
            pos_y_center=half_screen_height - 130
        )
        draw_message_component(
            f'maldição, chamada "O milagre". Sendo perseptivel a decadência de Cvstodia, nota-se que a',
            self.screen,
            font_color=(134, 118, 102),
            font_size=15,
            pos_x_center=half_screen_width,
            pos_y_center=half_screen_height - 110
        )
        draw_message_component(
            f'maldição da ciadade não diz respeito somente a si mesma, mas também aos seus cidadãos.',
            self.screen,
            font_color=(134, 118, 102),
            font_size=15,
            pos_x_center=half_screen_width,
            pos_y_center=half_screen_height - 90
        )
        draw_message_component(
            f'Os piores medos, os monstros mais macabros são sugados pela maldição do Milagre e jogados',
            self.screen,
            font_color=(134, 118, 102),
            font_size=15,
            pos_x_center=half_screen_width,
            pos_y_center=half_screen_height - 70
        )
        draw_message_component(
            f'na realidade de Cvstodia.',
            self.screen,
            font_color=(134, 118, 102),
            font_size=15,
            pos_x_center=half_screen_width - 215,
            pos_y_center=half_screen_height - 50
        )
        draw_message_component(
            f'Nesta história, você é o penitente. Você é um dos únicos que consegue libertar estas almas',
            self.screen,
            font_color=(134, 118, 102),
            font_size=15,
            pos_x_center=half_screen_width,
            pos_y_center=half_screen_height - 30
        )
        draw_message_component(
            f'atormentadas do sofrimento. Como penitente e sobrevivente de uma guerra brutal, o Pesar',
            self.screen,
            font_color=(134, 118, 102),
            font_size=15,
            pos_x_center=half_screen_width,
            pos_y_center=half_screen_height - 10
        )
        draw_message_component(
            f'Silêncioso, seu objetivo é libertar a cidade desta maldição, junto à sua espada: Mea Culpa,',
            self.screen,
            font_color=(134, 118, 102),
            font_size=15,
            pos_x_center=half_screen_width,
            pos_y_center=half_screen_height + 10
        )
        draw_message_component(
            f'e correr em busca da redenção.',
            self.screen,
            font_color=(134, 118, 102),
            font_size=15,
            pos_x_center=half_screen_width - 190,
            pos_y_center=half_screen_height + 30
        )


