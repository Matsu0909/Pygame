# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from config import WIDTH, HEIGHT

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Marcelo yag')

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
