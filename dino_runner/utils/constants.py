import pygame
import os

# Global Constants
TITLE = "Alpha Blasphemous"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
pygame.mixer.init()

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/run1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/run2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/run3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/run4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/run5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/run6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/run7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/run8.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/run9.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/run10.png"))
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/run1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/run2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/run3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/run4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/run5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/run6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/run7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/run8.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/run9.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/run10.png"))
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/sword1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/sword2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/sword3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/sword4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/sword5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/sword6.png"))
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/jump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/jump.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/jump.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/crouch1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/crouch2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/crouch3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/crouch4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/crouch5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/crouch6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/crouch7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/crouch8.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/crouch1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/crouch2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/crouch3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/crouch4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/crouch5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/crouch6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/crouch7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/crouch8.png"))
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/crouch1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/crouch2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/crouch3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/crouch4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/crouch5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/crouch6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/crouch7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/crouch8.png"))
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/mush1.png")),  
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/mush2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/mush3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/mush4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/mush5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/mush6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/mush7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/mush8.png"))
]  
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/skeleton1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/skeleton2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/skeleton3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/skeleton4.png"))
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/fly1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/fly2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/fly3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/fly4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/fly5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/fly6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/fly7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/fly8.png"))
]

MENU_BG = pygame.image.load(os.path.join(IMG_DIR, "Menu/menu_bg.png"))


MUSIC_THEME = os.path.join(IMG_DIR, 'Sound/Batalha.mp3')
MENU_THEME = os.path.join(IMG_DIR, 'Sound/O Carente.mp3')
JUMP = os.path.join(IMG_DIR, 'Sound/Jump.wav')
SHIELD_SOUND = os.path.join(IMG_DIR, 'Sound/rage.wav')
GAME_OVER = os.path.join(IMG_DIR, 'Sound/Desastre.mp3')


CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Other/Sword.png"))
SLOW = pygame.image.load(os.path.join(IMG_DIR, 'Other/Slow.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/BG12.png'))


HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "sword"
SLOW_TYPE = "slow"
