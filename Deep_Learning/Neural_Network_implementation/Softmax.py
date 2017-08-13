import numpy as np
import math   # This will import math module
exp_l = []
p_exp = []

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    sumExpl=0.0
    expL = np.exp(L)
    print "expl",expL
    sumExpL = sum(expL)
    print "sumExpl",sumExpL
    result = []
    for i in expL:
        print "i",i
        result.append(i*1.0/sumExpL)
    return result


L = [-1,-2, 0,1, 2]
ex_list = softmax(L)
print "ex_list",ex_list

l = [2,3,4,7]

for i in l:
    print "no.",i