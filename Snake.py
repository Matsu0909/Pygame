import pygame
import random

pygame.init()

#cores
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

FPS = 15

WIDTH = 800
HEIGHT = 600
APPLESIZE = 10
SIZE = 10
gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Snake')

#clock
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,25)

#funções
def snake(SIZE,S_list):
    for XeY in S_list:
        pygame.draw.rect(gameDisplay,green,[XeY[0],XeY[1],SIZE,SIZE])

def message(msg,color):
    screen_text = font.render(msg,True,color)
    gameDisplay.blit(screen_text, [WIDTH/2,HEIGHT/2])

def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = WIDTH/2
    lead_y = HEIGHT/2
    lead_x_change = 0
    lead_y_change = 0

    randAppleX = random.randrange(0,WIDTH-APPLESIZE,APPLESIZE)
    randAppleY = random.randrange(0,HEIGHT-APPLESIZE,APPLESIZE)

    snakeList = []
    snakeLength = 1

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(black)
            message("Aperte ENTER para jogar novamente ou Espaço para sair", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_RETURN:
                        gameLoop()
                


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -SIZE
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = SIZE
                    lead_x_change = 0

        #posicao
        if lead_y > HEIGHT or lead_y < 0 or lead_x < 0 or lead_x > WIDTH:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,APPLESIZE,APPLESIZE])

        #tamanho da cobra
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        
        if len(snakeList) > snakeLength:
            del snakeList[0]

        #colisao
        for SEGMENT in snakeList[:-1]:
            if SEGMENT == snakeHead:
                gameOver = True

        snake(SIZE,snakeList)

        pygame.display.update()  

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = random.randrange(0,WIDTH-SIZE,SIZE)
            randAppleY = random.randrange(0,HEIGHT-SIZE,SIZE)
            snakeLength += 1

        clock.tick(FPS) 


    pygame.quit()
    quit()

gameLoop()