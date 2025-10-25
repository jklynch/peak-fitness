#!/usr/bin/env python3
import sys
import pygame as pg

pg.init()
pg.font.init()
#each text is in its own rectangle
title_font = pg.font.SysFont('Comic Sans MS', 50)
title = title_font.render('Reach the peak!', True, (51, 0, 102))
# (0,0,0) is for black font
inst_font = pg.font.SysFont('Arial', 20)
inst1 = inst_font.render(f"Can you discover the most fit pentapeptide?", True, (96, 96, 96))
inst_font = pg.font.SysFont('Arial', 20)
inst2 = inst_font.render(f"Enter a starting sequence (5-mer) and get its fitness score.", True, (96, 96, 96))
inst_font = pg.font.SysFont('Arial', 20)
inst3 = inst_font.render(f"Improve the score to reach the peak!", True, (96, 96, 96))
inst4 = inst_font.render(f"You have 5 tries.", True, (96, 96, 96))


size = width, height = 640, 480
width = 640
height = 480
screen = pg.display.set_mode(size)
title_rect = title.get_rect(center=(width/2, height/2.2))
inst1_rect = inst1.get_rect(center=(width/2, height/1.7))
inst2_rect = inst2.get_rect(center=(width/2, height/1.6))
inst3_rect = inst3.get_rect(center=(width/2, height/1.5))
inst4_rect = inst4.get_rect(center=(width/2, height/1.4))

color = 204, 229, 255

# pg.display.set_caption("REACH THE PEAK!")

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()

    screen.fill(color)
    screen.blit(title, title_rect)
    screen.blit(inst1, inst1_rect)
    screen.blit(inst2, inst2_rect)
    screen.blit(inst3, inst3_rect)
    screen.blit(inst4, inst4_rect)
    pg.display.flip()
    
#Wait for Input --------------------------------------------------

def inputseqfunc():
    inputseq=''
    text1(f'Please enter a sequence of length {input_seq_length}', 300,400) #asks for seq
    pygame.display.flip()
    done = True
    for
