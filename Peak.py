#!/usr/bin/env python3

from pyfiglet import Figlet
import generate_all_seq, count_seq, random, time

#variables available
	#generate_all_seqs.py - 

	#vars needed: input_seq_length, player_input1 -> player_input5

#temporary solution ------------------------------------

if True:
	input_seq_length = 5

# ---------------------------------------------------

def main():

	peakmsg = Figlet(font='ticks')
	print(peakmsg.renderText('Peak'))

	all_seqs = generate_all_seq.generate_all_seqs(input_seq_length) # save list of all sequences

	peak_seq = all_seqs[random.randint(0,len(all_seqs))] # determine the peak sequence

	
	#wait for input 

def inputseqfunc():
	inputseq=''
	text1(f'Please enter a sequence of length {input_seq_length}', 300,400) #asks for seq
	pygame.display.flip()
	done = True
	for 


		













if __name__ == "__main__":
	main()
