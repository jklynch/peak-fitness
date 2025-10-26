#!/usr/bin/env python3

#from pyfiglet import Figlet
import generate_all_seq, count_seq, random, time

#variables available
	#generate_all_seqs.py - 

	#vars needed: input_seq_length, player_input1 -> player_input5

#temporary solution ------------------------------------

if True:
	input_seq_length = 5

# ---------------------------------------------------

def main():

	#peakmsg = Figlet(font='ticks')
	#print(peakmsg.renderText('Peak'))

	all_seqs = generate_all_seq.generate_all_seqs(input_seq_length) # save list of all sequences

	peak_seq = all_seqs[random.randint(0,len(all_seqs))] # determine the peak sequence

	##define a dictionary that will score all of the sequences as keys and their scores as values
	seqs_scores= {}
	n = 0
	all_seqs = sorted(all_seqs)
	for seq in all_seqs:
		if seq == peak_seq:
			seqs_scores[seq]= count_seq.count_score(peak_seq,seq)
		elif n == 1000:
			seqs_scores[seq]= count_seq.count_score(peak_seq,seq)
			n = 0
		else:
			n+=1

	
	return seqs_scores, peak_seq
	
if __name__ == '__main__':
	main()
