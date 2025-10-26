#!usr/bin/env python3
import pytest
import peak_seq


def test_peak_seq():
    try: 
        peak_seq('ABCD')
    except ValueError:
        return
    assert False, "expected ValueError"

#seq_length = int(sys.argv[1]) # could replace this with a specific number
#print(f"peak sequence: {peak_seq(seq_length)}")