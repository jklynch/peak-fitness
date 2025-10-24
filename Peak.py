#!/usr/bin/env python3

from pyfiglet import Figlet
import generate_all_seq, count_seq, random

#variables available
	#generate_all_seqs.py - 

	#vars needed: input_seq_length

#temporary solution ------------------------------------

if True:
	input_seq_length = 5

# ---------------------------------------------------

def main():

	peakmsg = Figlet(font='ticks')
	print(peakmsg.renderText('Peak'))

all_seqs = generate_all_seq.generate_all_seqs(input_seq_length) # save list of all sequences

peak_seq = all_seqs[random.randint(0,len(all_seqs))] # determine the peak sequence
















if __name__ == "__main__":
	main()
