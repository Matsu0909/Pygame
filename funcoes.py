import pygame
from assets import head_img,tail_img
from config import green,fontg,fontm,fontp,WIDTH,HEIGHT,black,darkgreen,white,SIZE
import random


def snake(SIZE,S_list,direction,gameDisplay):
    #Trocar a rotação da imagem da cabeca e do rabo de acordo com a direção
    if direction == 'oeste':
        head = pygame.transform.rotate(head_img,180)
        tail = pygame.transform.rotate(tail_img,180)
    
    elif direction == 'norte':
        head = pygame.transform.rotate(head_img,270)
        tail = pygame.transform.rotate(tail_img,270)

    elif direction == 'leste':
        head = pygame.transform.rotate(head_img, 0)
        tail = pygame.transform.rotate(tail_img,0)

    elif direction == 'sul':
        head = pygame.transform.rotate(head_img,90)
        tail = pygame.transform.rotate(tail_img,90)

    #Blit na cabeça aparecer
    gameDisplay.blit(head, (S_list[-1][0],S_list[-1][1]))
    for XeY in S_list[1:-1]:
        pygame.draw.rect(gameDisplay,green,[XeY[0],XeY[1],SIZE,SIZE])
    
    if len(S_list) != 1:
        gameDisplay.blit(tail, (S_list[0][0],S_list[0][1]))

#Funções para colocar texto na tela
def text_objects(text,color,size):
    if size == "small":
        textSurface = fontp.render(text,True,color)
    elif size == "medium":
        textSurface = fontm.render(text,True,color)
    elif size == "large":
        textSurface = fontg.render(text,True,color)
    return textSurface, textSurface.get_rect()


def message(msg,color,gameDisplay,y_displace = 0, size='small'):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (WIDTH/2), (HEIGHT/2)+y_displace
    gameDisplay.blit(textSurf, textRect)

#Função dos pontos
def score(snakeLength,gameDisplay):
    pygame.draw.rect(gameDisplay,darkgreen,[0,0,WIDTH,100])
    ponto = (snakeLength-1)*100
    text = 'SCORE: {0}'.format(ponto)
    textSurf, textRect = text_objects(text,white,"medium")
    textRect.center = (WIDTH-100),(50)
    gameDisplay.blit(textSurf,textRect)

    text = 'Python'
    textSurf, textRect = text_objects(text,white,"medium")
    textRect.center = (70),(50)
    gameDisplay.blit(textSurf,textRect)


def obstacle():
    randObsX = random.randrange(0,WIDTH-SIZE,SIZE)
    randObsY = random.randrange(100,HEIGHT-SIZE,SIZE)
    return randObsX,randObsY