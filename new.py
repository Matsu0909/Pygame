# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import os
from config import WIDTH,HEIGHT,GAME_NAME,TANKH,TANKW,IMG_DIR,WHITE,GREEN,BLACK

pygame.init()
pygame.font.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_NAME)

# ----- Inicia assets
font = pygame.font.SysFont(None, 48)
tank_img = pygame.image.load(os.path.join(IMG_DIR, 'tank.png')).convert()
tank_img_small = pygame.transform.scale(tank_img, (TANKW,TANKH))

# ----- Inicia estruturas de dados
game = True
tank_x = 200
# y negativo significa que está acima do topo da janela. O meteoro começa fora da janela
tank_y = 500
tank_speedx = 0
tank_speedy = 0

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Atualiza estado do jogo
    # Atualizando a posição do meteoro
    tank_x += tank_speedx
    tank_y += tank_speedy
    # Se o meteoro passar do final da tela, volta para cima
    if tank_y > HEIGHT or tank_x + TANKW < 0 or tank_x > WIDTH:
        tank_x = 200
        tank_y = 500

    # ----- Gera saídas
    window.fill(WHITE)  # Preenche com a cor branca

    #chao
    vertices = [(WIDTH, HEIGHT-35), (0, HEIGHT-35), (0, HEIGHT), (WIDTH, HEIGHT)]
    pygame.draw.polygon(window, GREEN, vertices)

    window.blit(tank_img_small, (tank_x, tank_y))
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados