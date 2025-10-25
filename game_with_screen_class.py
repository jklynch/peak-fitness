#!/usr/bin/env python3
PYGAME_DETECT_AVX2=1
import pygame
import sys
import pyfiglet

pygame.init()
pygame.font.init()
# Screen setup
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Peak fitness")

# Fonts and colors
font = pygame.font.SysFont('Arial', 60)
small_font = pygame.font.SysFont('Arial', 20)
button_font=pygame.font.Font(None,20)
button_font.set_bold(True)
MONO_FONT = pygame.font.SysFont("Courier New", 24)
MONO_FONT.set_bold(True)
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)
blue = (80, 140, 255)
green= (0, 128, 0)


clock = pygame.time.Clock()


# -------------------------------
# Base Screen Class
# -------------------------------
class Screen:
    def handle_event(self, event):
        pass
    def update(self):
        pass
    def draw(self, surface):
        pass


# -------------------------------
# Start Screen
# -------------------------------
class StartScreen(Screen):
    #What is in the screen: initialize variables specific to start screen
    def __init__(self, manager):
        self.manager = manager
        self.button_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 200, 200, 30)
        
        # Create a Figlet title using pyfiglet
        self.figlet_font = pyfiglet.Figlet(font="ticks")  # You can try fonts like 'doom', 'banner3-D', etc.
        self.figlet_text = self.figlet_font.renderText("peak")
        
        #adding instructions
        self.subtitle_lines = [
            "Can you discover the most fit pentapeptide?",
            "Enter a starting sequence (5-mer)",
            "and get its fitness score.",
            "Improve the score to reach the peak!",
            "You have 5 tries.",
            ]

        # Render it onto a Pygame surface (we’ll convert ASCII text to a surface)
        self.figlet_surface = self.render_figlet_surface(self.figlet_text)
    
    def render_figlet_surface(self, ascii_text):
        """Convert ASCII figlet text into a pygame surface."""
        lines = ascii_text.split("\n")
        line_surfaces = [MONO_FONT.render(line, True, blue) for line in lines]
        width = max(line.get_width() for line in line_surfaces)
        height = len(line_surfaces) * MONO_FONT.get_height()
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        y = 0
        for line in line_surfaces:
            surface.blit(line, (0, y))
            y += MONO_FONT.get_height()
        return surface

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                self.manager.set_screen(GameScreen(self.manager, []))

    def draw(self, surface):
        surface.fill(white)
        #draw figlet surface here in the center
        surface.blit(
            self.figlet_surface,
            (WIDTH//2 - self.figlet_surface.get_width()//2, HEIGHT//4 - self.figlet_surface.get_height()//2)
        )
        
        #print instructions
        y = HEIGHT // 2
        for line in self.subtitle_lines:
            txt = small_font.render(line, True, black)
            surface.blit(txt, (WIDTH // 2 - txt.get_width() // 2, y))
            y += 50
        
        #draw next button to screen at the bottom
        pygame.draw.rect(surface, green, self.button_rect, border_radius=10)
        btn_text = button_font.render("Begin", True, white)
        surface.blit(btn_text, (self.button_rect.centerx - btn_text.get_width()//2,
                                self.button_rect.centery - btn_text.get_height()//2))


# -------------------------------
# Game Screen (takes one input)
# -------------------------------
class GameScreen(Screen):
    def __init__(self, manager, inputs):
        self.manager = manager
        self.input_box = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 200, 200, 50)
        self.active = False
        self.user_text = ""
        self.inputs = inputs
        self.MAX_COUNT = 3

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.input_box.collidepoint(event.pos)

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                # Only take one input, must be exactly 5 alphabets
                if len(self.user_text) == 5 and self.user_text.isalpha():
                    self.inputs.append(self.user_text.upper())
                    self.manager.set_screen(ResultScreen(self.manager, self.inputs))
            elif event.key == pygame.K_BACKSPACE:
                self.user_text = self.user_text[:-1]
            elif len(self.user_text) < 5 and event.unicode.isalpha():
                self.user_text += event.unicode

    def draw(self, surface):
        surface.fill(white)
        color = blue if self.active else gray
        pygame.draw.rect(surface, color, self.input_box, border_radius=10)

        #print type in sequence above box
        label_text = small_font.render("Type in sequence", True, black)
        label_x = self.input_box.centerx - label_text.get_width() // 2
        label_y = self.input_box.top - 50
        surface.blit(label_text, (label_x, label_y))

        # Draw current text
        txt_surface = small_font.render(self.user_text.upper(), True, black)
        # surface.blit(txt_surface, (self.input_box.x + 20, self.input_box.y + 10))
        surface.blit(txt_surface, (self.input_box.centerx - txt_surface.get_width()//2,
                                    self.input_box.centery - txt_surface.get_height()//2))

        # Display count info
        count = len(self.inputs)
        count_text = small_font.render(f"Try {count + 1} of {self.MAX_COUNT}", True, black)
        surface.blit(count_text, (50, 50))


# -------------------------------
# Result Screen (after each input)
# -------------------------------
class ResultScreen(Screen):
    def __init__(self, manager, inputs):
        self.manager = manager
        self.inputs = inputs
        self.button_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT - 150, 200, 80)


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                # If less than 3 inputs, go back to Game Screen
                if len(self.inputs) < 3:
                    self.manager.set_screen(GameScreen(self.manager, self.inputs))
                else:
                    # End of game – show final results (stay here)
                    pass

    def draw(self, surface):
        surface.fill(white)
        title = font.render("Result Screen", True, black)
        surface.blit(title, (WIDTH//2 - title.get_width()//2, 80))

        y = 220
        for i, text in enumerate(self.inputs):
            line = small_font.render(f"Input {i+1}: {text}", True, black)
            surface.blit(line, (WIDTH//2 - line.get_width()//2, y))
            y += 70

        # Draw Next button unless finished
        if len(self.inputs) < 3:
            pygame.draw.rect(surface, blue, self.button_rect, border_radius=10)
            btn_text = small_font.render("Next", True, white)
            surface.blit(btn_text, (self.button_rect.centerx - btn_text.get_width()//2,
                                    self.button_rect.centery - btn_text.get_height()//2))
        else:
            done_text = small_font.render("All 3 inputs completed!", True, blue)
            surface.blit(done_text, (WIDTH//2 - done_text.get_width()//2, HEIGHT - 130))


# -------------------------------
# Screen Manager
# -------------------------------
class ScreenManager:
    def __init__(self):
        self.current_screen = StartScreen(self)

    def set_screen(self, screen):
        self.current_screen = screen

    def handle_event(self, event):
        self.current_screen.handle_event(event)

    def update(self):
        if hasattr(self.current_screen, "update"):
            self.current_screen.update()

    def draw(self, surface):
        self.current_screen.draw(surface)


# -------------------------------
# Main Loop
# -------------------------------
def main():
    manager = ScreenManager()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            manager.handle_event(event)

        manager.update()
        manager.draw(screen)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
