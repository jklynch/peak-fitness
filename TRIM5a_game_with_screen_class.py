#!/usr/bin/env python3
PYGAME_DETECT_AVX2=1
import pygame, sys, pyfiglet, random, activity_and_score_seq, math
from Bio.Align import substitution_matrices

pygame.init()
pygame.font.init()
pygame.mixer.init()

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
credits_font=pygame.font.SysFont('Calibri',25)
tiny_font=pygame.font.SysFont('Arial',10)
MONO_FONT = pygame.font.SysFont("Courier New", 24)
MONO_FONT.set_bold(True)
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)
blue = (80, 140, 255)
green = (0, 128, 0)
dark_orchid = (153,50,204)
pinky= (255,204,229)
light_green=(153,255,51)
red=(255, 0, 0)
gold=(255,215,0)

clock = pygame.time.Clock()

#BEWARE !!!!
#Full dictionary TRIM5
dictionary = {'GERGTRYQTFVNF': [[0.0, 21.2]], 'GAPSTRYQTFVNF': [[-3.0, 18.821]], 'GARGTAYQTFVNF': [[-2.0, 14.167]], 'GARGTGYQTFVNF': [[-3.0, 13.0]], 'GAPGTPYQTFVNF': [[-5.0, 11.25]], 'GAEGPRYQTFVNF': [[-2.0, 11.0]], 'GAPGLRYQTFVNF': [[-4.0, 10.667]], 'GTRGTSYQTFVNF': [[-2.0, 10.167]], 'GARGDRYQTFVNF': [[-2.0, 9.5]], 'GAPGMRYQTFVNF': [[-4.0, 8.75]], 'GARGTEYQTFVNF': [[-1.0, 8.0]], 'GAPGTRYQTFVNF': [[-3.0, 7.75]], 'GAPKTRYQTFVNF': [[-5.0, 7.75]], 'GAAWTRYQTFVNF': [[-4.0, 7.5]], 'GTRGTHYQTFVNF': [[-1.0, 7.5]], 'GAEGTKYQTFVNF': [[1.0, 7.083]], 'GARRTKYQTFVNF': [[-1.0, 7.0]], 'GAWGKRYQTFVNF': [[-5.0, 7.0]], 'GARVTKYQTFVNF': [[-2.0, 6.75]], 'GARETRYQTFVNF': [[-3.0, 6.5]], 'GARGTDYQTFVNF': [[-3.0, 6.5]], 'GARWTEYQTFVNF': [[-3.0, 6.25]], 'GARGTCYQTFVNF': [[-4.0, 6.0]], 'GAWGTSYQTFVNF': [[-5.0, 6.0]], 'GARGTLYQTFVNF': [[-3.0, 6.0]], 'GEEGTRYQTFVNF': [[0.0, 5.833]], 'GARGTKYQTFVNF': [[1.0, 5.75]], 'GAGGKRYQTFVNF': [[-4.0, 5.75]], 'GAPGPRYQTFVNF': [[-4.0, 5.688]], 'GARWTRYQTFVNF': [[-3.0, 5.65]], 'GAREPRYQTFVNF': [[-4.0, 5.625]], 'GTYGTRYQTFVNF': [[-3.0, 5.583]], 'GTRSTRYQTFVNF': [[-1.0, 5.5]], 'GARGTWYQTFVNF': [[-4.0, 5.5]], 'GAAGTRYQTFVNF': [[-2.0, 5.5]], 'GDQGTRYQTFVNF': [[3.0, 5.423]], 'GAMGTRYQTFVNF': [[-2.0, 5.29]], 'GARGTVYQTFVNF': [[-4.0, 5.25]], 'GARHTRYQTFVNF': [[-3.0, 5.219]], 'GERETRYQTFVNF': [[-2.0, 5.125]], 'GAWGTRYQTFVNF': [[-4.0, 5.1]], 'GDRGTRYQTFVNF': [[2.0, 5.0]], 'GACGTSYQTFVNF': [[-5.0, 5.0]], 'GAGRTRYQTFVNF': [[-5.0, 5.0]], 'GARGTRYQTFVNF': [[-1.0, 5.0]], 'GTTGTRYQTFVNF': [[-2.0, 4.875]], 'GAEGTRYQTFVNF': [[-1.0, 4.8]], 'GARGTPYQTFVNF': [[-3.0, 4.75]], 'GAPGTDYQTFVNF': [[-5.0, 4.65]], 'GTRGTLYQTFVNF': [[-3.0, 4.625]], 'GTEGTRYQTFVNF': [[-1.0, 4.536]], 'GTRGTEYQTFVNF': [[-1.0, 4.52]], 'GARGTSYQTFVNF': [[-2.0, 4.5]], 'GACGTRYQTFVNF': [[-4.0, 4.5]], 'GERRTRYQTFVNF': [[-2.0, 4.5]], 'GAPLTRYQTFVNF': [[-7.0, 4.5]], 'GARVTRYQTFVNF': [[-4.0, 4.278]], 'GARGPLYQTFVNF': [[-4.0, 4.25]], 'GAGGTRYQTFVNF': [[-3.0, 4.167]], 'GGGGTRYQTFVNF': [[-4.0, 4.167]], 'GAPGTNYQTFVNF': [[-3.0, 4.125]], 'GARDTRYQTFVNF': [[-2.0, 4.069]], 'GAQGTRYQTFVNF': [[0.0, 4.0]], 'GAGGTKYQTFVNF': [[-1.0, 4.0]], 'GARGTQYQTFVNF': [[0.0, 4.0]], 'GARGKRYQTFVNF': [[-2.0, 4.0]], 'GAQETRYQTFVNF': [[-2.0, 4.0]], 'GARETGYQTFVNF': [[-5.0, 4.0]], 'GAEWTRYQTFVNF': [[-3.0, 4.0]], 'GALGTRYQTFVNF': [[-3.0, 4.0]], 'GTDGTRYQTFVNF': [[-3.0, 3.975]], 'GAYGTRYQTFVNF': [[-3.0, 3.904]], 'GAVGTRYQTFVNF': [[-4.0, 3.875]], 'GTMGTRYQTFVNF': [[-2.0, 3.839]], 'GTRGTAYQTFVNF': [[-2.0, 3.836]], 'GTRGTGYQTFVNF': [[-3.0, 3.836]], 'GERGTEYQTFVNF': [[0.0, 3.833]], 'GERGTSYQTFVNF': [[-1.0, 3.833]], 'GTFGTRYQTFVNF': [[-4.0, 3.803]], 'GACGKRYQTFVNF': [[-5.0, 3.75]], 'GARWTGYQTFVNF': [[-5.0, 3.75]], 'GARGPEYQTFVNF': [[-2.0, 3.75]], 'GAREKRYQTFVNF': [[-4.0, 3.75]], 'GTRGTMYQTFVNF': [[-2.0, 3.7]], 'GTPGTRYQTFVNF': [[-3.0, 3.698]], 'GADGTRYQTFVNF': [[-3.0, 3.5]], 'GAHGTRYQTFVNF': [[-1.0, 3.5]], 'GACWTRYQTFVNF': [[-6.0, 3.5]], 'GAVWTRYQTFVNF': [[-6.0, 3.5]], 'GARGGRYQTFVNF': [[-3.0, 3.5]], 'GERGKRYQTFVNF': [[-1.0, 3.5]], 'GAHGTSYQTFVNF': [[-2.0, 3.5]], 'GAEETRYQTFVNF': [[-3.0, 3.5]], 'GAVGKRYQTFVNF': [[-5.0, 3.5]], 'GARGTNYQTFVNF': [[-1.0, 3.45]], 'GARGTHYQTFVNF': [[-1.0, 3.429]], 'GTRGTWYQTFVNF': [[-4.0, 3.403]], 'GTCGTRYQTFVNF': [[-4.0, 3.36]], 'GGRGTRYQTFVNF': [[-2.0, 3.357]], 'GTVGTRYQTFVNF': [[-4.0, 3.255]], 'GAPGKRYQTFVNF': [[-4.0, 3.25]], 'GAVGTSYQTFVNF': [[-5.0, 3.25]], 'GERGTGYQTFVNF': [[-2.0, 3.25]], 'GGRGKRYQTFVNF': [[-3.0, 3.25]], 'GARWTVYQTFVNF': [[-6.0, 3.25]], 'GASGTRYQTFVNF': [[-2.0, 3.167]], 'GTRGTCYQTFVNF': [[-4.0, 3.15]], 'GTWGTRYQTFVNF': [[-4.0, 3.144]], 'GATGTRYQTFVNF': [[-2.0, 3.132]], 'GTRGTPYQTFVNF': [[-3.0, 3.083]], 'GAIGTRYQTFVNF': [[-4.0, 3.068]], 'GARGTTYQTFVNF': [[-2.0, 3.04]], 'GTRETRYQTFVNF': [[-3.0, 3.035]], 'GTRDTRYQTFVNF': [[-2.0, 3.0]], 'GARATRYQTFVNF': [[-1.0, 3.0]], 'GARGPIYQTFVNF': [[-5.0, 3.0]], 'GADGKRYQTFVNF': [[-4.0, 3.0]], 'GASGTSYQTFVNF': [[-3.0, 3.0]], 'GGRGGRYQTFVNF': [[-4.0, 3.0]], 'GATRTRYQTFVNF': [[-4.0, 3.0]], 'GTRGTDYQTFVNF': [[-3.0, 2.979]], 'GAQGTLYQTFVNF': [[-2.0, 2.975]], 'GTQGTRYQTFVNF': [[0.0, 2.969]], 'GTRGTYYQTFVNF': [[-3.0, 2.958]], 'GAPGTIYQTFVNF': [[-6.0, 2.917]], 'GTRGTQYQTFVNF': [[0.0, 2.889]], 'GAPGTHYQTFVNF': [[-3.0, 2.875]], 'GAGGPRYQTFVNF': [[-4.0, 2.833]], 'GAPDTRYQTFVNF': [[-4.0, 2.833]], 'GGRWTRYQTFVNF': [[-4.0, 2.8]], 'GTAGTRYQTFVNF': [[-2.0, 2.792]], 'GARGPDYQTFVNF': [[-4.0, 2.75]], 'GARGTMYQTFVNF': [[-2.0, 2.75]], 'GARGPAYQTFVNF': [[-3.0, 2.75]], 'GTRATRYQTFVNF': [[-1.0, 2.75]], 'GAPGTTYQTFVNF': [[-4.0, 2.75]], 'GTKGTRYQTFVNF': [[1.0, 2.75]], 'GEGGTRYQTFVNF': [[-2.0, 2.75]], 'GARWPRYQTFVNF': [[-4.0, 2.688]], 'GA*GTRYQTFVNF': [[-5.0, 2.664]], 'GGRETRYQTFVNF': [[-4.0, 2.625]], 'GTRGTTYQTFVNF': [[-2.0, 2.6]], 'GARETSYQTFVNF': [[-4.0, 2.595]], 'GVRGTKYQTFVNF': [[0.0, 2.548]], 'GAPGTVYQTFVNF': [[-6.0, 2.528]], 'GAMETRYQTFVNF': [[-4.0, 2.5]], 'GARGKGYQTFVNF': [[-4.0, 2.5]], 'GARGTYYQTFVNF': [[-3.0, 2.5]], 'GDRGPRYQTFVNF': [[1.0, 2.5]], 'GAGVTRYQTFVNF': [[-6.0, 2.5]], 'GAAGKRYQTFVNF': [[-3.0, 2.5]], 'GARRGRYQTFVNF': [[-5.0, 2.5]], 'GACVTRYQTFVNF': [[-7.0, 2.5]], 'GMRGTRYQTFVNF': [[-2.0, 2.5]], 'GARWIRYQTFVNF': [[-4.0, 2.5]], 'GALGTWYQTFVNF': [[-6.0, 2.5]], 'GAEGTIYQTFVNF': [[-4.0, 2.5]], 'GARGARYQTFVNF': [[-1.0, 2.5]], 'GAFGTRYQTFVNF': [[-4.0, 2.48]], 'GAPGTMYQTFVNF': [[-4.0, 2.467]], 'GTRCTRYQTFVNF': [[-4.0, 2.467]], 'GTRQTRYQTFVNF': [[-3.0, 2.464]], 'GARVTSYQTFVNF': [[-5.0, 2.45]], 'GTSGTRYQTFVNF': [[-2.0, 2.45]], 'GTGGTRYQTFVNF': [[-3.0, 2.428]], 'GAPGVRYQTFVNF': [[-3.0, 2.417]], 'GEPGTRYQTFVNF': [[-2.0, 2.396]], 'GARGERYQTFVNF': [[-2.0, 2.337]], 'GARWKRYQTFVNF': [[-4.0, 2.333]], 'GAR*TRYQTFVNF': [[-5.0, 2.333]], 'GAPGTSYQTFVNF': [[-4.0, 2.327]], 'GAPGTGYQTFVNF': [[-5.0, 2.317]], 'GARCTRYQTFVNF': [[-4.0, 2.28]], 'GAWGPRYQTFVNF': [[-5.0, 2.267]], 'GEWGTRYQTFVNF': [[-3.0, 2.25]], 'GTNGTRYQTFVNF': [[-1.0, 2.25]], 'GTRGTVYQTFVNF': [[-4.0, 2.231]], 'GAPRTRYQTFVNF': [[-5.0, 2.222]], 'GAPGTCYQTFVNF': [[-6.0, 2.2]], 'GARETCYQTFVNF': [[-6.0, 2.2]], 'GARETKYQTFVNF': [[-1.0, 2.167]], 'GAGWTRYQTFVNF': [[-5.0, 2.167]], 'GARGT*YQTFVNF': [[-5.0, 2.163]], 'GAPGTQYQTFVNF': [[-2.0, 2.131]], 'GTRGTFYQTFVNF': [[-4.0, 2.125]], 'GARPTRYQTFVNF': [[-3.0, 2.122]], 'GTRGSRYQTFVNF': [[0.0, 2.107]], 'GARMTRYQTFVNF': [[-4.0, 2.104]], 'GARQTRYQTFVNF': [[-3.0, 2.103]], 'GAPGARYQTFVNF': [[-3.0, 2.1]], 'GARFTRYQTFVNF': [[-4.0, 2.093]], 'GARSTRYQTFVNF': [[-1.0, 2.089]], 'GGRGPRYQTFVNF': [[-3.0, 2.083]], 'GAGGARYQTFVNF': [[-3.0, 2.083]], 'GARWTKYQTFVNF': [[-1.0, 2.083]], 'GARLTRYQTFVNF': [[-5.0, 2.083]], 'GAPETRYQTFVNF': [[-5.0, 2.071]], 'GARTTRYQTFVNF': [[-3.0, 2.065]], 'GANGTRYQTFVNF': [[-1.0, 2.061]], 'GARYTRYQTFVNF': [[-4.0, 2.045]], 'GAAGTSYQTFVNF': [[-3.0, 2.0]], 'GGSGTRYQTFVNF': [[-3.0, 2.0]], 'GALWTRYQTFVNF': [[-5.0, 2.0]], 'GARGSRYQTFVNF': [[0.0, 2.0]], 'GGRGT*YQTFVNF': [[-6.0, 2.0]], 'GERGTKYQTFVNF': [[2.0, 2.0]], 'GELGTRYQTFVNF': [[-2.0, 2.0]], 'GARWTAYQTFVNF': [[-4.0, 2.0]], 'GARERRYQTFVNF': [[-4.0, 2.0]], 'GARATKYQTFVNF': [[1.0, 2.0]], 'GDGGTRYQTFVNF': [[0.0, 2.0]], 'GARGPQYQTFVNF': [[-1.0, 2.0]], 'GERGTCYQTFVNF': [[-3.0, 2.0]], 'GTRMTRYQTFVNF': [[-4.0, 2.0]], 'GAREGRYQTFVNF': [[-5.0, 2.0]], 'GARVPRYQTFVNF': [[-5.0, 2.0]], 'GTRGPRYQTFVNF': [[-2.0, 2.0]], 'GPRGTRYQTFVNF': [[-1.0, 2.0]], 'GEHGTRYQTFVNF': [[0.0, 2.0]], 'GAPGRRYQTFVNF': [[-4.0, 1.988]], 'GARGTIYQTFVNF': [[-4.0, 1.978]], 'GAKGTRYQTFVNF': [[1.0, 1.907]], 'GAPGTWYQTFVNF': [[-6.0, 1.906]], 'GTLGTRYQTFVNF': [[-3.0, 1.896]], 'GTRGTNYQTFVNF': [[-1.0, 1.875]], 'GERWTRYQTFVNF': [[-2.0, 1.833]], 'GAQGTVYQTFVNF': [[-3.0, 1.81]], 'GARWTSYQTFVNF': [[-4.0, 1.8]], 'GVPGTRYQTFVNF': [[-4.0, 1.778]], 'GARGPWYQTFVNF': [[-5.0, 1.75]], 'GDRGTSYQTFVNF': [[1.0, 1.75]], 'GESGTRYQTFVNF': [[-1.0, 1.75]], 'GAPCTRYQTFVNF': [[-6.0, 1.75]], 'GVRGPRYQTFVNF': [[-3.0, 1.75]], 'GGRGARYQTFVNF': [[-2.0, 1.75]], 'GGRGTKYQTFVNF': [[0.0, 1.75]], 'GARGPRYQTFVNF': [[-2.0, 1.75]], 'GAMGTSYQTFVNF': [[-3.0, 1.75]], 'GADWTRYQTFVNF': [[-5.0, 1.75]], 'GGRVTRYQTFVNF': [[-5.0, 1.75]], 'GARRTRYQTFVNF': [[-3.0, 1.75]], 'GTRGDRYQTFVNF': [[-2.0, 1.743]], 'GAPGTEYQTFVNF': [[-3.0, 1.715]], 'GPPGTRYQTFVNF': [[-3.0, 1.708]], 'GARGTFYQTFVNF': [[-4.0, 1.689]], 'GTRWTRYQTFVNF': [[-3.0, 1.683]], 'GAVGPRYQTFVNF': [[-5.0, 1.667]], 'GTHGTRYQTFVNF': [[-1.0, 1.646]], 'GAPGYRYQTFVNF': [[-5.0, 1.625]], 'GTRKTRYQTFVNF': [[-3.0, 1.625]], 'GTRGNRYQTFVNF': [[-1.0, 1.617]], 'GAPVTRYQTFVNF': [[-6.0, 1.592]], 'GAPATRYQTFVNF': [[-3.0, 1.551]], 'GAPGTLYQTFVNF': [[-5.0, 1.55]], 'GGPGTRYQTFVNF': [[-4.0, 1.521]], 'GAPGTKYQTFVNF': [[-1.0, 1.5]], 'GALVTRYQTFVNF': [[-6.0, 1.5]], 'GARGPMYQTFVNF': [[-3.0, 1.5]], 'GARETFYQTFVNF': [[-6.0, 1.5]], 'GARATSYQTFVNF': [[-2.0, 1.5]], 'GT*GTRYQTFVNF': [[-5.0, 1.5]], 'GTRGKRYQTFVNF': [[-2.0, 1.5]], 'GAGGT*YQTFVNF': [[-7.0, 1.5]], 'GAPGNRYQTFVNF': [[-3.0, 1.5]], 'GVLGTRYQTFVNF': [[-4.0, 1.5]], 'GVRVTRYQTFVNF': [[-5.0, 1.5]], 'GVRGTRYQTFVNF': [[-2.0, 1.5]], 'GARWTYYQTFVNF': [[-5.0, 1.5]], 'GRRGTRYQTFVNF': [[0.0, 1.5]], 'GEGGGRYQTFVNF': [[-4.0, 1.5]], 'GAQVTRYQTFVNF': [[-3.0, 1.5]], 'GACGPRYQTFVNF': [[-5.0, 1.5]], 'GERGTQYQTFVNF': [[1.0, 1.5]], 'GENGTRYQTFVNF': [[0.0, 1.5]], 'GKRGKRYQTFVNF': [[0.0, 1.5]], 'GDRWTRYQTFVNF': [[0.0, 1.5]], 'GAAGPRYQTFVNF': [[-3.0, 1.5]], 'GMRGPRYQTFVNF': [[-3.0, 1.5]], 'GTRVTRYQTFVNF': [[-4.0, 1.482]], 'GAPGTAYQTFVNF': [[-4.0, 1.476]], 'GTRLTRYQTFVNF': [[-5.0, 1.468]], 'GGRGTSYQTFVNF': [[-3.0, 1.458]], 'GQPGTRYQTFVNF': [[0.0, 1.45]], 'GTRGCRYQTFVNF': [[-2.0, 1.417]], 'GAPWTRYQTFVNF': [[-5.0, 1.384]], 'GTRGTIYQTFVNF': [[-4.0, 1.375]], 'GTRPTRYQTFVNF': [[-3.0, 1.375]], 'GARRKRYQTFVNF': [[-4.0, 1.375]], 'GTRGTKYQTFVNF': [[1.0, 1.361]], 'GTRGTRYQTFVNF': [[-1.0, 1.35]], 'GARGGSYQTFVNF': [[-4.0, 1.333]], 'GERATRYQTFVNF': [[0.0, 1.333]], 'GAPGTFYQTFVNF': [[-6.0, 1.333]], 'GLPGTRYQTFVNF': [[-5.0, 1.333]], 'GARRPRYQTFVNF': [[-4.0, 1.333]], 'GARWGRYQTFVNF': [[-5.0, 1.333]], 'GARGNRYQTFVNF': [[-1.0, 1.33]], 'GHRETRYQTFVNF': [[-2.0, 1.312]], 'GTIGTRYQTFVNF': [[-4.0, 1.304]], 'GAPGT*YQTFVNF': [[-7.0, 1.3]], 'GARAPRYQTFVNF': [[-2.0, 1.292]], 'GARGSSYQTFVNF': [[-1.0, 1.25]], 'GASGPRYQTFVNF': [[-3.0, 1.25]], 'GAPGHRYQTFVNF': [[-5.0, 1.25]], 'GTRGERYQTFVNF': [[-2.0, 1.25]], 'GERGTWYQTFVNF': [[-3.0, 1.25]], 'GNPGTRYQTFVNF': [[-2.0, 1.25]], 'GAPGTYYQTFVNF': [[-5.0, 1.25]], 'GAWETRYQTFVNF': [[-6.0, 1.25]], 'GARGASYQTFVNF': [[-2.0, 1.25]], 'GARVTVYQTFVNF': [[-7.0, 1.25]], 'GTRGARYQTFVNF': [[-1.0, 1.214]], 'GDPGTRYQTFVNF': [[0.0, 1.179]], 'GARVGRYQTFVNF': [[-6.0, 1.167]], 'GSRGPRYQTFVNF': [[-1.0, 1.167]], 'GARAKRYQTFVNF': [[-2.0, 1.167]], 'GARITRYQTFVNF': [[-5.0, 1.156]], 'GTRGGRYQTFVNF': [[-3.0, 1.146]], 'GAPGDRYQTFVNF': [[-4.0, 1.136]], 'GAGGTSYQTFVNF': [[-4.0, 1.125]], 'GCRGTSYQTFVNF': [[-5.0, 1.125]], 'GTRTTRYQTFVNF': [[-3.0, 1.087]], 'GLRGTRYQTFVNF': [[-3.0, 1.083]], 'GERGGRYQTFVNF': [[-2.0, 1.083]], 'GNRGTRYQTFVNF': [[0.0, 1.051]], 'GSRGTRYQTFVNF': [[0.0, 1.042]], 'GARVTTYQTFVNF': [[-5.0, 1.0]], 'GALRTRYQTFVNF': [[-5.0, 1.0]], 'GARWTLYQTFVNF': [[-5.0, 1.0]], 'GARVTIYQTFVNF': [[-7.0, 1.0]], 'GARETWYQTFVNF': [[-6.0, 1.0]], 'GATVTRYQTFVNF': [[-5.0, 1.0]], 'GARETLYQTFVNF': [[-5.0, 1.0]], 'GARETIYQTFVNF': [[-6.0, 1.0]], 'GARVTLYQTFVNF': [[-6.0, 1.0]], 'GERGTDYQTFVNF': [[-2.0, 1.0]], 'GARVDRYQTFVNF': [[-5.0, 1.0]], 'GG*GTRYQTFVNF': [[-6.0, 1.0]], 'GADGPRYQTFVNF': [[-4.0, 1.0]], 'GARETQYQTFVNF': [[-2.0, 1.0]], 'GARRTGYQTFVNF': [[-5.0, 1.0]], 'GARGNSYQTFVNF': [[-2.0, 1.0]], 'GERGRRYQTFVNF': [[-1.0, 1.0]], 'GKRGTRYQTFVNF': [[1.0, 1.0]], 'GDRGARYQTFVNF': [[2.0, 1.0]], 'GASVTRYQTFVNF': [[-5.0, 1.0]], 'GAPG*RYQTFVNF': [[-7.0, 1.0]], 'GGRRTRYQTFVNF': [[-4.0, 1.0]], 'GARGPSYQTFVNF': [[-3.0, 1.0]], 'GSRGTGYQTFVNF': [[-2.0, 1.0]], 'GCPGTRYQTFVNF': [[-6.0, 0.958]], 'GARRTSYQTFVNF': [[-4.0, 0.917]], 'GQRGTRYQTFVNF': [[2.0, 0.913]], 'GAPMTRYQTFVNF': [[-6.0, 0.875]], 'GRPGTRYQTFVNF': [[-2.0, 0.864]], 'GAHGPRYQTFVNF': [[-2.0, 0.833]], 'GTRGLRYQTFVNF': [[-2.0, 0.8]], 'GCRGTRYQTFVNF': [[-4.0, 0.789]], 'GHRGTRYQTFVNF': [[0.0, 0.776]], 'GARKTRYQTFVNF': [[-3.0, 0.759]], 'GAGGRRYQTFVNF': [[-4.0, 0.75]], 'GA*GTMYQTFVNF': [[-6.0, 0.75]], 'GAFGPRYQTFVNF': [[-5.0, 0.75]], 'GALGSRYQTFVNF': [[-2.0, 0.75]], 'GARGAKYQTFVNF': [[1.0, 0.75]], 'GMRWTRYQTFVNF': [[-4.0, 0.75]], 'GWRGTRYQTFVNF': [[-3.0, 0.75]], 'GAPGSRYQTFVNF': [[-2.0, 0.714]], 'GIRGTRYQTFVNF': [[-3.0, 0.695]], 'GTRGMRYQTFVNF': [[-2.0, 0.688]], 'GMRGKRYQTFVNF': [[-3.0, 0.667]], 'GRRVTRYQTFVNF': [[-3.0, 0.667]], 'GARGCRYQTFVNF': [[-2.0, 0.652]], 'GAPGGRYQTFVNF': [[-5.0, 0.635]], 'GARGRRYQTFVNF': [[-2.0, 0.629]], 'G*RGTRYQTFVNF': [[-4.0, 0.602]], 'GASWTRYQTFVNF': [[-4.0, 0.583]], 'GARGHRYQTFVNF': [[-3.0, 0.529]], 'GAPGERYQTFVNF': [[-4.0, 0.525]], 'GGLGTRYQTFVNF': [[-4.0, 0.5]], 'GSRRTRYQTFVNF': [[-2.0, 0.5]], 'GSRGTPYQTFVNF': [[-2.0, 0.5]], 'GSRGTSYQTFVNF': [[-1.0, 0.5]], 'GARWTQYQTFVNF': [[-2.0, 0.5]], 'GYPGTRYQTFVNF': [[-4.0, 0.5]], 'GWRGKRYQTFVNF': [[-4.0, 0.5]], 'GRRGRRYQTFVNF': [[-1.0, 0.5]], 'GAQRTRYQTFVNF': [[-2.0, 0.5]], 'GERGARYQTFVNF': [[0.0, 0.5]], 'GEVGTRYQTFVNF': [[-3.0, 0.5]], 'GSPGTRYQTFVNF': [[-2.0, 0.5]], 'GARGKHYQTFVNF': [[-2.0, 0.5]], 'GNRGKRYQTFVNF': [[-1.0, 0.5]], 'GARWMRYQTFVNF': [[-4.0, 0.5]], 'GMPGTRYQTFVNF': [[-4.0, 0.5]], 'GIPGTRYQTFVNF': [[-5.0, 0.5]], 'GRRWTRYQTFVNF': [[-2.0, 0.5]], 'G*PGTRYQTFVNF': [[-6.0, 0.5]], 'GGRGTGYQTFVNF': [[-4.0, 0.5]], 'GARGLRYQTFVNF': [[-2.0, 0.5]], 'GASGRRYQTFVNF': [[-3.0, 0.5]], 'GVRETRYQTFVNF': [[-4.0, 0.5]], 'GERGTFYQTFVNF': [[-3.0, 0.5]], 'GATETRYQTFVNF': [[-4.0, 0.5]], 'GARGWRYQTFVNF': [[-3.0, 0.5]], 'GARRTMYQTFVNF': [[-4.0, 0.5]], 'GARAARYQTFVNF': [[-1.0, 0.5]], 'GARRTVYQTFVNF': [[-6.0, 0.5]], 'GARGEIYQTFVNF': [[-5.0, 0.5]], 'GARGRQYQTFVNF': [[-1.0, 0.5]], 'GAQGKRYQTFVNF': [[-1.0, 0.5]], 'GARWSRYQTFVNF': [[-2.0, 0.5]], 'GALGTMYQTFVNF': [[-4.0, 0.5]], 'GALLTRYQTFVNF': [[-7.0, 0.5]], 'GARWLRYQTFVNF': [[-4.0, 0.5]], 'GA*GGRYQTFVNF': [[-7.0, 0.5]], 'GAVRTRYQTFVNF': [[-6.0, 0.5]], 'GAMGPRYQTFVNF': [[-3.0, 0.5]], 'GERGERYQTFVNF': [[-1.0, 0.5]], 'GRRGPRYQTFVNF': [[-1.0, 0.5]], 'GTRRTRYQTFVNF': [[-3.0, 0.476]], 'GARGQRYQTFVNF': [[-2.0, 0.45]], 'GDRGKRYQTFVNF': [[1.0, 0.417]], 'GKPGTRYQTFVNF': [[-1.0, 0.417]], 'GWPGTRYQTFVNF': [[-5.0, 0.4]], 'GARGMRYQTFVNF': [[-2.0, 0.398]], 'GRRGTSYQTFVNF': [[-1.0, 0.375]], 'GARGRKYQTFVNF': [[0.0, 0.333]], 'GVRGTSYQTFVNF': [[-3.0, 0.333]], 'GARNTRYQTFVNF': [[-1.0, 0.317]], 'GTRGT*YQTFVNF': [[-5.0, 0.311]], 'GARGVRYQTFVNF': [[-1.0, 0.298]], 'GARGIRYQTFVNF': [[-2.0, 0.28]], 'GARG*RYQTFVNF': [[-5.0, 0.279]], 'GFRGTRYQTFVNF': [[-3.0, 0.254]], 'GARWARYQTFVNF': [[-3.0, 0.25]], 'GSRWTRYQTFVNF': [[-2.0, 0.25]], 'GTRGRRYQTFVNF': [[-2.0, 0.25]], 'GAREDRYQTFVNF': [[-4.0, 0.25]], 'GAPGIRYQTFVNF': [[-4.0, 0.25]], 'GAPGQRYQTFVNF': [[-4.0, 0.25]], 'GYRGTRYQTFVNF': [[-2.0, 0.199]], 'GARGYRYQTFVNF': [[-3.0, 0.19]], 'GARRTIYQTFVNF': [[-6.0, 0.167]], 'GKRGTSYQTFVNF': [[0.0, 0.167]], 'GARWTCYQTFVNF': [[-6.0, 0.167]], 'GTR*TRYQTFVNF': [[-5.0, 0.167]], 'GTRGVRYQTFVNF': [[-1.0, 0.167]], 'GAPGWRYQTFVNF': [[-5.0, 0.167]], 'GVRGKRYQTFVNF': [[-3.0, 0.167]], 'GRRETRYQTFVNF': [[-2.0, 0.167]], 'GTRGWRYQTFVNF': [[-3.0, 0.156]], 'GTRGQRYQTFVNF': [[-2.0, 0.125]], 'GARGRSYQTFVNF': [[-3.0, 0.125]], 'GARGGKYQTFVNF': [[-1.0, 0.125]], 'GARGFRYQTFVNF': [[-3.0, 0.116]], 'GTRGFRYQTFVNF': [[-3.0, 0.1]], 'GTRGHRYQTFVNF': [[-3.0, 0.091]], 'GARRARYQTFVNF': [[-3.0, 0.0]], 'GERMTRYQTFVNF': [[-3.0, 0.0]], 'GARWWRYQTFVNF': [[-5.0, 0.0]], 'GRRGTKYQTFVNF': [[2.0, 0.0]], 'GERGVRYQTFVNF': [[0.0, 0.0]], 'GARVSRYQTFVNF': [[-3.0, 0.0]], 'GALETRYQTFVNF': [[-5.0, 0.0]], 'GARGVIYQTFVNF': [[-4.0, 0.0]], 'GAKGTKYQTFVNF': [[3.0, 0.0]], 'GTRITRYQTFVNF': [[-5.0, 0.0]], 'GARWVRYQTFVNF': [[-3.0, 0.0]], 'GWRVTRYQTFVNF': [[-6.0, 0.0]], 'GWRGSRYQTFVNF': [[-2.0, 0.0]], 'GWRGARYQTFVNF': [[-3.0, 0.0]], 'GRRGSRYQTFVNF': [[1.0, 0.0]], 'GERGT*YQTFVNF': [[-4.0, 0.0]], 'GTRGYRYQTFVNF': [[-3.0, 0.0]], 'GSRGARYQTFVNF': [[0.0, 0.0]], 'GSRGDRYQTFVNF': [[-1.0, 0.0]], 'GARGVKYQTFVNF': [[1.0, 0.0]], 'GARET*YQTFVNF': [[-7.0, 0.0]], 'GARRSRYQTFVNF': [[-2.0, 0.0]], 'GARGMSYQTFVNF': [[-3.0, 0.0]], 'GARGRIYQTFVNF': [[-5.0, 0.0]], 'GTRG*RYQTFVNF': [[-5.0, 0.0]], 'GARGVSYQTFVNF': [[-2.0, 0.0]], 'GARGGTYQTFVNF': [[-4.0, 0.0]], 'GARWRRYQTFVNF': [[-4.0, 0.0]], 'GVLGGRYQTFVNF': [[-6.0, 0.0]], 'GVRGARYQTFVNF': [[-2.0, 0.0]], 'GARRT*YQTFVNF': [[-7.0, 0.0]], 'GARTTKYQTFVNF': [[-1.0, 0.0]], 'GAQGCRYQTFVNF': [[-1.0, 0.0]], 'GAQGTKYQTFVNF': [[2.0, 0.0]], 'GSRGTKYQTFVNF': [[2.0, 0.0]], 'GVRGTWYQTFVNF': [[-5.0, 0.0]], 'GGRGSRYQTFVNF': [[-1.0, 0.0]], 'GRRGKRYQTFVNF': [[-1.0, 0.0]], 'GGRGTNYQTFVNF': [[-2.0, 0.0]], 'GA*RTRYQTFVNF': [[-7.0, 0.0]], 'GAGGTTYQTFVNF': [[-4.0, 0.0]], 'GKRWTRYQTFVNF': [[-1.0, 0.0]], 'GKRGIRYQTFVNF': [[0.0, 0.0]], 'GAAETRYQTFVNF': [[-4.0, 0.0]], 'GTRGIRYQTFVNF': [[-2.0, 0.0]], 'GGRGTIYQTFVNF': [[-5.0, 0.0]], 'GRQGTRYQTFVNF': [[1.0, 0.0]], 'GR*GTRYQTFVNF': [[-4.0, 0.0]], 'GRRGIRYQTFVNF': [[-1.0, 0.0]], 'GSRGTTYQTFVNF': [[-1.0, 0.0]], 'GALGWRYQTFVNF': [[-5.0, 0.0]], 'GAREERYQTFVNF': [[-4.0, 0.0]], 'GAKETRYQTFVNF': [[-1.0, 0.0]], 'GDRGSRYQTFVNF': [[3.0, 0.0]], 'GERTTRYQTFVNF': [[-2.0, 0.0]], 'GERGTTYQTFVNF': [[-1.0, 0.0]], 'GLLGTRYQTFVNF': [[-5.0, 0.0]], 'GRLGTRYQTFVNF': [[-2.0, 0.0]], 'GA*GERYQTFVNF': [[-6.0, 0.0]]}

# min_score_val = seqs_scores[min(seqs_scores, key=seqs_scores.get)] #finds lowest value in dictionary
# max_score_val = seqs_scores[max(seqs_scores, key=seqs_scores.get)] #finds highest value in dictionary
# min_index_val = 0
# max_index_val = len(seqs_scores_list)
# flowcontrolplot1 = -1
# plot_guess_dict = {}

peak = 'GERGTRYQTFVNF'

#
# Plots - - - - 
#
plotheight = 500
plotwidth = 1180
seqs = dictionary
plotrect = pygame.Surface((plotwidth,plotheight)) #creating plot bg
plotrect.fill((255,255,255)) #coloring the plot
yvalues = list(map(lambda x:x[0][1], seqs.values()))



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
    
    def enter(self):
        """Called when the screen becomes active"""
        pass
    
    def exit(self):
        """Called when the screen stops being active"""
        pass

# -------------------------------
# Start Screen
# -------------------------------
class StartScreen(Screen):
    #What is in the screen: initialize variables specific to start screen
    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self.button_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 200, 200, 30)
        
        # Create a Figlet title using pyfiglet
        self.figlet_font = pyfiglet.Figlet(font="ticks")
        self.figlet_text = self.figlet_font.renderText("peak")
        
        #adding instructions to be printed
        self.subtitle_lines = [
            "Which TRIM5a variant has the highest antiviral activity?",
            "Pick a starting sequence (5-mer) to complete G-----YQTFVNF",
            "and get its fitness score.",
            "Mutate the sequence to improve the score",
            "You win if you guess the most fit TRIM5a variant!",
            "Hint: Think about the amino acid classes",
            "You have 5 tries.",
            ]
        
        self.bg_image = pygame.image.load("peak_bg.png").convert_alpha()
        self.bg_width = self.bg_image.get_width()
        self.bg_height = self.bg_image.get_height()

        if self.bg_height != HEIGHT:
            scale_factor = HEIGHT / self.bg_height
            self.bg_width = int(self.bg_width * scale_factor)
            self.bg_image = pygame.transform.scale(self.bg_image, (self.bg_width, HEIGHT))
        
        # Render it onto a Pygame surface (we’ll convert ASCII text to a surface)
        self.figlet_surface = self.render_figlet_surface(self.figlet_text)
        
        self.bg_x = 0
        self.scroll_speed = 3  # pixels per frame — tweak this!
        global plotrect
        plotrect.fill((255,255,255))

    def enter(self):
        pygame.mixer.music.load("wildlife-forest-jungle-background-music-328255.mp3")
        pygame.mixer.music.play(-1) #starts playing music
    
    
    #making a figlet surface for peaks
    def render_figlet_surface(self, ascii_text):
        """Convert ASCII figlet text into a pygame surface."""
        lines = ascii_text.split("\n")
        line_surfaces = [MONO_FONT.render(line, True, white) for line in lines]
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
                self.manager.set_screen(GameScreen(self.manager, []))
    
    def update(self):
        # scroll the background
        self.bg_x -= self.scroll_speed
        if self.bg_x <= -self.bg_width:
            self.bg_x = 0  # Reset to loop seamlessly

    #putting things on the screen
    def draw(self, surface):
        surface.blit(self.bg_image, (self.bg_x, 0))
        surface.blit(self.bg_image, (self.bg_x + self.bg_width, 0))
       
        #drawing semi-transparent box behind figlet
        text_x = WIDTH // 2 - self.figlet_surface.get_width() // 2
        text_y = HEIGHT // 4 - self.figlet_surface.get_height() // 2
        rect_padding = 40  # extra space around the text box

        bg_rect = pygame.Rect(
            text_x - rect_padding // 2,
            text_y - rect_padding // 2,
            self.figlet_surface.get_width() + rect_padding,
            self.figlet_surface.get_height() + rect_padding,
        )
        overlay = pygame.Surface((bg_rect.width, bg_rect.height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))  # RGBA: last value = transparency (0–255)
        surface.blit(overlay, (bg_rect.x, bg_rect.y))
        
        #draw figlet surface here in the center
        surface.blit(
            self.figlet_surface,
            (WIDTH//2 - self.figlet_surface.get_width()//2, HEIGHT//4 - self.figlet_surface.get_height()//2)
        )
        
        #print instructions
        y = HEIGHT // 2.2
        for line in self.subtitle_lines:
            txt = small_font.render(line, True, white)
            surface.blit(txt, (WIDTH // 2 - txt.get_width() // 2, y))
            y += 30
        
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
        super().__init__()
        self.manager = manager
        self.input_box = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 200, 200, 50)
        self.active = False
        self.user_text = ""
        self.inputs = inputs
        self.MAX_COUNT = 5
        global peak
        global dictionary
    
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
        og_image = pygame.image.load("amino acid classification.png").convert_alpha() 
        smaller_image = pygame.transform.scale(og_image, (600, 450))

        # Get the image's rectangle and position it
        image_rect = smaller_image.get_rect()
        image_rect.center = (WIDTH // 2 +200, HEIGHT // 2.4)
        surface.blit(smaller_image, image_rect)

        #fonts for the label for the input box
        label_text = medium_font.render("Type in sequence to complete G-----YQTFVNF", True, green)
        label_x = self.input_box.centerx - label_text.get_width() // 2
        label_y = self.input_box.top - 50
        surface.blit(label_text, (label_x, label_y))

        # Draw box to enter onto screen
        txt_surface = small_font.render(self.user_text.upper(), True, black)
        # surface.blit(txt_surface, (self.input_box.x + 20, self.input_box.y + 10))
        surface.blit(txt_surface, (self.input_box.centerx - txt_surface.get_width()//2,
                                    self.input_box.centery - txt_surface.get_height()//2))
        
        #Display previous guesses
        global peak
        y = 50
        for i, text in enumerate(self.inputs):
            seq_aa = 'G'+text+'YQTFVNF'
            if seq_aa in dictionary.keys():
                score=dictionary[seq_aa][0][0]
                activity=dictionary[seq_aa][0][1]
            elif seq_aa not in dictionary.keys():
                score=activity_and_score_seq.sim_score(seq_aa)
                activity=0
            # Create the colored text for this guess
            seq_aa = 'G'+text+'YQTFVNF'
            for j, char in enumerate(seq_aa):
                color = green if char == peak[j] else black
                letter_surface = small_font.render(char, True, color)
                surface.blit(letter_surface, (10 + j * 20, y))
                final_val=10 + j * 20
            line = small_font.render(f'Score:{score}, Activity:{activity}', True, black)
            surface.blit(line, (final_val+30, y))
            y += 30

        # Display count info (how many tries are left)
        count = len(self.inputs)
        count_text = small_font.render(f"Try {count + 1} of {self.MAX_COUNT}", True, red)
        surface.blit(count_text, (20, 15))

# -------------------------------
# Result Screen (after each input)
# -------------------------------
class ResultScreen(Screen):
    #what's on the result screen? if you're including graphs, include the variable here because it needs to exist here!!
    def __init__(self, manager, inputs):
        super().__init__()
        self.manager = manager
        self.inputs = inputs
        self.next = pygame.Rect(WIDTH//2 - 100, HEIGHT - 150, 200, 80)
        self.see_result = pygame.Rect(WIDTH//2 - 100, HEIGHT - 150, 200, 80)      
        global peak
        
        #getting input from previous screen
        if inputs:
            self.last_input = inputs[-1]
            self.seq_aa = 'G'+self.last_input+'YQTFVNF'
            if self.seq_aa in dictionary.keys():
                self.score=dictionary[self.seq_aa][0][0]
                self.activity=dictionary[self.seq_aa][0][1]
            elif self.seq_aa not in dictionary.keys():
                self.score=activity_and_score_seq.sim_score(self.seq_aa)
                self.activity=0
        else:
            self.last_input = ""
            self.result1 = 0
            self.result2 = 0

    def compress_coords(score_x, score_y,-7, 3, 0, 21.2, 1180, 500,compression_strength=0.5):
        # normalize to [0, 1]
        xnorm = (score_x - min_score_value) / (max_score_value - min_score_value)
        ynorm = (score_y - min_activity_value) / (max_activity_value - min_activity_value)

        # center and apply nonlinear compression (symmetric around 0.5)
        x_centered = xnorm - 0.5
        y_centered = ynorm - 0.5

        x_compressed = math.copysign(abs(x_centered) ** compression_strength, x_centered) + 0.5
        y_compressed = math.copysign(abs(y_centered) ** compression_strength, y_centered) + 0.5

        # map back to pixel coordinates
        xval = x_compressed * plotwidth
        yval = plotheight - (y_compressed * plotheight)  # flip Y if origin is top-left

        return xval, yval

    #type of input- currently just have a next button but we can change that
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.next.collidepoint(event.pos):
                # If less than 3 inputs, go back to Game Screen
                if len(self.inputs) < 5:
                    self.manager.set_screen(GameScreen(self.manager, self.inputs))
                    if self.score ==0 and self.activity==21.2:
                        self.manager.set_screen(GameOverScreen(self.manager, self.inputs))
                    else:
                        self.manager.set_screen(GameScreen(self.manager, self.inputs))
                if len(self.inputs)==5:
                    self.manager.set_screen(GameOverScreen(self.manager, self.inputs))
            
    #drawing stuff to surface!               
    def draw(self, surface):
        
        surface.fill(white)
        screen.blit(plotrect, (50,50))
        # title = font.render("Traverse the Peak", True, black)
        # surface.blit(title, (WIDTH//2 - title.get_width()//2, 80))

        #Display previous guesses
        global peak
        y = 50
        for i, text in enumerate(self.inputs):
            seq_aa = 'G'+text+'YQTFVNF'
            if seq_aa in dictionary.keys():
                score=dictionary[seq_aa][0][0]
                activity=dictionary[seq_aa][0][1]
            elif seq_aa not in dictionary.keys():
                score=activity_and_score_seq.sim_score(seq_aa)
                activity=0
            # Create the colored text for this guess
            seq_aa = 'G'+text+'YQTFVNF'
            for j, char in enumerate(seq_aa):
                color = green if char == peak[j] else black
                letter_surface = small_font.render(char, True, color)
                surface.blit(letter_surface, (10 + j * 20, y))
                final_val=10 + j * 20
            line = small_font.render(f'Score:{score}, Activity:{activity}', True, black)
            surface.blit(line, (final_val+30, y))
            y += 30

#Plots - - - -
        activity_range = list(map(lambda x:x[0][1], dictionary.values())) #aka y values
        max_activity_value = max(activity_range)
        min_activity_value = min(activity_range)

        score_range = list(map(lambda x:x[0][0], dictionary.values())) #aka x values
        max_score_value = max(score_range)
        min_score_value = min(score_range)
        
        # for seq in seqs_scores:
        #     yval = seqs_scores[seq] * -1/(max_score_val - min_score_val) * plotheight #converts count scores to the Y value in plot
        #     xval =  seqs_scores_list.index(seq) / (max_index_val - min_index_val) * plotwidth #converts sequence index to the X value in plot
        #     if seq == peak:
        #         pygame.draw.circle(plotrect, color=(0,0,0), center=(xval,yval+20), radius=3)
        #         pygame.draw.circle(plotrect, color=(255,0,0), center=(xval,yval+20), radius=10)
        #     else:
        #         pygame.draw.circle(plotrect, color=(0,0,0), center=(xval,yval), radius=3)
        # input_seq_colors = [250, 200, 150, 100, 50]
        # for seq,color in zip (plot_guess_dict.keys(), input_seq_colors):
        #     yval = plot_guess_dict[seq][0] * -1/(max_score_val - min_score_val) * plotheight #converts count scores to the Y value in plot
        #     xval = plot_guess_dict[seq][1] / (max_index_val - min_index_val) * plotwidth #!!!!!!!!! Using a random number here for input in this case which I dont like
        #     # print(f'This is the input seq score {plot_guess_dict[seq][0]} x value {xval}, this is the y value {yval}, this is the peak {global peak}')
        #     pygame.draw.circle(plotrect, color=(0,color,0), center=(xval,yval), radius=10)

    #populate the graph with all existing seqs
        for seq in seqs:
            score_x = seqs[seq][0][0] + 8
            score_y = seqs[seq][0][1] + 1
            xval,yval = compress_coords(score_x, score_y) #converts count scores to the Y value in plot
            #print(f'max_score = {max_score_value}, min_score = {min_score_value}, max_activity = {max_activity_value}, min_activity = {min_activity_value}')
            pygame.draw.circle(plotrect, color=(0,0,0), center=(xval,yval), radius=3)
    #plot the input seq and check to make sure it's not the peak seq, if it is, it is also plotted
        print(f'this is self.input {self.inputs}')
        for line in self.inputs:
            seq = 'G'+line+'YQTFVNF'
            if seq == peak:
                score_x = 0
                score_y = 21.2 + 1
                yval = plotheight - (score_y/(max_activity_value-min_activity_value)) * plotheight #converts count scores to the Y value in plot
                xval = (score_x/ (max_score_value-min_score_value)) * plotwidth #converts sequence index to the X value in plot
                pygame.draw.circle(plotrect, color=(255,0,0), center=(xval,yval+20), radius=10)
                print ('seq = peak')
            elif seq in seqs:
                score_x = seqs[seq][0][0]+8
                score_y = seqs[seq][0][1] + 1
                yval = plotheight - (score_y/(max_activity_value-min_activity_value)) * plotheight #converts count scores to the Y value in plot
                xval = (score_x/ (max_score_value-min_score_value)) * plotwidth #converts sequence index to the X value in plot
                pygame.draw.circle(plotrect, color=blue, center=(xval,yval), radius=3)
                print('seq in seqs')
            else:
                score_x = activity_and_score_seq.sim_score(seq)
                score_y = 0 + 1
                yval = plotheight - (score_y/(max_activity_value-min_activity_value)) * plotheight #converts count scores to the Y value in plot
                xval = (score_x/ (max_score_value-min_score_value)) * plotwidth #converts sequence index to the X value in plot
                pygame.draw.circle(plotrect, color=(0,255,0), center=(xval,yval), radius=8)
                activity = 0
                print(seq)










        # Draw Next button unless finished
        if len(self.inputs) < 5:
            pygame.draw.rect(surface, blue, self.next, border_radius=10)
            btn_text = small_font.render("Next", True, white)
            surface.blit(btn_text, (
                self.next.centerx - btn_text.get_width() // 2,
                self.next.centery - btn_text.get_height() // 2
            ))
        
        #Draw see results button
        elif len(self.inputs)==5:
            pygame.draw.rect(surface, dark_orchid, self.next, border_radius=10)
            end_text = small_font.render("See how far you got", True, white)
            surface.blit(end_text, (
                self.see_result.centerx - end_text.get_width() // 2,
                self.see_result.centery - end_text.get_height() // 2
            ))
   

#--------------------------------
# Game over screen class
#--------------------------------
class GameOverScreen(Screen):
    
    def __init__(self, manager, inputs):
        super().__init__()
        self.manager = manager
        self.inputs = inputs
        
        #getting input from previous screen
        global peak
        if inputs:
            self.last_input = inputs[-1]
            self.seq_aa = 'G'+self.last_input+'YQTFVNF'
            self.last_input = self.inputs[-1]
            self.seq_aa = 'G'+self.last_input+'YQTFVNF'
            if self.seq_aa in dictionary.keys():
                self.score=dictionary[self.seq_aa][0][0]
                self.activity=dictionary[self.seq_aa][0][1]
            elif self.seq_aa not in dictionary.keys():
                self.score=activity_and_score_seq.sim_score(self.seq_aa)
                self.activity=0

        else:
            self.last_input = ""
            self.score = None
        
        #looping image background
        self.bg_image = pygame.image.load("peak_bg.png").convert_alpha()
        self.bg_width = self.bg_image.get_width()
        self.bg_height = self.bg_image.get_height()
        
        if self.bg_height != HEIGHT:
            scale_factor = HEIGHT / self.bg_height
            self.bg_width = int(self.bg_width * scale_factor)
            self.bg_image = pygame.transform.scale(self.bg_image, (self.bg_width, HEIGHT))
        
        self.bg_x = 0
        self.scroll_speed = 3  # pixels per frame — tweak this!

        self.credits = [
            "Brought to you by:",
            "Jane, Giancarlo, Vivian and Ananya",
            "Spirit guided by: Joshua Lynch",
            "Music: Royalty-free music",
            "Background art: Ananya",
            "Built with Python + Pygame",
            "(with some help from chatGPT)"
        ]
        

    #type of input- currently just have a next button but we can change that
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                main()
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()

    def enter(self):
        pygame.mixer.music.fadeout(1500)
        
        if self.score == 0 and self.activity==21.2:
            pygame.mixer.music.load("awards-ceremony-winner-background-music-330167.mp3")
        else:
            pygame.mixer.music.load("losing-horn-313723.mp3")

        pygame.mixer.music.play()
    
    def update(self):
        # scroll bg
        self.bg_x -= self.scroll_speed
        if self.bg_x <= -self.bg_width:
            self.bg_x = 0  # Reset to loop seamlessly
    
    def draw(self, surface):
        
       surface.blit(self.bg_image, (self.bg_x, 0))
       surface.blit(self.bg_image, (self.bg_x + self.bg_width, 0))
        
       title = font.render("Traverse the Peak", True, white)
       surface.blit(title, (WIDTH//2 - title.get_width() // 2, 60))

       if self.score==0 and self.activity==21.2:
            score_text = medium_font.render(f"You won in {len(self.inputs)} tries", True, light_green)
            
       if self.score!=0 and self.activity!=21.2:
            score_text = medium_font.render(f"Better luck next time! :(", True, white)
        
       score_rect = score_text.get_rect(center=(WIDTH // 2, 150))
       screen.blit(score_text, score_rect)
        
       y = 200
       for line in self.credits:
            txt = credits_font.render(line, True, white)
            surface.blit(txt, (WIDTH // 2 - txt.get_width() // 2, y))
            y += 30


       restart_or_quit=small_font.render("Press escape to quit or Space to restart",True, pinky)
       surface.blit(restart_or_quit, (WIDTH//2 - restart_or_quit.get_width()//2, 550))
        

# -------------------------------
# Screen Manager
# -------------------------------
class ScreenManager:
    def __init__(self):
        self.current_screen = StartScreen(self)
        global peak
        self.current_screen.enter() 
    
    def set_screen(self, screen):
        self.current_screen = screen
        self.current_screen.enter()  

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
    print(dictionary)
    main()
