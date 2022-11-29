# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from config import WIDTH, HEIGHT,INIT,GAME,QUIT,GAME_NAME, VICTORY,WHITE,BLACK,FPS
from init_screen import init_screen
from game_screen import game_screen
from victory_screen import victory_screen

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_NAME)

# ----- Inicia estruturas de dados
game = True
font = pygame.font.SysFont(None, 80)
text1 = font.render(GAME_NAME, True, WHITE)
text2 = font.render("Pressione qualquer tecla para iniciar", True, WHITE)
clock = pygame.time.Clock()

# ===== Loop principal =====
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.KEYUP:
            pygame.quit()
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill(BLACK)
    window.blit(text1, (70, 250))
    window.blit(text2, (70, 500))
    
    pygame.display.flip()  # Preenche com a cor branca

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

