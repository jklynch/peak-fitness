#!/usr/bin/env python3
PYGAME_DETECT_AVX2=1
import pygame, sys, pyfiglet, random
import count_seq, peak_seq
from Bio.Align import substitution_matrices

pygame.init()
pygame.font.init()
# Screen setup
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Peak fitness")

# Fonts and colors
font = pygame.font.SysFont('Arial', 60)
small_font = pygame.font.SysFont('Arial', 20)
medium_font = pygame.font.SysFont('Arial', 30)
medium_font.set_bold(True)
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


#ADD ONLY THINGS YOU WANT ON THE START SCREEN. WE CAN MAKE THIS VIBIER LATER? 
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
        
        #adding instructions to be printed
        self.subtitle_lines = [
            "Can you discover the most fit pentapeptide?",
            "Enter a starting sequence (5-mer)",
            "and get its fitness score.",
            "Improve the score to reach the peak!",
            "You have 5 tries.",
            ]

        # Render it onto a Pygame surface (we’ll convert ASCII text to a surface)
        self.figlet_surface = self.render_figlet_surface(self.figlet_text)
    
    #making a figlet surface for peaks
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
    #handle inputs for this screen. only type of input will be a mouse click.
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                self.manager.set_screen(GameScreen(self.manager, []))

    #putting things on the screen
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


#This is where we take the input sequence. It accounts for if the characters entered are amino acids.
# -------------------------------
# Game Screen (takes one input)
# -------------------------------
class GameScreen(Screen):
    #what's in this type of screen
    def __init__(self, manager, inputs):
        self.manager = manager
        self.input_box = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 200, 200, 50)
        self.active = False
        self.user_text = ""
        self.inputs = inputs
        self.MAX_COUNT = 5
        
    #handling inputs for input. Also takes in only amino acid sequences - automatically makes them uppercase
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.input_box.collidepoint(event.pos)

        if event.type == pygame.KEYDOWN and self.active:
            valid_amino_acids = set("ACDEFGHIKLMNPQRSTVWY")
            if event.key == pygame.K_RETURN:
                # Only take one input, must be exactly 5 alphabets
                if len(self.user_text) == 5 and all(c in valid_amino_acids for c in self.user_text.upper()):
                    self.inputs.append(self.user_text.upper())
                    self.manager.set_screen(ResultScreen(self.manager, self.inputs))
            #backspaces
            elif event.key == pygame.K_BACKSPACE:
                self.user_text = self.user_text[:-1]
            elif len(self.user_text) < 5 and event.unicode.upper() in valid_amino_acids:
                self.user_text += event.unicode
    #show stuff on screen
    def draw(self, surface):
        #background color
        surface.fill(white)
        #active is if mouse clicks within the box for input
        color = blue if self.active else gray
        pygame.draw.rect(surface, color, self.input_box, border_radius=10)
        
        #amino acid image
        og_image = pygame.image.load("amino acid chart.png").convert_alpha() 
        smaller_image = pygame.transform.scale(og_image, (600, 450))

        # Get the image's rectangle and position it
        image_rect = smaller_image.get_rect()
        image_rect.center = (WIDTH // 2, HEIGHT // 2.7)

        screen.blit(smaller_image, image_rect)

        #fonts for the label for the input box
        label_text = small_font.render("Type in sequence", True, black)
        label_x = self.input_box.centerx - label_text.get_width() // 2
        label_y = self.input_box.top - 50
        surface.blit(label_text, (label_x, label_y))

        # Draw box to enter onto screen
        txt_surface = small_font.render(self.user_text.upper(), True, black)
        # surface.blit(txt_surface, (self.input_box.x + 20, self.input_box.y + 10))
        surface.blit(txt_surface, (self.input_box.centerx - txt_surface.get_width()//2,
                                    self.input_box.centery - txt_surface.get_height()//2))

        # Display count info (how many tries are left)
        count = len(self.inputs)
        count_text = small_font.render(f"Try {count + 1} of {self.MAX_COUNT}", True, black)
        surface.blit(count_text, (50, 50))


#Add stuff here for visualization in result page- LIKE GRAPHS.
# -------------------------------
# Result Screen (after each input)
# -------------------------------
class ResultScreen(Screen):
    #what's on the result screen? if you're including graphs, include the variable here because it needs to exist here!!
    def __init__(self, manager, inputs):
        self.manager = manager
        self.inputs = inputs
        self.button_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT - 150, 200, 80)
        
        #getting input from previous screen
        if inputs:
            peak = self.manager.peak
            self.last_input = inputs[-1]
            self.score = count_seq.count_score(peak, self.last_input)
            print(peak) #this is just for checking the peak_seq function
        else:
            self.last_input = ""
            self.result1 = 0
            self.result2 = 0

    #type of input- currently just have a next button but we can change that
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                # If less than 3 inputs, go back to Game Screen
                if len(self.inputs) < 5:
                    self.manager.set_screen(GameScreen(self.manager, self.inputs))
                else:
                    #score
                    #visualize result
                    # won = total_result == 0  negative sum = lose?
                    #self.manager.set_screen(GameOverScreen(self.manager, won))
                    #lost= total_result ==None
                    pass
    
    #drawing stuff to surface- for now it just shows you the string input and score. We need to add the plotting script!               
    def draw(self, surface):
        surface.fill(white)
        title = font.render("Traverse the Peak", True, black)
        surface.blit(title, (WIDTH//2 - title.get_width()//2, 80))
        score = medium_font.render(f'Score: {self.score}', True, blue)
        surface.blit(score, (20, 40))

        y = 220
        for i, text in enumerate(self.inputs):
            line = small_font.render(f"Input {i+1}: {text}", True, black)
            surface.blit(line, (WIDTH//2 - line.get_width()//2, y))
            y += 70

        # Draw Next button unless finished
        if len(self.inputs) < 5:
            pygame.draw.rect(surface, blue, self.button_rect, border_radius=10)
            btn_text = small_font.render("Next", True, white)
            surface.blit(btn_text, (
                self.button_rect.centerx - btn_text.get_width() // 2,
                self.button_rect.centery - btn_text.get_height() // 2
            ))

# -------------------------------
# Result Screen (After attempt Number 5)
# -------------------------------
class Result_5_Screen(Screen):
    #what's on the result screen? if you're including graphs, include the variable here because it needs to exist here!!
    def __init__(self, manager, inputs):
        self.manager = manager
        self.inputs = inputs
        self.button_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT - 150, 200, 80)
        
        #getting input from previous screen
        if inputs:
            peak = self.manager.peak
            self.last_input = inputs[-1]
            self.score = count_seq.count_score(peak, self.last_input)
            # print(peak) #this is just for checking the peak_seq function
        else:
            self.last_input = ""
            self.result1 = 0
            self.result2 = 0

    #type of input- currently just have a next button but we can change that
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                # If less than 3 inputs, go back to Game Screen
                if len(self.inputs) < 5:
                    self.manager.set_screen(GameScreen(self.manager, self.inputs))
                else:
                    #score
                    #visualize result
                    # won = total_result == 0  negative sum = lose?
                    self.manager.set_screen(GameOverScreen(self.manager, won))
                    #lost= total_result ==None
                    # pass
    
    #drawing stuff to surface- for now it just shows you the string input and score. We need to add the plotting script!               
    def draw(self, surface):
        surface.fill(white)
        title = font.render("Traverse the Peak", True, black)
        surface.blit(title, (WIDTH//2 - title.get_width()//2, 80))
        score = medium_font.render(f'Score: {self.score}', True, blue)
        surface.blit(score, (20, 40))

        y = 220
        for i, text in enumerate(self.inputs):
            line = small_font.render(f"Input {i+1}: {text}", True, black)
            surface.blit(line, (WIDTH//2 - line.get_width()//2, y))
            y += 70

        # Draw Next button unless finished
        if len(self.inputs) == 5:
            end_text = small_font.render("Click to see final result", True, blue)
            surface.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, HEIGHT - 130))
        else:
            pass

#--------------------------------
# Game over screen class
#--------------------------------
class GameOverScreen(Screen):
    def __init__(self, manager, inputs):
        self.manager = manager
        self.inputs = inputs
        
        #getting input from previous screen
        if inputs:
            peak = self.manager.peak
            self.last_input = inputs[-1]
            self.score = count_seq.count_score(peak, self.last_input)
            # print(peak) - this is just for checking the peak_seq function
        else:
            self.last_input = ""
            self.result1 = 0
            self.result2 = 0

    #type of input- currently just have a next button but we can change that
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                if self.score is not None:
                    score_text = medium_font.render(f"You won in {len(self.imputs)} tries", True, blue)
                    score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
                    screen.blit(score_text, score_rect)

            if self.score is None:
                score_text = medium_font.render(f"Better luck next time!", True, blue)
                score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
                screen.blit(score_text, score_rect)

    def draw(self, surface):
        surface.fill(white)
        title = font.render("Traverse the Peak", True, black)
        surface.blit(title, (WIDTH//2 - title.get_width()//2, 80))
        score = medium_font.render(f'Score: {self.score}', True, blue)
        surface.blit(score, (20, 40))
        small_font.render("Click to see final result", True, blue)
        # surface.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, HEIGHT - 130))

# -------------------------------
# Screen Manager
# -------------------------------
class ScreenManager:
    def __init__(self):
        self.current_screen = StartScreen(self)
        # select random peptide using peak_seq function from peak_seq.py
        self.peak = peak_seq.peak_seq(5)

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
