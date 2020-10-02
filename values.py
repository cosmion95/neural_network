from functions import entry, activation

#defining the lists of values
IL = []
HL1 = []
HL2 = []
HL3 = []
OL = []

withHL2 = False
withHL3 = False

#TODO: call functions from a list
# def test1(x, y):
#     print(str(x+y))

# def test2(x, y):
#     print(str(x-y))

# entry_functions = [
#     test1,
#     test2
# ]

# activation_functions = [
#     activation.rampa,
#     activation.sigmoidala,
#     activation.signum,
#     activation.tangenta_hiperbolica,
#     activation.treapta
# ]

def setWithHL2():
    global withHL2
    withHL2 = True

def setWithHL3():
    global withHL2, withHL3
    withHL2 = True
    withHL3 = True

#find neurons by ID
def findInputLayerNeuronByID(neuronID):
    for neuron in IL:
        if neuron.id == neuronID:
            return neuron

def findHL1NeuronByID(neuronID):
    for neuron in HL1:
        if neuron.id == neuronID:
            return neuron

def findHL2NeuronByID(neuronID):
    for neuron in HL2:
        if neuron.id == neuronID:
            return neuron

def findHL3NeuronByID(neuronID):
    for neuron in HL3:
        if neuron.id == neuronID:
            return neuron

def findHiddenLayerNeuronByID(hiddenLayerNr, neuronID):
    if hiddenLayerNr == 1:
        return findHL1NeuronByID(neuronID)
    elif hiddenLayerNr == 2:
        return findHL2NeuronByID(neuronID)
    elif hiddenLayerNr == 3:
        return findHL3NeuronByID(neuronID)
    else:
        return None

def findOutputLayerNeuronByID(neuronID):
    for neuron in OL:
        if neuron.id == neuronID:
            return neuron


#retrieve link values

def getInputLayerLinkValue(fromNeuronID, toNeuronID):
    for neuron in IL:
        if neuron.id == fromNeuronID:
            for link in neuron.links:
                if link.neuron.id == toNeuronID:
                    return link.value


#---------------------- modify values ----------------------------------
#input neuron value
def modifyInputLayerNeuronValue(neuronID, value):
    for neuron in IL:
        if neuron.id == neuronID:
            neuron.value = value

#input neuron link value to another neuron
def modifyInputLayerLinkValue(fromNeuronID, toNeuronID, value):
    for neuron in IL:
        if neuron.id == fromNeuronID:
            for link in neuron.links:
                if link.neuron.id == toNeuronID:
                    link.value = value
