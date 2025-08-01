# test_1.py 
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from script import addition
from script import addition 
def test_add(): 
    subj = addition(2, 3) 
    assert subj == 5 
