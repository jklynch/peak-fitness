#!/usr/bin/env python3
import sys
import pygame as pg

#initialize pygame
pg.init()
pg.font.init()
done = False
#add the welcome message, note - 
#each text is in its own rectangle - we couldn't figure out how to do line breaks or center alignment
# (0,0,0) is for black font
# font for all of the instructions

title_font = pg.font.SysFont('Comic Sans MS',60)
inst_font = pg.font.SysFont('Arial', 20)
seq_font = pg.font.SysFont('Arial', 30)
title = title_font.render('Reach the peak!', True, (51, 0, 102))
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

title_rect = title.get_rect(center=(width/2, height/3.2))
text1_rect = text1.get_rect(center=(width/4, height/1.3))

color = 204, 229, 255
inputseq = ''

# #Wait for Input --------------------------------------------------

while not done:
    #this is an infinite loop... until player types quit
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            done = True
        if event.type == pg.KEYDOWN: #this records the keystrokes
            if event.key == pg.K_BACKSPACE:
                #handle backspace
                inputseq = inputseq[:-1]
            elif event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
            elif event.key == pg.K_RETURN:  # Handle Enter key
                print(f"Sequence submitted: {inputseq}")
                submitted_text = inputseq  # store the submitted string
                inputseq = ""
            else: #this adds a chracter to the inputseq
                inputseq += event.unicode

    screen.fill(color)
    screen.blit(title, title_rect)
    draw_centered_text(screen, instructions, inst_font, (96, 96, 96), 450, line_spacing=10)
    screen.blit(text1, text1_rect)
    seq = seq_font.render(inputseq, True, (51, 0, 102))
    seq_rect = text1.get_rect(center=(width/2, height/1.3))
    screen.blit(seq, seq_rect)
    pg.display.flip()

#Push input sequence to top corner along with attempts
