#!/usr/bin/env python3
from Bio.Align import substitution_matrices


def count_score(peak,seq):
    '''
    This is a function to calculate a no-gap alignment score between our Peak sequence and our current sequence.
    We take two sequences of the same length and calculate pairwise scores across the alignment iteratively for each pair
    of amino acids in the sequence. It returns the total alignment score that we're calling the 'score'.
    '''
    amino_acids='A C D E F G H I K L M N P Q R S T V W Y'
    set_AA=set(amino_acids.split(' '))

    if type(peak)!=str or type(seq)!=str:
        raise ValueError('Input should be string')
    if not (set(peak).issubset(set_AA) or set(seq).issubset(set_AA)):
        raise ValueError("Invalid characters in sequence")
    # if len(peak)!=len(seq):
    #     raise ValueError('Sequences must be the same length')
    
    peak=peak.upper()
    seq=seq.upper()

    score=0
    matrix=substitution_matrices.load("BLOSUM62")
    for i in range(len(peak)):
        aa_1=peak[i]
        aa_2=seq[i]
        if aa_1==aa_2:
            continue
        else:
            try:
                #subtracting 3 to everything that is not identical to the value
                score+=matrix[(aa_1,aa_2)]- 3
            except:
                score+=matrix[(aa_2,aa_1)] - 3
                print(i)
    return score

