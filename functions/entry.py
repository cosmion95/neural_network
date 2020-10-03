import numpy as np

def suma(inputs):
    suma = 0
    if not inputs:
        return 0
    else:
        for item in inputs:
            suma = suma + item[0] * item[1]
    #print("intorc suma: " + str(suma))
    return suma

def produs(inputs):
    produs = 1
    if not inputs:
        return 0
    else:
        for item in inputs:
            produs = produs * (item[0] * item[1])
    return produs

def minim(inputs):
    minim = 0
    if not inputs:
        return 0
    else:
        minim = inputs[0][0] * inputs[0][1]
        for item in inputs:
            value = item[0] * item[1]
            if value < minim:
                minim = value
    return minim

def maxim(inputs):
    maxim = 0
    if not inputs:
        return 0
    else:
        maxim = inputs[0][0] * inputs[0][1]
        for item in inputs:
            value = item[0] * item[1]
            if value > maxim:
                maxim = value
    return maxim


def format_float(num):
    return np.format_float_positional(num, trim='-')



