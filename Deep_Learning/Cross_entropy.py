import numpy as np
import math
# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    cross_entropy_t=0
    for i in range(len(Y)):
        cross_entropy_t = cross_entropy_t - float (Y[i]*math.log(P[i])+(1-Y[i])*(math.log(1-P[i])))
    print cross_entropy_t
    return cross_entropy_t