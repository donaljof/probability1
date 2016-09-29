# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 11:02:58 2016

@author: donaljof
"""
from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction

#choose function stolen from stack exchange
def nCk(n,k): 
  return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )

def lot_probability(ops, paths):
    p1 = (pow((1.0 - 1.0/paths),(ops - 1)))
    p2 = sum((nCk(ops, x)*pow((1.0/paths),x)) for x in range(ops + 1)[1:])
    #p3 = nCk(ops, 0)*pow((1.0/paths),0)
    return p1*p2

for i in range(20):
    print lot_probability(i, 3)
