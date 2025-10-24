#!/usr/bin/env python3
from Bio.Align import substitution_matrices

def count_score(peak,seq):
    '''
    This is a function to calculate a no-gap alignment score between our Peak sequence and our current sequence.
    We take two sequences of the same length and calculate pairwise scores across the alignment iteratively for each pair
    of amino acids in the sequence. It returns the total alignment score that we're calling the 'score'.
    '''
    if len(peak)!=len(seq):
        raise ValueError('Sequences must be the same length')
    
    score=0
    matrix=substitution_matrices.load("BLOSUM62")
    for i in range(len(peak)):
        aa_1=peak[i]
        aa_2=seq[i]
        if aa_1==aa_2:
            continue
        else:
            try:
                score+=matrix[(aa_1,aa_2)]
            except:
                score+=matrix[(aa_2,aa_1)]
    return score


    
