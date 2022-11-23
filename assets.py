import pygame
import os
from config import IMG_DIR, SND_DIR, FNT_DIR

BACKGROUND = 'background'
DESTROY_SOUND = 'destroy_sound'
TANQUE1 = 'tanque_azul'
TANQUE1_EXPLODINDO = ''

#-------------------------
def load_assets():
    assets = {}
    assets[TANQUE1] = pygame.image.load(os.path.join(IMG_DIR, 'tankblue.png')).convert()
    assets[TANQUE1_EXPLODINDO] = pygame.image.load(os.path.join(IMG_DIR, 'right_explode_blue-Sheet.png')).convert()
    