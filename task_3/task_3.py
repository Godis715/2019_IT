import numpy as np
import math

def splitSet(n, m, ratio):
    """
    Split function for data set
    
    The function divide the set into subsets, which consist from two parts: train and test part.
    This function uses lazy model of evaluations.
    
    Parameters:
    n(int): length of data set
    m(int): required number of subsets
    ratio(float): length of the test part divided by length of the train part
    
    Returns: Sequence of tuples (subset start index, test start index, subset length)
    """
    if (n < m):
        raise ValueError("Number of subsets is more than length of the set")
    length = n // m
    start = 0
    end = length if n % m == 0 else length + 1
    
    for i in range(m):
        currLength = length if i >= n % m else length + 1
        trainStart = math.floor((1 / (ratio + 1)) * currLength)
        yield (start, start + trainStart, start + currLength)
        start += currLength
# tests
print(list(splitSet(n=10, m=3, ratio=0.5)))
print(list(splitSet(n=10, m=4, ratio=0.5)))
print(list(splitSet(n=1000, m=10, ratio=0.3)))
