from math import e

def treapta(entry_value, teta=0.0, g=1.0, a=1.0):
    if entry_value < teta:
        return 0
    else:
        return 1

def sigmoidala(entry_value, teta=0.0, g=1.0, a=1.0):
    exit_value = 1 / (1 + e ** ((-g) * (entry_value - teta)))
    return exit_value

def signum(entry_value, teta=0.0, g=1.0, a=1.0):
    if entry_value < teta:
        return -1
    else:
        return 1

def tangenta_hiperbolica(entry_value, teta=0.0, g=1.0, a=1.0):
    numarator = (e ** (g * (entry_value - teta)) - e ** ((-g) * (entry_value - teta)))
    numitor = (e ** (g * (entry_value - teta)) + e ** ((-g) * (entry_value - teta)))
    return numarator / numitor

def rampa(entry_value, teta=0.0, g=1.0, a=1.0):
    x = entry_value - teta
    if x < -a:
        return -1
    elif x >= -a and x <= a:
        return x / a
    else:
        return 1

def binarSigmoidala(binar, activationValue):
    if binar:
        if activationValue >= 0.5:
            return 1
        else:
            return 0
    else:
        return activationValue

def binarTangentaHiperbolica(binar, activationValue):
    if binar:
        if activationValue >= 0:
            return 1
        else:
            return -1
    else:
        return activationValue

def binarRampa(binar, activationValue):
    if binar:
        if activationValue >= 0:
            return 1
        else:
            return -1
    else:
        return activationValue