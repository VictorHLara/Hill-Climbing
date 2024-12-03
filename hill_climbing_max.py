import pygame
from configs import *

def hill_climbing_max(values, start_pos):
    """Algoritmo de subida de encosta no espaço discreto 2D."""
    current_pos = start_pos
    path = [current_pos]
    while True:
        left = current_pos - 1 if current_pos > 0 else None
        right = current_pos + 1 if current_pos < len(values) - 1 else None
        neighbors = [(left, values[left]) if left is not None else None,
                     (right, values[right]) if right is not None else None]
        
        # Filtra vizinhos válidos
        neighbors = [n for n in neighbors if n is not None]
        
        # Encontra o melhor vizinho
        best_neighbor = max(neighbors, key=lambda n: n[1], default=None)
        
        # Verifica se há melhoria
        if best_neighbor is None or best_neighbor[1] <= values[current_pos]:
            break
        
        # Atualiza a posição atual
        current_pos = best_neighbor[0]
        path.append(current_pos)
    
    return path

pygame.display.set_caption("Subida de Encosta")

# Loop principal
running = True
while running:
    screen.fill(BG_COLOR)
    
    # Desenha as colunas
    for i, value in enumerate(values):
        x = i * COLUMN_WIDTH
        y = HEIGHT - value * (HEIGHT // MAX_HEIGHT)
        
        # Define a cor da coluna
        if not agent_started and i == start_pos:
            color = AGENT_COLOR  # A posição inicial do agente
        elif agent_started and not search_completed and step < len(path) and i == path[step]:
            color = AGENT_COLOR  # Coluna do agente em movimento
        elif search_completed and i == final_position:
            color = AGENT_COLOR  # Coluna final após a busca
        else:
            color = COLUMN_COLOR
        
        pygame.draw.rect(screen, color, (x, y, COLUMN_WIDTH - 2, value * (HEIGHT // MAX_HEIGHT)))
        
        # Exibe o texto "Máx local" na barra final
        if search_completed and i == final_position:
            label = font.render("Máx local", True, TEXT_COLOR)
            screen.blit(label, (x + COLUMN_WIDTH // 4, y - 70))
    
    # Mostra instruções ou informações
    if not agent_started:
        text = font.render("Pressione ESPAÇO", True, TEXT_COLOR)
    else:
        current_value = values[path[step]] if step < len(path) else values[path[-1]]
        text = font.render(f"Altura: {current_value}", True, TEXT_COLOR)
    screen.blit(text, (10, 10))
    
    pygame.display.flip()
    
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not agent_started:
            agent_started = True
            path = hill_climbing_max(values, start_pos)
            final_position = path[-1]  # Salva a posição final do agente
    
    # Atualiza o passo
    if agent_started and step < len(path):
        step += 1
        pygame.time.delay(800)
    elif agent_started and step >= len(path):
        search_completed = True  # Marca que a busca foi concluída

pygame.quit()
