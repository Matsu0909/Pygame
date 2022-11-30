import pygame
import random
from config import black,white,red,green,FPS,WIDTH,HEIGHT,APPLESIZE,SIZE,fontg,fontm,fontp,SIZEHEIGHT
from funcoes import message, snake, score
from assets import head_img,apple_img,tail_img

pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT+SIZEHEIGHT))
pygame.display.set_caption('Snake')
pygame.display.set_icon(apple_img)

#clock
clock = pygame.time.Clock()

#Carrega sons do jogo
chompsnd = pygame.mixer.Sound('assets/snd/chompsnd.mp3')

#funções
def game_intro():
    
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message("Bem-vindo à Python", 
        green,gameDisplay,
        -100, 
        "large")
        message("O objetivo do jogo é comer maçãs vermelhas e sobreviver",
        black,gameDisplay,
        -30)
        message("Quanto mais maçãs você comer, maior você fica",
        black,gameDisplay,
        10)
        message("Se você correr em si mesmo, ou nas bordas da tela, você morre",
        black,gameDisplay,
        50)
        message("Pressione ENTER para iniciar ou ESPAÇO para sair",
        black,gameDisplay,
        180)

        pygame.display.update()
        clock.tick(5)

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
            message("Aperte ENTER para jogar novamente ou Espaço para sair", red,gameDisplay)
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

        snake(SIZE,snakeList,direction,gameDisplay)

        score(snakeLength,gameDisplay)

        pygame.display.update()

        #comer
        if lead_x >= randAppleX and lead_x <= randAppleX+APPLESIZE-SIZE:
            if lead_y >= randAppleY and lead_y <= randAppleY+APPLESIZE-SIZE:
                randAppleX = random.randrange(0,WIDTH-APPLESIZE,APPLESIZE)
                randAppleY = random.randrange(0,HEIGHT-APPLESIZE,APPLESIZE)
                snakeLength += 1
                chompsnd.play()

        clock.tick(FPS) 


    pygame.quit()
    quit()

game_intro()
gameLoop()