from os import path
import pygame

pygame.init()
# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')

#Tamanho
WIDTH = 800
HEIGHT = 600

TANKH = 20
TANKW = 40

CHAOH = 30

#Nome do jogo
GAME_NAME = 'TANK WARS'

#assets
FPS = 30

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

FONTEP = pygame.font.SysFont(None, 25)
FONTEM = pygame.font.SysFont(None, 50)
FONTEG = pygame.font.SysFont(None, 80)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2
VICTORY = 3

#Dois players
PLAYER_1 = 1
PLAYER_2 = 2
WINNER = 0

TURN = 1