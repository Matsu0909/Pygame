import pygame
import time
import random

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

def message(msg, color):
    text = font.render(msg,True,color)
    gameDisplay.blit(text, [WIDTH/2, HEIGHT/2])

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

game_intro()

while not gameExit:
    for event in pygame.event.get():
        #Sair do jogo
        if event.type == pygame.QUIT:
            gameExit = True
        #Mover cobra para os lados e para cima
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -block_size
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = block_size
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -block_size
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = block_size
                lead_x_change = 0
    #Fecha o jogo se acertar os limites da tela
    if lead_x >= WIDTH or lead_x < 0 or lead_y >= HEIGHT or lead_y < 0:
        gameExit = True

        #Cobra para de se mover se não continuar pressionando a tecla
        #if event.type == pygame.KEYUP:
        #    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #        lead_x_change = 0 

    lead_x += lead_x_change
    lead_y += lead_y_change
    #Configurações do background
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, block_size, block_size])
    #Atuaiza o background
    pygame.display.update()
    
    clock.tick(FPS)

#Menssagem de game over
message('Você perdeu! :(', red)
pygame.display.update()
time.sleep(2)
#Sai do jogo
pygame.quit()
quit()