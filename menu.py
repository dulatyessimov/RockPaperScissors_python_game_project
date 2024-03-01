import pygame
import sys
import subprocess

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Menu")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.Font(None, 40)

# Function to display text
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Main Menu function
def main_menu():
    while True:
        screen.fill(WHITE)
        draw_text("Main Menu", font, BLACK, screen, WIDTH // 2, HEIGHT // 4)

        # Play with computer button
        play_computer_button = pygame.Rect(WIDTH // 4, HEIGHT // 2, WIDTH // 2, 50)
        pygame.draw.rect(screen, RED, play_computer_button)
        draw_text("Play with computer", font, BLACK, screen, WIDTH // 2, HEIGHT // 2)

        # Play 2 player button
        play_2_player_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 + 60, WIDTH // 2, 50)
        pygame.draw.rect(screen, RED, play_2_player_button)
        draw_text("Play 2 player", font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 60)

        # Quit button
        quit_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 + 120, WIDTH // 2, 50)
        pygame.draw.rect(screen, RED, quit_button)
        draw_text("Quit", font, BLACK, screen, WIDTH // 2, HEIGHT // 2 + 120)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if play_computer_button.collidepoint(mouse_pos):
                    subprocess.Popen(["python", "scissor_paper_rock.py"])
                    pygame.quit()  # Close Pygame window
                    sys.exit()
                elif play_2_player_button.collidepoint(mouse_pos):
                    subprocess.Popen(["python", "scissor_paper_rock_duo.py"])

                    pygame.quit()  # Close Pygame window
                    sys.exit()
                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# Run the main menu
if __name__ == "__main__":
    main_menu()
