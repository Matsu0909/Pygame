# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 1000
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Marcelo yag')

# ----- Inicia assets
FPS = 30


# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
