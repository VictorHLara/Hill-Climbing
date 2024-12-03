import pygame

# Configurações da tela
WIDTH, HEIGHT = 1000, 600
BG_COLOR = (40, 40, 40)
COLUMN_COLOR = (100, 100, 100)
AGENT_COLOR = (255, 255, 0) 
TEXT_COLOR = (255, 255, 255)

# Configurações do espaço de busca
NUM_COLUMNS = 20
COLUMN_WIDTH = WIDTH // NUM_COLUMNS
MAX_HEIGHT = 20

# Lista de valores (de 0 a 20)
values = [3, 2, 3, 5, 4, 4, 5, 6, 8, 9, 10, 11, 14, 15, 16, 16, 13, 12, 12, 9]

# Variáveis de controle
agent_started = False
step = 0
start_pos = 10  # O agente começa na primeira coluna
path = []
final_position = None  # Para armazenar a posição final do agente
search_completed = False  # Marca se a busca foi concluída

# Inicializa Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 36)

# Variáveis de controle de estado
agent_started = False
step = 0
search_completed = False
