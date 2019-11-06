import pytest
import sys, os
# This block is not neccessary if you instaled your package
# using e.g. pip install -e
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), # location of this file
            os.pardir, # and one level up, in linux ../
        )
    )
)
# EOBlock

import playground

def test_find_peaks():
    peaks = playground.core.find_peaks([0, 2, 1])
    assert peaks == [2]   
    
def test_find_peaks_two():
    peaks = playground.core.find_peaks([0, 2, 1, 0, 2, 1])
    assert peaks == [2,2] 
    
def test_find_peaks_in_small_list():
    peaks = playground.core.find_peaks([0, 2])
    assert peaks == [] 
