#!/usr/bin/env python3

#Oct 25, 2025 Vivian Li
##takes the count and if count is None (lost), the better ending screen is different than
##if the count is an integer between 1-5

import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame End Screen")

# Colors
BLUE = (135, 206, 237)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fonts
font_large = pygame.font.SysFont("Arial", 72)
font_medium = pygame.font.SysFont("Arial", 36)

##enter how many tries it took for user to win aka count
def display_end_screen(message, count=None):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Press space to restart or quit
                    running = False  # Exit end screen loop

        screen.fill(BLACK)  # Fill background with black

        # Render main message
        text_surface = font_large.render(message, True, WHITE)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(text_surface, text_rect)

        # Render count (if provided)
        if coun_rect is not None:
            coun_rect_text = font_medium.render(f"You won in {coun_rect} tries", True, BLUE)
            coun_rect_rect = coun_rect_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
            screen.blit(coun_rect_text, coun_rect_rect)

        if coun_rect is None:
            coun_rect_text = font_medium.render(f"Better luck next time!", True, BLUE)
            coun_rect_rect = coun_rect_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
            screen.blit(coun_rect_text, coun_rect_rect)


        # Render instruction text
        instruction_text = font_medium.render("Press SPACE to restart or quit", True, BLUE)
        instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        screen.blit(instruction_text, instruction_rect)

        pygame.display.flip()  # Update the display

# Example usage:
# Simulate game over after some time
#pygame.time.wait(2000)  # Wait for 2 seconds
display_end_screen("GAME OVER!", coun_rect=3)

# After the end screen, you could potentially restart the game or quit
# For this example, we'll just quit after the end screen loop finishes
pygame.quit()
sys.exit()
