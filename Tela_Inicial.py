#Aqui será implementado o código da tela inicial do jogo

import pygame
import time
import random
from funcoes import message

#Inicia o pygame
pygame.init()

#Cores
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

WIDTH = 800
HEIGHT = 600
gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Eat & Slither")

pygame.display.update()

gameExit = False

lead_x = WIDTH/2
lead_y = HEIGHT/2
lead_x_change = 0
lead_y_change = 0
FPS = 30
clock = pygame.time.Clock()
block_size = 10

font = pygame.font.SysFont(None, 25)

#Antes da função Snake
def game_intro():
    
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message("Bem-vindo ao Eat & Slither", 
        green, 
        -100, 
        "large")
        message("O objetivo do jogo é comer maças vermelhas e sobreviver",
        black,
        -30)
        message("Quanto mais maçâs você comer, maior você fica",
        black,
        10)
        message("Se você correr em si mesmo, ou nas bordas da tela, você morre",
        black,
        50)
        message("Pressione ENTER para iniciar ou ESPAÇO para sair",
        black,
        80)

        pygame.display.update()
        clock.tick(5)

        #Antes de gameLoop(), chamar a função gameIntro!!!!