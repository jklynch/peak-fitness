#!/usr/bin/env python3
import sys
import pygame as pg
import count_seq
from Bio.Align import substitution_matrices

#initialize pygame
pg.init()
pg.font.init()

#fonts
title_font = pg.font.SysFont('Comic Sans MS',60)
inst_font = pg.font.SysFont('Arial', 20)
seq_font = pg.font.SysFont('Arial', 30)

#asks for seq
text1 = seq_font.render(f'Type your sequence:', True, (51, 0, 102)) 
instructions = [
    "Can you discovery the most fit pentapeptide?",
    "Enter a starting sequence (5-mer)",
    "and get its fitness score.",
    "Improve the score to reach the peak!",
    "You have 5 tries."
]
#this function takes the lines above and then center aligns the text
def draw_centered_text(screen, lines, font, color, start_y, line_spacing=10):
    total_height = sum(font.size(line)[1] + line_spacing for line in lines) - line_spacing
    y = start_y - total_height  # start so that all lines are vertically centered around start_y
    for line in lines:
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(center=(screen.get_width() // 2, y + font.get_height() // 2))
        screen.blit(text_surface, text_rect)
        y += font.get_height() + line_spacing

#set display
size = width, height = 1280, 720
width = 1280
height = 720
screen = pg.display.set_mode(size)
title = title_font.render('Reach the peak!', True, (51, 0, 102))
title_rect = title.get_rect(center=(width/2, height/3.2))
text1_rect = text1.get_rect(center=(width/4, height/1.3))

color = 204, 229, 255
inputseq = ''

# Game state
state = "input"
inputseq = ''
score = None
peak = 'AAAAA'
matrix = substitution_matrices.load('BLOSUM62')
amino_acids='A C D E F G H I K L M N P Q R S T V W Y'
set_AA=set(amino_acids.split(' '))

running = True
submitted = False

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            running = False
        elif event.type == pg.KEYDOWN: #this records the keystrokes
            if event.key == pg.K_ESCAPE:
                running = False
            if state == "input":
                if event.key == pg.K_BACKSPACE:
                    inputseq = inputseq[:-1]
                elif event.key == pg.K_RETURN:  # Handle Enter key
                    if len(inputseq) == 5 and set(inputseq.upper()).issubset(set_AA):
                        submitted = True
                        input_score = count_seq.count_score(peak, inputseq)
                        state = "score"
                    else:
                        print(f'Sequence must be exactly 5 naturally occuring amino acids!')
                else:
            # Only add character if input is less than 5
                    if len(inputseq) < 5:
                        inputseq += event.unicode
                        print(f"Sequence submitted: {inputseq}")

    screen.fill(color)

    if state == "input":
        screen.blit(title, title_rect)
        draw_centered_text(screen, instructions, inst_font, (96, 96, 96), 450, line_spacing=10)
        screen.blit(text1, text1_rect)
        seq = seq_font.render(inputseq, True, (51, 0, 102))
        seq_rect = text1.get_rect(center=(width/2, height/1.3))
        screen.blit(seq, seq_rect)

    elif state == "score":
        # Display sequence and score
        seq_surface = seq_font.render(f"Your sequence: {inputseq.upper()}", True, (51,0,102))
        screen.blit(seq_surface, (20, 20))

        score_surface = seq_font.render(f"Score: {input_score}", True, (255, 0, 0))
        screen.blit(score_surface, (20, 60))

        hint_surface = inst_font.render("Press ESC to quit.", True, (51,0,102))
        screen.blit(hint_surface, (20, 100))

    pg.display.flip()

   