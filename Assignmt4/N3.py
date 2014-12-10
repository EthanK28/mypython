__author__ = 'ES'
# -*- coding: utf-8 -*-
#def frange(start, stop, step):
#인수 하나 stop start = 0.0, steop 0.1
#인수 두개 start, stop, step =0.1
from decimal import *
def frange(*args):
    start = 0.0
    step = 0.1
    step = round(step, 1)
    frangeArray=[]
    if len(args) == 1:
        frangeArray.append(start)
        while start < args[0]:
            frangeArray.append(start)
            start = start + step
            start = round(start, 1)

        return frangeArray
    if len(args) == 2:
        start = args[0]        

        while start < args[1]:
            frangeArray.append(start)
            start = start + step
            start = round(start, 1)
            
        return frangeArray
    if len(args) >= 3:
        start = args[0]
        step = args[2]
        start = round(start, 1)
        while start < args[1]:
            frangeArray.append(start)
            start = start + step
            
        return frangeArray

print frange(2.2, 4.0, 0.5)
