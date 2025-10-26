#!/usr/bin/env python3
import random
import sys

# take an input sequence
# then make it any other sequence of same length - choosing from list of 20 aa
# set that sequence as our "peak_peptide"

#def function()
#return a string

def peak_seq(seq_length):
    '''This is a function to pick a random peptide sequence based on user defined sequence lenght.'''

    if not isinstance(seq_length, int):
        raise ValueError("Not an intenger")
    
    amino_acids = 'ACDEFGHIKLMNPQRSTVWY'
    peak_seq = ''.join([random.choice(amino_acids) for _ in range(seq_length)])
    
    return peak_seq

