"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    # Your code goes here
    frequencies = {}
    for i in items:
        k = str(i)
        if k in frequencies :
            frequencies[k] += 1 
        else:
            frequencies[k] = 1
    
    return frequencies
