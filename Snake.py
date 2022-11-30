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
SIZE = 10
gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Snake')

#clock
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,25)

#funções
def snake(lead_x,lead_y,SIZE):
    pygame.draw.rect(gameDisplay,green,[lead_x,lead_y,SIZE,SIZE])

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

    randAppleX = random.randrange(0,WIDTH-SIZE,SIZE)
    randAppleY = random.randrange(0,HEIGHT-SIZE,SIZE)

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(black)
            message("Aperte C para jogar novamente ou Q para sair", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
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
        pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,SIZE,SIZE])
        snake(lead_x,lead_y,SIZE)

        pygame.display.update()  

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = random.randrange(0,WIDTH-SIZE,SIZE)
            randAppleY = random.randrange(0,HEIGHT-SIZE,SIZE)


        clock.tick(FPS) 


    pygame.quit()
    quit()

gameLoop()