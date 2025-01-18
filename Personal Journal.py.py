import pygame

# Inicialização do Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Alchemy Game")

# Cores
TEXT_COL = (255, 255, 255)
HIGHLIGHT_COL = (255, 215, 0)

# Fontes
font_title = pygame.font.SysFont("timesnewroman", 64)
font_menu = pygame.font.SysFont("timesnewroman", 40)

# Opções do menu
menu_options = ["New Game", "Options", "Volume", "Credits"]
selected_option = 0

def draw_text(text, font, text_col, x, y):
    """Renderiza e desenha texto na tela."""
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def render_menu(selected_option):
    """Desenha o menu na tela."""
    screen.fill((0, 0, 0))  # Fundo preto
    draw_text("MENU", font_title, TEXT_COL, 300, 100)

    # Desenhar opções do menu
    for i, option in enumerate(menu_options):
        color = HIGHLIGHT_COL if i == selected_option else TEXT_COL
        draw_text(option, font_menu, color, 320, 200 + i * 50)

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(menu_options)
            if event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(menu_options)
            if event.key == pygame.K_RETURN:
                print(f"Você selecionou: {menu_options[selected_option]}")

    # Renderizar o menu
    render_menu(selected_option)

    # Atualizar a tela
    pygame.display.update()

# Encerrar o Pygame
pygame.quit()
