#!/usr/bin/env python3
import pandas as pd
import re
import sys
from Bio.Align import substitution_matrices
import activity_and_score_seq
import pytest

'''This script calls a sequence and looks it up in a dictionary from activity_and_score_seq.py. If that key exists, then x = value[0], y=[1]. Else, the sequence is the string entered into the function sim_score(seq), in which the sequence = seq.'''


def call_x_y(seq_aa):
    dictionary = activity_and_score_seq.score_act_dict()
    if seq_aa in dictionary:
        x = dictionary[seq_aa][0][0]
        y = dictionary[seq_aa][0][1]
        # print(f'The x={x}, y={y}.')
    else:
        x = activity_and_score_seq.sim_score(seq_aa)
        y = 0
        # print(f'The x={x}, y={y}.')
    
    return x, y

#for testing function:
# print(call_x_y('GAPGTPYQTFVNF'))

def test_call_x_y_noinput():
    try:
        call_x_y('')
    except IndexError:
        return
    assert False, 'expected IndexError'

def test_call_x_y_int():
    try:
        call_x_y(12)
    except TypeError:
        return
    assert False, 'expected TypeError'

