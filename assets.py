import pygame
import os
from config import IMG_DIR, SND_DIR, FNT_DIR

BACKGROUND = 'background'
TANQUE1 = 'tanque_azul'
TANQUE1_EXPLODINDO = 'tanque1_explodindo'
TANQUE1_ATIRANDO = 'tanque1_atirando'
TANQUE2 = 'tanque_vermelho'
TANQUE2_EXPLODINDO = 'tanque2_explodindo'
TANQUE2_ATIRANDO = 'tanque2_atirando'
SOUNDT_EXP = 'somtanque_explodindo'

#-------------------------
def load_assets():
    assets = {}
    assets[TANQUE1] = pygame.image.load(os.path.join(IMG_DIR, 'tankblue.png')).convert()
    assets[TANQUE1_EXPLODINDO] = pygame.image.load(os.path.join(IMG_DIR, 'right_explode_blue-Sheet.png')).convert()
    assets[TANQUE1_ATIRANDO] = pygame.image.load(os.path.join(IMG_DIR,'right_fire_blue-Sheet.png')).convert()
    assets[TANQUE2] = pygame.image.load(os.path.join(IMG_DIR, 'tank_red_left.png')).convert()
    assets[TANQUE2_EXPLODINDO] = pygame.image.load(os.path.join(IMG_DIR, 'left_explode_red-Sheet.png')).convert()
    assets[TANQUE2_ATIRANDO] = pygame.image.load(os.path.join(IMG_DIR, 'left_fire_red-Sheet.png')).convert()
    assets[SOUNDT_EXP] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl6.wav'))
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'backgroundpygame.png')).convert()