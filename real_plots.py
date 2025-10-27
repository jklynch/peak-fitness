#!/usr/bin/env python3
import sys
import pygame as pg
import activity_and_score_seq
import call_act_and_score_v2


plotheight = 500 #saved in a variable to futureproof y value formula in plot
plotwidth = 1180 #same as above
plotrect = pg.Surface((plotwidth,plotheight)) #creating plot bg
plotrect.fill((255,255,255)) #coloring plot bg

# --------------------------------------------------------------------
seqs= activity_and_score_seq.score_act_dict()
yvalues = list(map(lambda x:x[0][1], seqs.values()))
max_value = max(yvalues)
min_value = max(yvalues)
peak_seq = max(seqs.items(), key= lambda item: item[0][1])


while True:
	for event in pg.event.get():
		if event.type == pg.QUIT: sys.exit()
	
	screen.fill(color) #fills background with color
	screen.blit(plotrect, (50,50))
	#populate the graph with all existing seqs
	for seq in seqs:
		score_x, score_y = call_act_and_score_v2.main(seq)
		yval = score_y/(max_value-min_value) * plotheight #converts count scores to the Y value in plot
		xval = score_x/ (max_value-min_value) * plotwidth #converts sequence index to the X value in plot
		pg.draw.circle(plotrect, color=(0,0,0), center=(xval,yval), radius=3)
	#plot the input seq and check to make sure it's not the peak seq, if it is, it is also plotted
	for seq in self.inputs:
		if seq == peak:
			pg.draw.circle(plotrect, color=(255,0,0), center=(xval,yval+20), radius=10)
		else:
			score_x, score_y = call_act_and_score_v2(seq)
			pg.draw.circle(plotrect, color=(0,0,0), center=(xval,yval), radius=3)