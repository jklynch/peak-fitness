#!/usr/bin/env python3
import sys
import pygame as pg

pg.init()
pg.font.init()
#each text is in its own rectangle
title_font = pg.font.SysFont('Arial', 40)
title = title_font.render('Reach the peak!', True, (0, 0, 0))
# (0,0,0) is for black font
inst_font = pg.font.SysFont('Arial', 20)
inst1 = inst_font.render(f"Can you figure out the most fit pentapeptide?", True, (0, 0, 0))
inst_font = pg.font.SysFont('Arial', 20)
inst2 = inst_font.render(f"Enter a starting sequence (5-mer) and get its fitness score.", True, (0, 0, 0))
inst_font = pg.font.SysFont('Arial', 20)
inst3 = inst_font.render(f"Try to improve the score to reach the peak!", True, (0, 0, 0))
inst4 = inst_font.render(f"You have 5 tries.", True, (0, 0, 0))

# defines elements to show on screen VVV ------------------------

size = width, height = 1280, 720
width = 1280
height = 720
screen = pg.display.set_mode(size)

#title_rect = title.get_rect(center=(width/2, height/2))
#inst1_rect = inst1.get_rect(center=(width/2, height/1.4))
#inst2_rect = inst2.get_rect(center=(width/2, height/1.5))
#inst3_rect = inst3.get_rect(center=(width/2, height/1.6))
#inst4_rect = inst4.get_rect(center=(width/2, height/1.7))
# -------------------------------------------------------------

#define a rectangle for plot
#plotrect1 = pg.draw.rect(screen, (0,0,255), [100,100,400,100],)

#ciricle1 = pg.draw.circle(plot_rectangle1, 10, (10,10), 10)


# ------------------------------------------------------------

color = 135, 206, 235

# pg.display.set_caption("REACH THE PEAK!")

# Defines elements ------------------------------------------------

plotheight = 500 #saved in a variable to futureproof y value formula in plot
plotwidth = 1180 #same as above
plotrect = pg.Surface((plotwidth,plotheight)) #creating plot bg
plotrect.fill((255,255,255)) #coloring plot bg

# ---------------------------

#simulating or adding all seq count here, TEMP!!! -------------------

#seqs_scores = {'AAA':0,'CCC':-1,'TTT':-2,'GGG':-3,'DDD':-4,'PPP':-5,'AAC':-6,'AGG':-7, 'GGC':-8, 'GAG':-9, 'AGE':-10, 'TAT':-11, 'TTA':-12}

import Peak #Also TEMP!!!
seqs_scores, peak_seq = Peak.main() #full list, not used later
seqs_scores_list = list(seqs_scores.keys())
# --------------------------------------------------------------------

# This is the part that has changed from the pygame_title script -----


xval = 0 #used for x value in plots
flowcontrolplot1 = 0 #used to make things happen ONCE in the loop

min_score_val = seqs_scores[min(seqs_scores, key=seqs_scores.get)] #finds lowest value in dictionary
max_score_val = seqs_scores[max(seqs_scores, key=seqs_scores.get)] #finds highest value in dictionary
min_index_val = 0
max_index_val = len(seqs_scores_list)

#Make Peak stand out !!!

while True:
	for event in pg.event.get():
		if event.type == pg.QUIT: sys.exit()

	screen.fill(color) #fills background with color
	
	screen.blit(plotrect, (50,50))
	for seq in seqs_scores:
		if flowcontrolplot1 == 0: # Prevents points being added forever
			yval = seqs_scores[seq] * -1/(max_score_val - min_score_val) * plotheight #converts count scores to the Y value in plot
			xval =  seqs_scores_list.index(seq) / (max_index_val - min_index_val) * plotwidth #converts sequence index to the X value in plot
			pg.draw.circle(plotrect, color=(0,0,0), center=(xval,yval), radius=3)
	flowcontrolplot1 = 1
	if flowcontrolplot1 == 1:
		pg.draw.circle(plotrect, color=(0,0,0), center=(seqs_scores_list.index(peak_seq),max_score_val), radius=3)
		flowcontrolplot1 = 2
	pg.display.flip() # Accumulates and renders ALL elements
	
