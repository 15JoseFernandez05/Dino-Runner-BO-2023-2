import pygame
import os

# Global Constants
TITLE = "Sonic_Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

SONIC_RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Sonic/sprite1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Sonic/sprite2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Sonic/sprite3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Sonic/sprite4.png")),
]


SONIC_JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Sonic/syasprite3.png"))

SONIC_DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Sonic/syasprite1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Sonic/syasprite2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Sonic/syasprite3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Sonic/syasprite4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Sonic/syasprite5.png")),
]

SMALL_ENEMY = [
    pygame.image.load(os.path.join(IMG_DIR, "Enemies/small_enemy1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Enemies/small_enemy3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Enemies/small_enemy2.png")),
]
LARGE_ENEMY = [
    pygame.image.load(os.path.join(IMG_DIR, "Enemies/large_enemy1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Enemies/large_enemy2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Enemies/large_enemy3.png")),
]

BEE = [
    pygame.image.load(os.path.join(IMG_DIR, "Bee/bee1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bee/bee2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bee/bee3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bee/bee4.png")),
]

RINGS = [
    pygame.image.load(os.path.join(IMG_DIR, "Other/ring1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Other/ring2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Other/ring2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Other/ring2.png")),
]

SONIC_DEAD = pygame.image.load(os.path.join(IMG_DIR, 'Sonic/sonic_dead.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/fondo.jpg'))
BG2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/suelo.png'))

pygame.init()
pygame.mixer.init()

SOUNDS = pygame.mixer.music.load(os.path.join(IMG_DIR, "Sounds/level_music.mpeg"))
MENU = pygame.image.load(os.path.join(IMG_DIR, 'Other/menu.jpg'))
LIVE = pygame.image.load(os.path.join(IMG_DIR, 'Other/live.png'))
SUPER_SONIC = [
    pygame.image.load(os.path.join(IMG_DIR, 'Sonic/supersonic.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Sonic/supersonic.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Sonic/supersonic.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Sonic/supersonic.png')),
]
ESMERALD = pygame.image.load(os.path.join(IMG_DIR, 'Other/esmerald.png'))

DEFAULT_TYPE = "default"
RING_TYPE = "ring"
LIVE_TYPE = "live"
SUPER_SONIC_TYPE = "supersonic"
