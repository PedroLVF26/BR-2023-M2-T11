import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

X_POS = 80
Y_POS = 310
JUMP_VEL = 8.5
Y_DUCK = 335
# Constante criada para definir o valor da coordenada em Y para o dinossauro agachado, visto que, caso utilize a constante Y_POS, o nosso dino irá 'flutuar'


class Dinossaur(Sprite):
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = 80
        self.dino_rect.y = 310
        self.step_index = 0
        self.jump_vel = JUMP_VEL
        self.dino_jump = False
        self.dino_run = True
        self.dino_duck = False
        # Atributo criado para que o nosso dino não inicie o jogo agachado.

    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
        # Aqui, verificamos se a variável dino_duck é True. Caso seja, o persoangem irá se agachar
            self.duck()
            # Caso a condição acima seja atendida, chamamos o método self.duck() para se encarregar da lógica do agachamento

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif not self.dino_jump:
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False
        
        if user_input[pygame.K_DOWN] and not self.dino_jump:
        # Condicional criada para verificar se o usuário pressionou a seta para baixo.
            self.dino_jump = False
            # Caso tenha pressionado, a variável dino_jump será False, pois, o boneco não pode correr e agachar enquanto pressiona uma só tecla
            self.dino_run = False
            # Caso tenha pressionado, a variável dino_run será False
            self.dino_duck = True
            # Caso tenha pressionado, a variável dino_duck será True
        

        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.dino_rect_y = Y_POS
            self.jump_vel = JUMP_VEL
            # Reinicia a velocidade do salto
            self.dino_jump = False
            # Permite que o dino pule mais de uma vez
            self.dino_run = True
            # Faz com que o dino volte a correr
            
    def duck(self):
        # Nesta linha, estamos atribuindo um valor para a variável self.image, sendo DUCKING[0] ou DUCKING[1], a depender do valor do step_index.
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1] 
        # Criamos o rect do personagem  utilizando o método get_rect() da imagem atual
        # O rect é utilizado para armazenar as coordenadas e o tamano do retângulo q está em volta da imagem
        self.dino_rect = self.image.get_rect()
        # A variável dino_rect.x recebe a nossa coordenada X do retângulo.
        # Definimos com o valor de X_POS, que foi definido anteiormente.
        self.dino_rect.x = X_POS
        # Fizemos o mesmo para a variável dino_rect.y, visto que definimos o valor da coordenada Y do retângulo
        # O valor definido foi criado agora, já que, caso colocassemos o valor como Y_POS, o dinossauro ficaria acima do chão.
        self.dino_rect.y = Y_DUCK
        # Estamos incrementando o valor do step_index em 1. A variável é utilizada para controlar a animação do personagem.
        self.step_index += 1
        # Esta variável serve para verificar se o dinossauro está 'ducking', ou 'agachado', ou não.
        self.dino_duck = False
        
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
