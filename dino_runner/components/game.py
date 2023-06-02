import pygame
from pygame.locals import *
import os


from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, MUSIC_THEME, MENU_THEME
from dino_runner.components.Dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.components.powerups.power_up_manager import PowerUpManager
from dino_runner.components.menu import Htp
from dino_runner.components.about import About

IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
pygame.mixer.init()

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        # pontuação
        self.score = 0
        self.death_count = 0
        self.high_score = 0
        self.game_speed = 20
        # localização
        self.x_pos_bg = 0
        self.y_pos_bg = -50
        # tela menu
        self.htp = Htp()
        self.about = About()
        # pause
        self.paused = False
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()




    def play_menu_music(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(MENU_THEME)
        pygame.mixer.music.play(-1)

    def play_game_music(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(MUSIC_THEME)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)

# função de executar
    def execute(self):
        self.play_menu_music()
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
            else:
                self.play_game_music()
               

        pygame.display.quit()
        pygame.quit()
    

    def run(self):
        self.playing = True
        self.play_game_music()        
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.game_speed = 20
        self.score = 0
        # jogo rodando
        while self.playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()


            self.update()
            self.draw()
            self.events()
             
        
# detalhando os eventos do jogo
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # iniciar
                self.playing = False
                # caminhar
                self.running = False
        
# atualizar informações do jogo
    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player)
        if not self.playing and self.death_count == 1:
            pygame.mixer.music.stop()

    def update_score(self):
            self.score += 1
            if self.score % 100 == 0:
                self.game_speed += 3
                if self.player.has_power_up and self.player.slow:
                    self.game_speed *= 0.5
                           
    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)


        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        self.x_pos_bg -= self.game_speed
        if self.x_pos_bg <= -image_width:
            self.x_pos_bg = 0
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))


    def draw_score(self):
        draw_message_component(
            f"PONTOS: {self.score}",
            self.screen,
            pos_x_center = 1000,
            pos_y_center = 50
        )

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                draw_message_component(
                    f"{self.player.type.upper()} ENABLE {time_to_show} SECONDS",    #captalize ---> upper
                    self.screen,
                    font_size=25,
                    pos_x_center=500,
                    pos_y_center=40
                )

            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def show_about(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

            self.about.draw()  # Chama o método draw() na instância de about
            pygame.display.flip()


    def show_htp(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

            self.htp.draw()  # Chama o método draw() na instância de Htp
            pygame.display.flip()
            
    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.run()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        self.show_htp()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LCTRL:
                        self.show_about()

    
    def show_menu(self):
        image = pygame.image.load(os.path.join(IMG_DIR, "Menu/menu_bg.png"))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        if self.death_count == 0:
            self.screen.blit(image, ((0, 0)))
            draw_message_component("PRESSIONE QUALQUER TECLA PARA INICAR O JOGO.", self.screen, font_size=20, pos_y_center=half_screen_width - 120, font_color=(179, 133, 121))
            pygame.draw.rect(self.screen, (24, 24, 37), (0, 300, 160, 250))
            draw_message_component(
                f"V: 0.0.1(ALPHA)",
                self.screen,
                font_color=(179, 133, 121),
                font_size=20,
                pos_x_center=half_screen_width - 450,
                pos_y_center=half_screen_height + 280
            )
            draw_message_component(
                f"[LCTRL] ABOUT",
                self.screen,
                font_size=15,
                pos_x_center=half_screen_width - 470,
                pos_y_center=half_screen_height + 90

            )
            draw_message_component(
                f"[TAB] HOW TO PLAY",
                self.screen,
                font_size=15,
                pos_x_center=half_screen_width - 470,
                pos_y_center=half_screen_height + 120
            )
            
            
        else:
            menu_game_over = pygame.image.load(os.path.join(IMG_DIR, "Menu/GAME_OVER_MENU.png"))
            self.screen.blit(menu_game_over, ((0, 0)))
            draw_message_component("PRESSIONE QUALQUER TECLA PARA REINICAR O JOGO.", self.screen, pos_y_center = half_screen_height + 140, font_color=(120, 6, 6))
            draw_message_component(
                f"SUA PONTUAÇÃO: {self.score}",
                self.screen,
                pos_y_center=half_screen_height - 280,
                font_color=(120, 6, 6)
            )

            draw_message_component(
                f"CONTAGEM DE VIDA: {self.death_count}",
                self.screen, 
                pos_y_center=half_screen_height - 230,
                font_color=(120, 6, 6)
                )
            
            draw_message_component(
                f"RECORDE DE PONTUAÇÃO: {self.high_score}",
                self.screen,
                pos_y_center=half_screen_height - 180,
                font_color=(120, 6, 6)
                )
            
            
        pygame.display.flip()
        self.handle_events_on_menu()
        
        