#!/usr/bin/env python3
import count_seq
import pytest
##Tests -------------------------------------------------------

def test_count_score_eq_len():
    try:
        count_score('AAA','AAAA')
    except ValueError:
        return
    assert False,'expected ValueError'

def test_count_score_not_string():
    try:
        count_score(1,2)
    except ValueError:
        return
    assert False, 'expected ValueError'

def test_count_seq_invalidAA():
    try:
        count_score('XYZ','OOP')
    except ValueError:
        return
    assert False, 'expected ValueError'