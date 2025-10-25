#!/usr/bin/env python3
import random
import pytest
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

def test_peak_seq():
    try: 
        peak_seq('ABCD')
    except ValueError:
        return
    assert False, "expected ValueError"

#seq_length = int(sys.argv[1]) # could replace this with a specific number
#print(f"peak sequence: {peak_seq(seq_length)}")