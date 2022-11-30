import pygame

#Inicia o pygame
pygame.init()

#Cores
branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)

#Pixels e nome do jogo
WIDTH = 800
HEIGHT = 600
gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Eat & Slither")

#Atualiza pixels e nome do jogo 
pygame.display.update()

#Variável de saída do jogo
gameExit = False

#Mais variáveis
lead_x = WIDTH/2
lead_y = HEIGHT/2
lead_x_change = 0
lead_y_change = 0
FPS = 30
clock = pygame.time.Clock()
block_size = 10

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
    gameDisplay.fill(branco)
    pygame.draw.rect(gameDisplay, preto, [lead_x, lead_y, block_size, block_size])
    #Atuaiza o background
    pygame.display.update()
    
    clock.tick(FPS)

#Sai do jogo
pygame.quit()
quit()