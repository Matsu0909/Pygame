import pygame
import random
from Tela_Inicial import game_intro
from config import black,white,red,green,FPS,WIDTH,HEIGHT,APPLESIZE,SIZE,fontg,fontm,fontp
from funcoes import message, snake
from assets import head_img,apple_img

pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Snake')

#clock
clock = pygame.time.Clock()

#funções
def snake(SIZE,S_list,direction):
    if direction == 'oeste':
        head = pygame.transform.rotate(head_img,180)
    
    elif direction == 'norte':
        head = pygame.transform.rotate(head_img,270)

    elif direction == 'leste':
        head = pygame.transform.rotate(head_img, 0)

    elif direction == 'sul':
        head = pygame.transform.rotate(head_img,90)

    gameDisplay.blit(head, (S_list[-1][0],S_list[-1][1]))
    for XeY in S_list[:-1]:
        pygame.draw.rect(gameDisplay,green,[XeY[0],XeY[1],SIZE,SIZE])

def text_objects(text,color,size):
    if size == "small":
        textSurface = fontp.render(text,True,color)
    elif size == "medium":
        textSurface = fontm.render(text,True,color)
    elif size == "large":
        textSurface = fontg.render(text,True,color)
    return textSurface, textSurface.get_rect()


def message(msg,color,y_displace = 0, size='small'):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (WIDTH/2), (HEIGHT/2)+y_displace
    gameDisplay.blit(textSurf, textRect)

def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = WIDTH/2
    lead_y = HEIGHT/2
    lead_x_change = SIZE
    lead_y_change = 0
    direction = 'leste'

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
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
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
                    direction = 'oeste'
                    lead_x_change = -SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = 'leste'
                    lead_x_change = SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = 'sul'
                    lead_y_change = -SIZE
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = 'norte'
                    lead_y_change = SIZE
                    lead_x_change = 0

        #posicao
        if lead_y > HEIGHT or lead_y < 0 or lead_x < 0 or lead_x > WIDTH:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change
    

        gameDisplay.fill(white)
        gameDisplay.blit(apple_img, (randAppleX,randAppleY))
        #pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,APPLESIZE,APPLESIZE])

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

        snake(SIZE,snakeList,direction)

        pygame.display.update()

        #comer
        if lead_x >= randAppleX and lead_x <= randAppleX+APPLESIZE-SIZE:
            if lead_y >= randAppleY and lead_y <= randAppleY+APPLESIZE-SIZE:
                randAppleX = random.randrange(0,WIDTH-APPLESIZE,APPLESIZE)
                randAppleY = random.randrange(0,HEIGHT-APPLESIZE,APPLESIZE)
                snakeLength += 1


        clock.tick(FPS) 


    pygame.quit()
    quit()

game_intro()
gameLoop()