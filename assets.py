import pygame
import os
from config import IMG_DIR, SND_DIR, FNT_DIR

BACKGROUND = 'background'
TANQUE1 = 'tanque_azul'
TANQUE1_EXPLODINDO = 'tanque1_explodindo1'
TANQUE_EXPLODINDO1 = 'tanque1_explodindo2'
TANQUE_EXPLODINDO2 = 'tanque1_explodindo3'
TANQUE_EXPLODINDO3 = 'tanque1_explodindo4'
TANQUE2 = 'tanque_vermelho'
TANQUE2_EXPLODINDO = 'tanque2_explodindo'
SOUNDT_EXP = 'somtanque_explodindo'
BALA = 'bala'

#-------------------------
def load_assets():
    assets = {}
    assets[TANQUE1] = pygame.image.load(os.path.join(IMG_DIR, 'tank.png')).convert()
    assets[TANQUE1_EXPLODINDO] = pygame.image.load(os.path.join(IMG_DIR, 'explosao1.png')).convert()
    assets[TANQUE2_EXPLODINDO] = pygame.image.load(os.path.join(IMG_DIR, 'explosao1.1.png')).convert()
    assets[TANQUE_EXPLODINDO1] = pygame.image.load(os.path.join(IMG_DIR, 'explosao2.png')).convert()
    assets[TANQUE_EXPLODINDO2] = pygame.image.load(os.path.join(IMG_DIR, 'explosao3.png')).convert()
    assets[TANQUE_EXPLODINDO3] = pygame.image.load(os.path.join(IMG_DIR, 'explosao4.png')).convert()
    assets[TANQUE2] = pygame.image.load(os.path.join(IMG_DIR, 'tank2.png')).convert()
    assets[SOUNDT_EXP] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl6.wav'))
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'backgroundpygame.png')).convert()
    assets[BALA] = pygame.image.load(os.path.join(IMG_DIR, 'bala.png')).convert()