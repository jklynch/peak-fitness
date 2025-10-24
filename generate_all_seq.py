#!/usr/bin/env python3 

#Vivian + Giancarlo Oct 24, 2025

import sys, os, itertools

def generate_all_seqs(num_elements):
    if num_elements > 1:
        aminoacids= list('ARTNCEQGHILKMFPSTWYV')
        all_seq = list(itertools.product(aminoacids, repeat=num_elements))
        return all_seq
    else:
        raise ValueError 

def test_generate_all_seqs ():
    try:
        observed= generate_all_seqs()
    except TypeError:
        return  
    assert False, 'expected TypeError exception, got ({observed})'

def test_zero ():
    try:
        generate_all_seqs(0)
    except ValueError:
        return
    assert False

